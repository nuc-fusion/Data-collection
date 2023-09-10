from lxml import html, etree
import html as html2
import emoji
import time, copy, random
import json, re, os
from typing import Optional, Tuple, Union, List, Callable, Dict, Any

REDUCE_HTML = os.environ.get('REDUCE_HTML') if os.environ.get('REDUCE_HTML') else False
MAX_TAG_NUM = int(os.environ.get('MAX_TAG_NUM')) if os.environ.get('MAX_TAG_NUM') else 350

NORM_WINDOW = {
    "top": 0,
    "left": 0,
    "bottom": 1080,
    "right": 1920,
    "x": 1920,
    "y": 1080
}

class TreeTool:
    def __init__(self, ctx: str) -> None:
        self.target = '' # used for contriever
        self.current_url = ''
        self.id2xpath = {} # set by _label()
        self.keep_list = {}
        self.label_dict = {}
        self.elem_bounding = {}
        self.append_url_list = []
        self.window = NORM_WINDOW
        self.tree_init(ctx)
    
    def set_current_url(self, url):
        self.current_url = url
        
    def get_extra_url_list(self, n: int = 3):
        if len(self.append_url_list) > n:
            tar_id = random.sample(range(len(self.append_url_list)), n)
            return [self.append_url_list[i] for i in tar_id]
        return self.append_url_list
        
    def set_keep_list(self, keep_list):
        self.keep_list = keep_list
        
    def set_rect_list(self, rect_list: List[Dict]):
        self.elem_bounding = copy.deepcopy(rect_list)
        
    def set_target(self, target):
        self.target = target
        
    def set_window(self, window):
        self.window = window
    
    def tree_init(self, ctx: str):
        def _ctx2tree(ctx: str):
            def _extract(text):
                if text is None:
                    return ''
                text = re.sub(r"\s+", ' ', text).strip()
                return text
            
            # remove emoji and special characters
            ctx = emoji.replace_emoji(ctx, replace='')
            ctx = re.sub(u'([^\u0020-\u0204\u0400-\u04ff\u3400-\u4db5\u4e00-\u9fa5])', '', ctx)

            # remove useless tags, eg. style and script
            ctx = re.sub('<!--[\W\w]*?-->', '', ctx)
            ctx = re.sub('<style[\W\w]*?>[\W\w]*?</style>', '', ctx)
            ctx = re.sub('<script[\W\w]*?>[\W\w]*?</script>', '', ctx)
            ctx = _extract(ctx)
            dom_tree = html.fromstring(ctx)
            
            return dom_tree

        def _label():
            def _get_xpath(element):
                xpath = ''
                while element is not None:
                    # Find the element's index within its parent
                    if 'id' in element.attrib:
                        xpath = '//*[@id="' + element.attrib['id'] + '"]' + xpath
                        break

                    # Back to root
                    if element.tag == 'body':
                        xpath = '/html/body' + xpath
                        break

                    parent = element.getparent()

                    # Element is 'root'
                    if parent is None:
                        xpath = '/' + element.tag.lower() + xpath
                        break

                    is_found = False
                    tot_ix = 0
                    ix = 0
                    
                    # iterate siblings and find the index
                    children = parent.getchildren()
                    for sibling in children:
                        if sibling == element:
                            is_found = True
                        if sibling.tag == element.tag:
                            if is_found == False:
                                ix += 1
                            tot_ix += 1

                    suffix = f'[{ix + 1}]' if tot_ix > 1 else ''
                    xpath = '/' + element.tag.lower() + suffix + xpath

                    # iterate parent node
                    element = parent

                return 'xpath/' + xpath
            
            id = 0
            i2xpath = {}
            nodes = self.dom_tree.xpath('//*') # get all nodes
            for e in nodes:
                e.attrib['temp_id'] = str(id) # set temp_id to etree's nodes
                i2xpath[str(id)] = _get_xpath(e)
                id += 1
            return i2xpath
        
        self.dom_tree = _ctx2tree(ctx)
        self.id2xpath = _label() # set number label
    
    def get_xpath_dict(self):
        return self.id2xpath
    
    def _get_root(self, tree):
        root = tree.xpath('/html')[0]
        return root

    def tree2str(self, tree):
        root = self._get_root(tree)
        html_str = etree.tostring(root, pretty_print=True, method='html').decode()
        res = html2.unescape(html_str)
        return res
    
    def node2str(self, node):
        html_str = etree.tostring(node, method='html').decode()
        res = html2.unescape(html_str)
        return res
    
    def add_attributes(self):
        def _is_elem_clickable(elem):
            tag = elem.tag
            is_clickable = False
            elem_disabled = 'disabled' in elem.attrib and elem.attrib['disabled']
            elem_readonly = 'readonly' in elem.attrib and elem.attrib['readonly']
            
            if 'onclick' in elem.attrib or 'href' in elem.attrib:
                is_clickable = True
            elif 'role' in elem.attrib:
                if elem.attrib['role'].lower() in [
                    "button",
                    "tab",
                    "link",
                    "checkbox",
                    "menuitem",
                    "menuitemcheckbox",
                    "menuitemradio",
                    "radio",
                ]:
                    is_clickable = True
            elif 'contentEditable' in elem.attrib:
                if elem.attrib['contentEditable'].lower() in ["", "contenteditable", "true"]:
                    is_clickable = True

            if not is_clickable and "jsaction" in elem.attrib:
                jsaction_rules = elem.attrib["jsaction"].split(";")
                for jsaction_rule in jsaction_rules:
                    rule_split = jsaction_rule.strip().split(":")
                    # if (1 <= len(ruleSplit) <= 2):
                    #     # 如果规则长度为1
                    #     if len(rule_split) == 1:
                    #         # 拆分规则字符串并赋值给eventType, namespace, actionName，如果没有获取到对应值，则使用默认值["_"]
                    #         eventType, namespace, actionName = ["click", *rule_split[0].strip().split("."), "_"]
                    #     else:
                    #         # 如果规则长度不为1，则拆分规则字符串并赋值给eventType, namespace, actionName，如果没有获取到对应值，则使用规则中的 对应部分和默认值["_"]
                    #         eventType, namespace, actionName = [rule_split[0], *rule_split[1].strip().split("."), "_"]
                    #     if not is_clickable:
                    #         is_clickable = (eventType == "click") and (namespace != "none") and (actionName != "_")
            
            # other clickable elements
            if tag == 'a':
                is_clickable = True
            elif tag == 'textarea':
                if not is_clickable:
                    is_clickable = not elem_disabled and not elem_readonly
            elif tag == 'input':
                _type = elem.attrib['type'] if 'type' in elem.attrib else None
                if not is_clickable:
                    isClickable = not ((_type and (_type.lower() == "hidden")) or elem_disabled or elem_readonly)
            elif tag == 'button' or tag == 'select':
                if not is_clickable:
                    is_clickable = not elem_disabled
            elif tag == 'object' or tag == 'embed':
                is_clickable = True
            elif tag == 'label':
                is_clickable = True
            elif tag == 'img':
                if 'alt' in elem.attrib:
                    is_clickable = True
            elif tag == 'ul' or tag == 'ol':
                is_clickable = True
            elif tag == 'details':
                is_clickable = True
                
            return is_clickable
    
        def _is_elem_visible(rect):
            # unjudgeable element
            if rect is None:
                return False
            
            # promise the node is in current window
            if rect['bottom'] >= 0 and rect['right'] >= 0 and rect['top'] <= self.window['y'] and rect['left'] <= self.window['x']:
                return True
            # element is out of window
            return False
        
        # turn bool to etree value
        def _bool_convert(op: bool):
            return '1' if op else '0'

        def _get_text(str):
            if str is None:
                return ''
            str = re.sub('[<>()\{\}\[\]]', '', str.strip())
            return str
            
        def _get_bounding(xpath):
            if xpath in self.elem_bounding:
                return self.elem_bounding[xpath]
            return None
            
        def _dfs(node):
            # basic information
            id = node.attrib['temp_id']
            tag = node.tag

            # get rect
            xpath = self.id2xpath[id]
            rect = _get_bounding(xpath)
            
            # new attributes
            clickable = _is_elem_clickable(node)
            visible = _is_elem_visible(rect)
            
            # check if any children clickable
            children = node.getchildren()
            for e in children:
                visible = _dfs(e) or visible

            # element which is keeped equivalent to visible
            in_keep_list = True if id in self.keep_list else False
            clickable = clickable or in_keep_list
            visible = visible or in_keep_list
            
            # get text or alt_text of current element
            if tag == 'img' and 'alt' in node.attrib:
                node_text = _get_text(node.attrib['alt'])
            else:
                node_text = _get_text(node.text)
            
            node.attrib['temp_clickable'] = _bool_convert(clickable)
            node.attrib['temp_visible'] = _bool_convert(visible)
            node.attrib['temp_value'] = node_text[:500]
        
        # start from here
        root = self._get_root(self.dom_tree)
        _dfs(root)

    def keep_useful_elements(self):
        # turn etree value to bool
        def _bool_convert(op: str):
            return True if op == '1' else False
        
        def _get_url_from_href(node):
            if 'href' not in node.attrib:
                return None
            
            def _valid_url(url):
                last = url.split('/')[-1]
                if len(re.findall('[.&?]', last)) == 0:
                    return True
                if last.count('.') == 1:
                    if last.split('.')[-1] in ['html', 'htm']:
                        return True
                    return False
                return False
            
            url = node.attrib['href']
            # get absolute url
            if url.startswith('//'):
                url = 'http:' + url
            # concat relative url
            elif url.startswith('/'):
                url = self.current_url + url
            
            # only parse url start with http
            if url.startswith('http') and _valid_url(url):
                return url
            
            return None
        
        def _dfs(node):
            # useful infomations
            id = node.attrib['temp_id']
            tag = node.tag
            xpath = self.id2xpath[id]
            
            # get tempeorary attributes
            clickable = _bool_convert(node.attrib['temp_clickable'])
            visible = _bool_convert(node.attrib['temp_visible'])
            
            # handle inner text
            node_text = node.attrib['temp_value']
            length = len(node_text)
            have_text = True if length > 0 else False
            keep = (clickable or have_text) and visible
            
            # get child elements
            child_list = []
            url_list = []
            children = node.getchildren()
            for e in children:
                nmsg, cmsg = _dfs(e)
                keep = keep or cmsg['keep']
                length += cmsg['text_length']
                url_list += cmsg['url_list']
                if nmsg is not None:
                    child_list.append(nmsg)
            
            # handle new urls
            url = _get_url_from_href(node)
            if url is not None:
                url_list.append(url)
                
            # control message for current node
            control_msg = {
                'text_length': length if keep else 0,
                'keep': keep,
                'url_list': url_list,
            }
            
            # remove current node if none of the children should be keeped
            if not keep:
                return None, control_msg
            
            # reconstruct node
            node_msg = {
                'id': id,
                'tag': tag,
                'text': node_text,
                'xpath': xpath,
                'child': child_list,
                'clickable': clickable,
                'have_text': have_text,
            }
            
            return node_msg, control_msg
    
        root = self._get_root(self.dom_tree)
        json_obj, control_msg = _dfs(root)
        
        self.append_url_list = list(set(control_msg['url_list']))
        return json_obj, control_msg['text_length']
    
    def pack_object(self, obj):
        def _id2label(idx: int):
            c0 = idx // 676
            c1 = (idx // 26) % 26
            c2 = idx % 26
            label = f'{chr(c1 + 65)}{chr(c2 + 65)}'
            return label if c0 == 0 else f'{chr(c0 + 64)}{label}'
        
        def _dfs(obj):
            if obj is None:
                return '', {
                    'have_clickable': False,
                    'clickable_list': [],
                    'id2labels': {}
                }
            
            # tag attributes
            id = obj['id']
            tag = obj['tag']
            clickable = obj['clickable']
            have_text = obj['have_text']
            
            # results
            parts = []
            id_list = []
            labels = {}
            
            if clickable:        
                # update label
                labels[id] = label = _id2label(self.obj_label_id)
                self.obj_label_id += 1
                
                # save clickable id
                id_list.append(id)
                labels[id] = label
                parts.append(f'{tag}[{label}]')
            
            if have_text:
                parts.append(obj['text'])
            
            clickable_count = 0
            for child in obj['child']:
                cres, cmsg = _dfs(child)        
                clickable_count += 1 if cmsg['have_clickable'] else 0
                id_list += cmsg['clickable_list']
                labels.update(cmsg['id2labels'])
                if len(cres) != 0:
                    parts.append(cres)
 
            # concat node result
            res = ' '.join(parts)
            if clickable_count > 1 or clickable:
                if res[0] == '<':
                    res = ' ' + res
                if res[-1] == '>':
                    res = res + ' '
                res = f'<{res}>'
                
            control_msg = {
                'have_clickable': clickable or clickable_count,
                'clickable_list': id_list,
                'id2labels': labels
            }
            
            return res, control_msg
        
        self.obj_label_id = 0
        res, control_msg = _dfs(obj)
        
        cl_list = control_msg['clickable_list']
        labels = control_msg['id2labels']
        self.label_dict = labels
        # print(res)
        # print(f'[Clickable] {len(cl_list)}, {len(res)}')
        
        return {
            'html': res,
            'clickable_list': cl_list, 
            'clickable_labels': labels
        }
        
    def parse_tree(self):  
        self.add_attributes()
        obj, len = self.keep_useful_elements()
        # contriever if needed
        
        packed = self.pack_object(obj)
        return packed
           
    def label2id(self, tag):
        keys = list(self.label_dict.keys())
        values = list(self.label_dict.values())
        try:
            pos = values.index(tag)
            return keys[pos] 
        except:
            return None
        
    def xpath2id(self, xpath):
        keys = list(self.id2xpath.keys())
        values = list(self.id2xpath.values())
        
        try:
            pos = values.index(xpath)
            return keys[pos] 
        except:
            return None
        
    def id2label(self, id):
        return self.label_dict[id] if id in self.label_dict else None
        
    def get_label_by_xpath(self, xpath):
        id = self.xpath2id(xpath)
        if id is None:
            return None
        return self.id2label(str(id))
        
    def get_xpath_by_id(self, id: str):
        try:
            xpath = self.id2xpath[id]
            xpath = xpath.replace("xpath", "xpath=", 1).replace("//*[", "/*[")
            return xpath
        except:
            return None
    
    def get_xpath_by_label(self, label):
        id = self.label2id(label)
        if id is None:
            return None
        return self.get_xpath_by_id(id)
    
    def print_html_object(self, obj):
        tab_cnt = 0
        for ch in obj:
            if ch == '<':
                print()
                print('  ' * tab_cnt, end='')
                print('<', end = '')
                tab_cnt += 1
            elif ch == '>':
                tab_cnt -= 1
                print('>')
                print('  ' * tab_cnt, end='')
            else:
                print(ch, end='')

if __name__ == '__main__':
    for _, _, files in os.walk('files'):
        
        for fn in files:
            if fn[-4:] != 'json':
                continue
            
            with open(f'files/{fn}', 'r', encoding='utf8') as f:
            
            # with open('src/600/recact_6.json', 'r', encoding='utf8') as f:
                json_data = json.load(f)

            # for obj in json_data['action']:
            #     if 'html' not in obj:
            #         continue
            #     if obj['type'] == 'scrollend':
            #         continue
            #     print(obj['type'])
            #     ctx = obj['html']
            #     rect = obj['elementPosNSize']
            
                url = json_data['url']
                ctx = json_data['src_html']
                info = json_data['rect']
                
                rect = {}
                for k, v in info.items():
                    rect[v['src_xpath']] = v['rect']

                tree = TreeTool(ctx)
                tree.set_current_url(url)
                tree.set_rect_list(rect)
                tree.parse_tree()
                print(tree.get_extra_url_list())
                
                # tree.set_keep_list(['84'])
                # obj = tree.dump_tree()
                # print(obj)
                # res = tree.pack_object(obj)
                # print(res)

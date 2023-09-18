import json, os, re, random
from tqdm import tqdm

htmls = []
files = os.listdir('/workspace/hanyu/ryl/phase2/')
for file in tqdm(files[:20000]):
    if file.startswith('obj_') and file.endswith('.json'):
        with open('/workspace/hanyu/ryl/phase2/'+file, 'r') as f:
            try:
                html = json.load(f)
                htmls.append(html)
            except:
                continue

cn_urls = []

tag_to_cn = {
    'a': '链接',
    'img': '图片',
    'input': '输入框',
    'button': '按钮',
    'select': '下拉框',
    'dt': '框图',
    'ul': '列表',
    'ol': '列表',
    'li': '列表项',
    'div': '区域',
    'span': '区域',
    'p': '段落',
    'h1': '标题',
    'h2': '标题',
    'h3': '标题',
    'area': '区域',
    'map': '地图',
    'table': '表格',
    'tr': '表格行',
    'td': '表格列',
    'th': '表格列',
}

tag_to_en = {
    'a': 'link',
    'img': 'image',
    'input': 'input box',
    'button': 'button',
    'select': 'drop-down box',
    'dt': 'frame',
    'ul': 'list',
    'ol': 'list',
    'li': 'list item',
    'div': 'div',
    'span': 'span',
    'p': 'paragraph',
    'h1': 'title',
    'h2': 'title',
    'h3': 'title',
    'area': 'area',
    'map': 'map',
    'table': 'table',
    'tr': 'table row',
    'td': 'table column',
    'th': 'table column',
}

with open('web_cn.txt', 'r') as f:
    for line in f:
        url = line.strip()
        url = "http://" + url if not url.startswith("http") else url
        cn_urls.append(url)

def main():
    data_id = 0
    for html in tqdm(htmls):
            url = html['url']
            matches = re.findall(r'<(.*?)\[(.*?)\](.*?)>', html['html'])
            tags_types = []
            tags = []
            labels = []
            texts = []
            for match in matches:
                tag = match[0]
                label = match[1]
                text = match[2]
                if tag == '' or '<' in tag or '>' in tag or '[' in tag or ']' in tag:
                    continue
                if label == '' or '<' in label or '>' in label or '[' in label or ']' in label:
                    continue
                if '<' in text or '>' in text or '[' in text or ']' in text:
                    continue
                tags.append(tag)
                labels.append(label)
                texts.append(text)
                if tag not in tags_types and tag != 'a':
                    tags_types.append(tag)
                # if tag not in tags_types:
                #     tags_types.append(tag)
            elem_infos = []
            for tag, label, text in zip(tags, labels, texts):
                elem_infos.append({'tag': tag, 'label': label, 'text': text})
            if len(elem_infos) == 0:
                continue
            if len(tags_types) == 0:
                selected_tag = 'a'
            else:   
                selected_tag = random.choice(tags_types)
            # selected_tag = random.choice(tags_types)
            selected_elem_set = []
            for elem_info in elem_infos:
                if elem_info['tag'] == selected_tag:
                    selected_elem_set.append(elem_info)
            selected_elem = random.choice(selected_elem_set)
            label = selected_elem['label']
            tag = selected_elem['tag']
            text = selected_elem['text'].strip()
            elem_ = None
            for elem in html['info'].values():
                if 'label' in elem and elem['label'] == label and elem['rect'] is not None:
                    elem_ = elem
                    break
            if elem_ is None:
                continue
            pos_x = elem_['rect']['x']
            pos_y = elem_['rect']['y']                   
            try:
                html_width = 1080
                html_height = 720
                rel_x = pos_x / html_width
                rel_x = round(rel_x, 2)
                rel_y = pos_y / html_height
                rel_y = round(rel_y, 2)
            except:
                continue
            if url not in cn_urls:
                querys = []
                querys.append(f"According to the screenshot and html, what is the element at position ({rel_x}, {rel_y})? What is its content?")
                querys.append(f"Tell me what's located at ({rel_x} {rel_y}) and what its content is based on the screenshot and html.")
                querys.append(f"What can be found at the ({rel_x} {rel_y}) coordinates according to the screenshot and html? What is its content?")
                querys.append(f"Please provide the info about the element at position ({rel_x} {rel_y}) based on the screenshot and html.")
                querys.append(f"What's stored at the ({rel_x} {rel_y}) position according to the screenshot and html? What is its content?")
                querys.append(f"Based on the screenshot and html, give me the information at coordinates ({rel_x} {rel_y}).")
                querys.append(f"According to the screenshot and html, what exists at ({rel_x} {rel_y}) on the grid? What is its content?")
                querys.append(f"I'd like to know what's situated at ({rel_x} {rel_y}) and its content based on the screenshot and html.")
                querys.append(f"Inform me about the element present at ({rel_x} {rel_y}) according to the screenshot and html.")
                query = random.choice(querys)
                if tag not in tag_to_en:
                    continue
                if text.strip() == '':
                    target = f"The element at the specified position is {label}. It is {'an' if tag_to_en[tag][0] in ['a', 'e', 'i', 'o', 'u'] else 'a'} {tag_to_en[tag]}."
                else:
                    target = f"The element at the specified position is {label}. It is {'an' if tag_to_en[tag][0] in ['a', 'e', 'i', 'o', 'u'] else 'a'} {tag_to_en[tag]} with content \"{text}\"."
            else:
                querys = []
                querys.append(f"根据截图和html文件，请问 ({rel_x} {rel_y}) 这个位置上的元素是什么？它的内容是什么？")
                querys.append(f"在坐标 ({rel_x} {rel_y}) 处有什么元素, 内容是什么？根据截图和html文件回答")
                querys.append(f"基于截图和html文件来看，请告诉我 ({rel_x} {rel_y}) 处的元素及其内容是什么。")
                querys.append(f"根据截图和html文件，在 ({rel_x} {rel_y}) 这个位置上有什么元素？它的内容是什么？")
                querys.append(f"位于 ({rel_x} {rel_y}) 处的是什么元素？有什么内容？基于截图和html文件回答。")
                querys.append(f"请根据截图和html文件提供坐标 ({rel_x} {rel_y}) 上的元素相关信息。")
                querys.append(f"根据截图和html文件，位于 ({rel_x} {rel_y}) 的位置上有什么元素？内容又是什么？")
                query = random.choice(querys)
                if tag not in tag_to_cn:
                    continue
                if text.strip() == '':
                    target = f"指定位置的元素是{label}。它是一个{tag_to_cn[tag]}。"
                else:
                    target = f"指定位置的元素是{label}。它是一个内容为“{text}”的{tag_to_cn[tag]}。"
            oldpath = f"/workspace/hanyu/ryl/phase2/screenshot_mark/screenshot_{html['id']}.png"
            newpath = f"/workspace/hanyu/cyx/turbo_data/img_mark_useful/screenshot_{html['id']}.png"
            if os.path.exists(oldpath) == False:
                print('no img')
                continue
            if os.path.exists(newpath) == False:
                os.system(f"cp {oldpath} {newpath}")
            img = newpath
            with open('elem_pos_sample.jsonl', 'a') as f:
                f.write(json.dumps({'url': html['url'], 'target': target, 'img': img, 'html':html['html'] , 'source':query, 'id': data_id}, ensure_ascii=False) + '\n')
            data_id += 1
if __name__ == '__main__':
    main()
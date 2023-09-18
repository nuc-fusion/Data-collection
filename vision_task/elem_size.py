import json, os, re, random
from tqdm import tqdm
import random

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

with open('web_cn.txt', 'r') as f:
    for line in f:
        url = line.strip()
        url = "http://" + url if not url.startswith("http") else url
        cn_urls.append(url)

def main():
    data_id = 0
    for html in tqdm(htmls):
        info = html['info']
        elems = []
        labels = re.findall(r'img\[([A-Z][A-Z])\]', html['html'])
        if len(labels) < 2:
            continue
        label_1, label_2 = random.sample(labels, 2)
        elem1 = None
        elem2 = None
        for elem in info.values():
            if elem['rect'] is None:
                continue
            if 'label' not in elem:
                continue
            if elem['label'] == label_1:
                elem1 = elem
            elif elem['label'] == label_2:
                elem2 = elem
        if elem1 is None or elem2 is None:
            continue
        
        url = html['url']
        if url not in cn_urls:
            querys = []
            querys.append(f"Which of the elements, {elem1['label']} or {elem2['label']}, is bigger in size?")
            querys.append(f"Is {elem1['label']} or {elem2['label']} the larger element in terms of size?")
            querys.append(f"{elem1['label']} and {elem2['label']}—which one has a greater size?")
            querys.append(f"Which element, {elem1['label']} or {elem2['label']}, possesses a larger size?")
            querys.append(f"Is {elem1['label']} bigger in size than {elem2['label']}?")
            querys.append(f"Which element is more substantial in size, {elem1['label']} or {elem2['label']}?")
            querys.append(f"Comparing {elem1['label']} and {elem2['label']}, which one is larger in size?")
            querys.append(f"Which of the two elements, {elem1['label']} or {elem2['label']}, is the bigger one in terms of size?")
            querys.append(f"Which element, {elem1['label']} or {elem2['label']}, exhibits a greater size?")
            query = random.choice(querys)
            
        else:
            querys = []
            querys.append(f"哪个元素的尺寸更大？{elem1['label']} 还是 {elem2['label']}？")
            querys.append(f"{elem1['label']} 和 {elem2['label']} 中哪一个尺寸更大？")
            querys.append(f"{elem1['label']} 和 {elem2['label']} 之间，哪个元素尺寸更大？")
            querys.append(f"哪一个元素的大小更大，{elem1['label']} 还是 {elem2['label']}？")
            querys.append(f"{elem1['label']} 和 {elem2['label']}，哪一个更大？")
            querys.append(f"{elem1['label']} 和 {elem2['label']} 中，哪个元素的尺寸较大？")
            querys.append(f"{elem1['label']} 和 {elem2['label']} 中，哪一个更占空间？")
            querys.append(f"{elem1['label']} 和 {elem2['label']}，哪一个的尺寸更大？")
            querys.append(f"在 {elem1['label']} 和 {elem2['label']} 中，哪个元素更大？")
            query = random.choice(querys)
        
        rect1 = elem1['rect']
        rect2 = elem2['rect']
        
        target = None
        if url not in cn_urls:
            if rect1['width'] > rect2['width'] and rect1['height'] > rect2['height']:
                target = f"{elem1['label']} is larger in size."
            elif rect1['width'] == rect2['width'] and rect1['height'] == rect2['height']:
                target = f"They are same in size."
            elif rect1['width'] < rect2['width'] and rect1['height'] < rect2['height']:
                target =f"{elem2['label']} is larger in size."
        else:
            if rect1['width'] > rect2['width'] and rect1['height'] > rect2['height']:
                target = f"{elem1['label']} 的尺寸更大。"
            elif rect1['width'] == rect2['width'] and rect1['height'] == rect2['height']:
                target = f"它们的尺寸相同。"
            elif rect1['width'] < rect2['width'] and rect1['height'] < rect2['height']:
                target =f"{elem2['label']} 的尺寸更大。"
        
        if target is not None:
            oldpath = f"/workspace/hanyu/ryl/phase2/screenshot_mark/screenshot_{html['id']}.png"
            newpath = f"/workspace/hanyu/cyx/turbo_data/img_mark_useful/screenshot_{html['id']}.png"
            if os.path.exists(oldpath) == False:
                        print('no img')
                        continue
            if os.path.exists(newpath) == False:
                        os.system(f"cp {oldpath} {newpath}")
            img = newpath
            with open('elem_size_.jsonl', 'a') as f:
                        f.write(json.dumps({'url': html['url'], 'target': target, 'img': img, 'html':html['html'] , 'source':query, 'id': data_id}, ensure_ascii=False) + '\n')
            data_id += 1

if __name__ == '__main__':
    main()
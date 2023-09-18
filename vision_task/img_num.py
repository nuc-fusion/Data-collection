import json, os, re, random
from tqdm import tqdm

htmls = []
files = os.listdir('/workspace/hanyu/ryl/phase2/')
for file in tqdm(files):
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

queryes = []
with open('img_num_query.txt', 'r') as f:
    for line in f:
        queryes.append(line.strip()[1:-1])

def main():
    data_id = 0
    global queryes
    for html in tqdm(htmls):
        html_ = html['html']
        url = html['url']
        matches = re.findall(r'img\[[A-Z][A-Z]\]', html_)
        oldpath = f"/workspace/hanyu/ryl/phase2/screenshot_mark/screenshot_{html['id']}.png"
        newpath = f"/workspace/hanyu/cyx/turbo_data/img_mark_useful/screenshot_{html['id']}.png"
        if os.path.exists(oldpath) == False:
            print('no img')
            continue
        if os.path.exists(newpath) == False:
            os.system(f"cp {oldpath} {newpath}")
        img = newpath
        if url not in cn_urls:
            query = random.choice(queryes)
            query = query.replace('screenshot', 'webpage')
        else:
            querys = []

            querys.append(f"请问这个网页包含多少张图像？")
            querys.append(f"这个网页中有多少个图片？")
            querys.append(f"请告诉我这个网页里有多少张图片。") 
            querys.append(f"这个网页中的图像数量是多少？")
            querys.append(f"请问一下，这个页面里有几张照片？")
            querys.append(f"这个网站上总共有多少张图？")
            querys.append(f"可以告诉我这个网页中图片的总数吗？")
            querys.append(f"这个网页中的图片总共有多少？")
            querys.append(f"请问一下，这个页面里图片的数量是多少？")
            querys.append(f"这个网页中图片的数量是多少？")
            query = random.choice(querys)
        with open('img_num_.jsonl', 'a') as f:
           f.write(json.dumps({'url': html['url'], 'target': len(matches), 'img': img, 'html': html_, 'source': query, 'id': data_id}, ensure_ascii=False) + '\n')
        data_id += 1
if __name__ == '__main__':
    main()
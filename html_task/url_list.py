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

queryes_en = [
    "How many hyperlinks are there in this webpage? Show me one of them.",
    "How many links can be found on this webpage? Display one of them.",
    "Can you tell me the total number of hyperlinks on this page? Provide an example.",
    "I'd like to know the count of hyperlinks within this webpage. Please exhibit one.",
    "Could you inform me about the quantity of links present on this web page? Illustrate one as an instance.",
    "Please reveal the number of hyperlinks contained in this webpage and show me a sample.",
    "What is the total count of hyperlinks on this webpage? Demonstrate one of them.",
    "Can you give me an idea of how many hyperlinks exist on this page? Share one as an example.",
    "Provide me with information about the quantity of hyperlinks available in this webpage. Display one of them.",
    "I'm curious about the number of hyperlinks on this webpage. Can you provide one as a reference?",
    "Tell me how many hyperlinks there are on this page and show me one for reference."
]

queryes_cn = [
    '这个网页上有多少超链接？展示其中一个。',
    '请告诉我这个网页上的超链接总数，展示其中一个作为例子。',
    '我想知道这个网页上有多少个超链接。请展示一个作为例子。',
    '能告诉我这个网页上链接的数量吗？展示一个作为示例。',
    '请透露这个网页中的超链接数量，并展示一个样本。',
    '这个网页上有多少个超链接？演示其中一个。',
    '你能告诉我这个页面上有多少个超链接吗？分享一个作为例子。',
    '给我提供有关这个网页中超链接数量的信息，展示一个作为示范。',
    '我对这个网页上的超链接数量很好奇。你能提供一个作为参考吗？',
    '告诉我这个页面上有多少个超链接，并展示一个作为参考。'
]

with open('web_cn.txt', 'r') as f:
    for line in f:
        url = line.strip()
        url = "http://" + url if not url.startswith("http") else url
        cn_urls.append(url)

def main():
    data_id = 0
    for html in tqdm(htmls):
        oldpath = f"/workspace/hanyu/ryl/phase2/screenshot_mark/screenshot_{html['id']}.png"
        newpath = f"/workspace/hanyu/cyx/turbo_data/img_mark_useful/screenshot_{html['id']}.png"
        if os.path.exists(oldpath) == False:
            print('no img')
            continue
        if os.path.exists(newpath) == False:
            os.system(f"cp {oldpath} {newpath}")
        img = newpath
        src_html = html['src_html']
        url = html['url']
        matches = re.findall(r'<a.*?href="(.*?)".*?>(.*?)</a>', src_html)
        hrefs = []
        texts = []
        for match in matches:
            href = match[0]
            text = match[1]
            text = re.sub(r'<.*?>', '', text)
            if href.startswith('http') and text != '':
                hrefs.append(href)
                texts.append(text)
        if len(hrefs) < 2:
            continue
        if url not in cn_urls:
            query = random.choice(queryes_en)
        else:
            query = random.choice(queryes_cn)
        random_index = random.randint(0, len(hrefs)-1)
        target = f"There are {len(matches)} hyperlinks in this webpage. Below is one of them: {texts[random_index]} {hrefs[random_index]}"
        with open('url_list.jsonl', 'a') as f:
           f.write(json.dumps({'url': html['url'], 'target': target, 'img': img, 'html': html['html'], 'source': query, 'id': data_id}, ensure_ascii=False) + '\n')
        data_id += 1
        
if __name__ == '__main__':
    main()
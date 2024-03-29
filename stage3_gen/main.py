import asyncio
import time
import re
import json
import os
from tqdm import tqdm

from lxml import html, etree

from llm import Agent

# ACT_TIME_OUT = 10000
# NAV_TIME_OUT = 25000

# NUM_PROCESS = 10

cn_urls = []

with open('web_cn.txt', 'r') as f:
    for line in f:
        url = line.strip()
        url = "http://" + url if not url.startswith("http") else url
        cn_urls.append(url)

async def run(html):
    agent = Agent()
    question, anwser = await agent.get_model_output(html)
    return question, anwser

htmls = []
files = os.listdir('/workspace/hanyu/ryl/phase2/')
for file in tqdm(files):
    if file.startswith('obj_') and file.endswith('.json'):
        with open('/workspace/hanyu/ryl/phase2/'+file, 'r') as f:
            try:
                htmls.append(json.load(f))
            except:
                continue
    

exist_data = []
if os.path.exists('stage3_cn.jsonl'):
    with open('stage3_cn.jsonl', 'r') as f:
        for line in f:
            line = json.loads(line)
            exist_data.append(line)
exist_urls = [data['url'] for data in exist_data]
data_num = len(exist_data)

async def main():
    global data_num
    data_id = data_num
    for html in tqdm(htmls):
        url = html['url']
        if url in exist_urls:
            continue
        if url not in cn_urls:
            continue
        try:
            question, anwser = await run(html['html'])
            img = f"/workspace/hanyu/ryl/phase2/screenshot_mark/screenshot_{html['id']}.png"
            html_ = html['html']
            with open('stage3_cn.jsonl', 'a') as f:
                f.write(json.dumps({'url': url, 'target': anwser, 'img': img, 'html': html_, 'source': question, 'id': data_id}) + '\n')
            data_id += 1
        except:
            continue
        
asyncio.run(main())

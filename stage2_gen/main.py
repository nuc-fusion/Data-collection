import asyncio
import time
import re
import json
import os
from tqdm import tqdm
from playwright.async_api import async_playwright
from lxml import html, etree
from verify import verify
from llm import Agent

# ACT_TIME_OUT = 10000
# NAV_TIME_OUT = 25000

# NUM_PROCESS = 10

async def run(html):
    agent = Agent()
    question, anwser, op, param = await agent.get_model_output(html, '')
    return question, anwser, op, param

htmls = []
files = os.listdir('/workspace/hanyu/ryl/phase2a/')
for file in tqdm(files[:2]):
    if file.startswith('obj_') and file.endswith('.json'):
        with open('/workspace/hanyu/ryl/phase2a/'+file, 'r') as f:
            try:
                htmls.append(json.load(f))
            except:
                continue
    

exist_data = []
with open('stage2_useful.jsonl', 'r') as f:
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
            print('exist')
            continue
        try:
            async with async_playwright() as p:
                question, answer_, op, param = await run(html['html'])
                if not await verify(p, url, op, param):
                    print('verify error')
                    continue
                oldpath = f"/workspace/hanyu/ryl/phase2a/screenshot_mark/screenshot_{html['id']}.png"
                newpath = f"/workspace/hanyu/cyx/turbo_data/img_mark_useful/screenshot_{html['id']}.png"
                if os.path.exists(oldpath) == False:
                    print('no img')
                    continue
                if os.path.exists(newpath) == False:
                    os.system(f"cp {oldpath} {newpath}")
                img = newpath
                html_ = html['html']
                with open('stage2_useful.jsonl', 'a') as f:
                    f.write(json.dumps({'url': url, 'target': answer_, 'img': img, 'html': html_, 'source': question, 'id': data_id}) + '\n')
                data_id += 1
        except Exception as e:
            print("------------------error------------------")
            print(e)
            continue
        
asyncio.run(main())

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

async def run(html,operation):
    agent = Agent()
    question, anwser, op, param = await agent.get_model_output(html, operation)
    return question, anwser, op, param

htmls = []
files = os.listdir('/workspace/hanyu/ryl/phase2b/')
for file in tqdm(files):
    if file.startswith('obj_') and file.endswith('.json'):
        with open('/workspace/hanyu/ryl/phase2b/'+file, 'r') as f:
            try:
                htmls.append(json.load(f))
            except:
                continue
    

exist_data = []
if os.path.exists('stage2_useful_new.jsonl'):
    with open('stage2_useful_new.jsonl', 'r') as f:
        for line in f:
            line = json.loads(line)
            exist_data.append(line)
            
exist_urls = [data['url'] for data in exist_data]
data_num = len(exist_data)

operation_list = ['Goto','Answer']

async def main():
    global data_num
    data_id = data_num
    op_id = 0
    for html in tqdm(htmls):
        op_id += 1
        url = html['url']
        if url in exist_urls:
            print('exist')
            continue
        try:
            async with async_playwright() as p:
                op_type = operation_list[op_id % len(operation_list)]
                question, answer_, op, param = await run(html['html'], op_type)
                op = op[1:-1]
                print(question, answer_, op, param)
                if not await verify(p, url, op, param):
                    print('verify error')
                    continue
                oldpath = f"/workspace/hanyu/ryl/phase2b/screenshot_mark/screenshot_{html['id']}.png"
                newpath = f"/workspace/hanyu/cyx/turbo_data/img_mark_usefulb/screenshot_{html['id']}.png"
                if os.path.exists(oldpath) == False:
                    print('no img')
                    continue
                if os.path.exists(newpath) == False:
                    os.system(f"cp {oldpath} {newpath}")
                img = newpath
                html_ = html['html']
                with open('stage2_useful_new.jsonl', 'a') as f:
                    f.write(json.dumps({'url': url, 'target': answer_, 'img': img, 'html': html_, 'source': question, 'id': data_id}) + '\n')
                data_id += 1
        except Exception as e:
            print("------------------error------------------")
            print(e)
            continue
        
asyncio.run(main())

# -*- coding:utf-8 -*-
LANGUAGE = 'en'
import os, json, sys, time, re, math, random, datetime, argparse, requests, csv
from typing import List, Dict, Any, Optional, Union, Tuple, Callable, Type, TypeVar
from html2text import html2text
if LANGUAGE == 'en':
    from prompt.en import *
elif LANGUAGE == 'cn':
    from prompt.cn import *
import tiktoken
from time import sleep
from tqdm import tqdm
import time
import asyncio

# os.environ["http_proxy"] = "http://127.0.0.1:9910"
# os.environ["https_proxy"] = "http://127.0.0.1:9910"

queries_en = [
"Give me the caption that describes how the page works using the website screenshot.",
"Show me the caption explaining what the page does from the website screenshot.",
"I need the caption that tells about the page's function using the website screenshot.",
"Share the caption that explains the purpose of the page using the website screenshot.",
"Provide the caption that describes the page's functionality using the website screenshot.",
"What's the caption explaining the operation of the page from the website screenshot?",
"I want the caption that breaks down the page's function using the website screenshot.",
"Let me see the caption that explains the page's functionality according to the website screenshot.",
"Share the caption that explains the page's functionality based on the website screenshot.",
"Show me the caption that explains the page's functionality based on the website screenshot.",
"I want to see the caption that explains the page's functionality from the website screenshot.",
]
queries_cn = [
    "请根据网页的截图给出对该网站用途的描述。",
    "根据网页截图描述该网站的功能。",
    "根据截图描述一下网站是干什么的。",
    "请根据截图解释一下这个网站的用途。",
    "根据截图，描述一下这个网站的功能。",
    "请根据截图描述一下这个网站的功能。",
    "请根据网页截图描述一下这个网站的功能。",
    "根据网页截图描述一下这个网站的功能。",
    "这个网站是干什么的？根据网页截图描述一下。",
    "请根据网页截图描述一下这个网站的功能。",
] 
enc = tiktoken.encoding_for_model('gpt-3.5-turbo')

CHAT_URL = "http://40.74.217.35:10014/api/v1/chat/completions"
TASK_PROCESSES = 2000

def chatgpt_call(prompt, history=None, system=None):
    t0 = time.time()
    message = []
    if system:
        message.append({
            "role": "system",
            "content": system
        })
    
    if history:
        for ix, chat in enumerate(history):
            message.append({
                "role": "user",
                "content": chat[0]
            })
            message.append({
                "role": "assistant",
                "content": chat[1]
            })
            
    
    message.append({
        "role": "user",
        "content": prompt
    })

    headers = {
        'Authorization': 'f5f042145daf5a1b55b16c3043551e12',
        'Content-Type': 'application/json'
    }
    
    for i in range(5):
        try:
            resp = requests.post(
                CHAT_URL, 
                json = {
                    "model": "gpt-3.5-turbo",
                    "messages": message,
                },
                headers=headers,
                timeout=100
            )
        except:
            sleep(1)
            continue
        
        if resp.status_code == 200:
            break
    else:
        print(resp.text)
        raise
    
    print(time.time() - t0)
        
    return resp.json()["choices"][0]["message"]["content"]

def getPurpose(html):
    webtext = html2text(html)
    x = enc.encode(purpose_query % webtext)
    truncated_query = enc.decode(x[:3500])
    purpose = chatgpt_call(truncated_query, history=[purpose_query % example_in, example_out], system=purpose_system)
    
    if purpose == no_purpose:
        return None
    
    return purpose

htmls = []
files = os.listdir('/workspace/hanyu/ryl/phase1/')
for file in files:
    if file.startswith('obj_'):
        with open('/workspace/hanyu/ryl/phase1/'+file, 'r') as f:
            htmls.append(json.load(f))

exist_data = []
with open('stage1.jsonl', 'r') as f:
    for line in f:
        line = json.loads(line)
        exist_data.append(line)
exist_urls = [data['url'] for data in exist_data]
data_num = len(exist_data)

data_id = data_num

for html in tqdm(htmls):
    url = html['url']
    if url in exist_urls:
        continue
    purpose_ = getPurpose(html['html'])
    img = html['img']
    html_ = html['html']
    source = random.choice(queries_en)
    with open('stage1.jsonl', 'a') as f:
        f.write(json.dumps({'url': url, 'purpose': purpose_, 'img': img, 'html': html_, 'source': source, 'id': data_id}) + '\n')
    data_id += 1
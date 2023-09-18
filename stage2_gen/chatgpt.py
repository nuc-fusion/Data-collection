import aiohttp
import asyncio
import requests
import json
import os

CHAT_URL = "http://40.74.217.35:10014/api/v1/chat/completions"
async def chatgpt_call(prompt, history=None, system=None):
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
            print('chatgpt call fail!')
            continue
        
        if resp.status_code == 200:
            break
    else:
        print(resp.text)
        raise
    
    # print(time.time() - t0)
        
    return resp.json()["choices"][0]["message"]["content"]

import aiohttp
import asyncio

async def chatgpt_call(history, prompt, system=None, lan='en'):
    message = []
    if system:
        message.append({
            "role": "system",
            "content": system
        })
    
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
    
    endpoint = "http://40.74.217.35:10014/api/v1/chat/completions"
    
    payload = {
            "model": "gpt-3.5-turbo",
            "messages": message,
            "temperature": 0.9
        }
    
    headers={
        "Authorization": "bd91cab0bac53e6e3bb091f308ab23e9",
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(endpoint, headers=headers, json=payload, timeout=50) as response:
            data = await response.json()
            # if resp.status_code != 200:
            #    return ''
            output = data["choices"][0]["message"]["content"]
            return output

if __name__ == '__main__':
    print(asyncio.run(chatgpt_call([], 'Hello')))
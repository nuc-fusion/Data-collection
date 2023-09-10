import os, json
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
useful_data = []

with open('stage1_valid.jsonl', 'r') as f:
    for line in tqdm(f):
        line = json.loads(line)
        url = line['url']
        for html in htmls:
            if url == html['url']:
                len_ = len(html['clickable_list'])
                if len_ < 3 or len_ < 60:
                    break
                else:
                    old_path = f"/workspace/hanyu/ryl/phase2/screenshot/screenshot_{html['id']}.png"
                    new_path = f"/workspace/hanyu/cyx/turbo_data/img/screenshot_{html['id']}.png"
                    os.system(f"cp {old_path} {new_path}")
                    line['image'] = new_path
                    useful_data.append(line)
                    break

with open('stage1_useful.jsonl', 'w') as f:
    for line in useful_data:
        f.write(json.dumps(line, ensure_ascii=False)+'\n')
                
lines = []

with open('stage1_useful.jsonl', 'r') as f:
    for line in tqdm(f):
       lines.append(json.loads(line))
import random      
for i in range(29563):
    lines.append(random.choice(lines))
with open('stage1_useful.jsonl', 'w') as f:
    for line in lines:
        f.write(json.dumps(line, ensure_ascii=False)+'\n')
        


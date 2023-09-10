import json, os
from tqdm import tqdm

data = []
with open('stage1_useful.jsonl', 'r') as f:
    for line in f:
        line = json.loads(line)
        data.append(line)
        
for d in tqdm(data):
    path = d['image']
    id_ = path.split('_')[-1].split('.')[0]
    old_path = f"/workspace/hanyu/ryl/phase2/screenshot_mark/screenshot_{id_}.png"
    new_path = f"/workspace/hanyu/cyx/turbo_data/img_mark/screenshot_{id_}.png"
    os.system(f"cp {old_path} {new_path}")
    d['image'] = new_path
    
with open('stage1_useful_mark.jsonl', 'w') as f:
    for line in data:
        f.write(json.dumps(line, ensure_ascii=False)+'\n')
        
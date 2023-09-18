import json, random

with open('stage3_cn.jsonl', 'r') as f:
    data = []
    for line in f:
        data_ = json.loads(line)
        target = data_['target']
        if "无" in target or "没有" in target or "不知道" in target:
            continue
        if data_['html'] == '':
            continue
        data.append(data_)
        
with open('elem_disc_cn.jsonl', 'a') as f:
    for d in data:
        f.write(json.dumps(d, ensure_ascii=False) + '\n')

for i in range(5199-len(data)):
    d = random.choice(data)
    d['id'] = i+len(data)
    with open('elem_disc_cn.jsonl', 'a') as f:
        f.write(json.dumps(d, ensure_ascii=False) + '\n')
    
# with open('elem_disc.jsonl', 'w') as f:
#     for d in data:
#         f.write(json.dumps(d, ensure_ascii=False) + '\n')
# useful_data = []

# for d in data:
#     usage = d['usage']
#     if 'none' in usage.lower():
#         continue
#     d['target'] = usage
#     d.pop('usage')
#     useful_data.append(d)
    
# with open('elem_disc.jsonl', 'w') as f:
#     for d in useful_data:
#         f.write(json.dumps(d, ensure_ascii=False) + '\n')
import os, json
from tqdm import tqdm
import re
import random
# htmls = []
# files = os.listdir('/workspace/hanyu/ryl/phase2/')
# for file in tqdm(files[:20000]):
#     if file.startswith('obj_') and file.endswith('.json'):
#         with open('/workspace/hanyu/ryl/phase2/'+file, 'r') as f:
#             try:
#                 html = json.load(f)
#                 htmls.append(html)
#             except:
#                 continue
# useful_data = []

# with open('stage2_new.jsonl', 'r') as f:
#     for line in tqdm(f):
#         line = json.loads(line)
#         url = line['url']
#         target = line['target']
#         # #匹配#Type# 字符串
#         # regex = re.compile(r'#(.*?)# (.*?)')
#         # mate = regex.findall(target)
#         # if len(mate) == 0:
#         #     useful_data.append(line)
#         # else:
#         #     if(len(mate) > 1):
#         #         print('error')
#         #         continue
#         #     elif len(mate[0][1]) != 2:
#         #         useful_data.append(line)
#         #     else:
#         #         print('error')
#         for html in htmls:
#             if url == html['url']:
#                     old_path = f"/workspace/hanyu/ryl/phase2/screenshot_mark/screenshot_{html['id']}.png"
#                     new_path = f"/workspace/hanyu/cyx/turbo_data/img_mark_1/screenshot_{html['id']}.png"
#                     os.system(f"cp {old_path} {new_path}")
#                     line['image'] = new_path
#                     if os.path.exists(new_path) == False:
#                         break
#                     useful_data.append(line)
#                     break

# with open('stage2_mark.jsonl', 'w') as f:
#     for line in useful_data:
#         f.write(json.dumps(line, ensure_ascii=False)+'\n')
all_data = []
with open('stage2_useful_new.jsonl', 'r') as f:
    for line in tqdm(f):
        line = json.loads(line)
        all_data.append(line)
# with open ('stage2_useful.jsonl', 'r') as f:
#     for line in tqdm(f):
#         line = json.loads(line)
#         all_data.append(line)
        
op_num_dir = {}
useful_data = []
ans_num = 0
goto_num = 0


for d in tqdm(all_data):
    if d['target'].count('#') == 2:
        op = d['target'].split('#')[1]
        if op not in op_num_dir:
            op_num_dir[op] = 1
        else:
            op_num_dir[op] += 1
        if op == 'Answer' and len(d['target']) > 20:
            useful_data.append(d)
            ans_num += 1
        if op == 'Goto' and "http" in d['target']:
            useful_data.append(d)
            goto_num += 1
            
print(ans_num)
print(goto_num)

# if len(useful_data) < 40000:
#     append_num = 40000 - len(useful_data)
#     append_data = random.sample(other_data, append_num)
#     useful_data.extend(append_data)

sample_data = random.sample(useful_data, 100)

with open('sample.jsonl', 'w') as f:
    for line in sample_data:
        f.write(json.dumps(line, ensure_ascii=False)+'\n')

# with open('stage2_all__.jsonl', 'w') as f:
#     for line in useful_data:
#         f.write(json.dumps(line, ensure_ascii=False)+'\n')
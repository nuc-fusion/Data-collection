import os, json
from tqdm import tqdm
import re

# htmls = []
# files = os.listdir('/workspace/hanyu/ryl/phase2/')
# for file in tqdm(files):
#     if file.startswith('obj_') and file.endswith('.json'):
#         with open('/workspace/hanyu/ryl/phase2/'+file, 'r') as f:
#             try:
#                 html = json.load(f)
#                 htmls.append(html)
#             except:
#                 continue
useful_data = []

with open('stage2.jsonl', 'r') as f:
    for line in tqdm(f):
        line = json.loads(line)
        url = line['url']
        target = line['target']
        #匹配#Type# 字符串
        regex = re.compile(r'#(.*?)# (.*?)')
        mate = regex.findall(target)
        if len(mate) == 0:
            useful_data.append(line)
        else:
            if(len(mate) > 1):
                print('error')
                continue
            elif len(mate[0][1]) != 2:
                useful_data.append(line)
            else:
                print('error')
        # for html in htmls:
        #     if url == html['url']:
        #             old_path = f"/workspace/hanyu/ryl/phase2/screenshot_mark/screenshot_{html['id']}.png"
        #             new_path = f"/workspace/hanyu/cyx/turbo_data/img_mark_1/screenshot_{html['id']}.png"
        #             os.system(f"cp {old_path} {new_path}")
        #             line['image'] = new_path
        #             line['target'] = line['opration']
        #             if os.path.exists(new_path) == False:
        #                 # line['source'] += line['html'][:-10]
        #                 break
        #             line.pop('opration')
        #             useful_data.append(line)
        #             break

with open('stage2_type.jsonl', 'w') as f:
    for line in useful_data:
        f.write(json.dumps(line, ensure_ascii=False)+'\n')
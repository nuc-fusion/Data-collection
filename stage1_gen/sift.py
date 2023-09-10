import json
import os
from tqdm import tqdm

def keyword_rule(target:str):
    keywords_cn = ['未知', '不确定', '不知道', '不清楚', '不了解', '不明白', '不懂', '根据文本','无法访问']
    keywords_en = ['unknown', 'not sure', 'not know', 'not clear', 'not understand', 'not understand', 'not understand', 'none', 'been blocked', 'Sorry']
    for keyword in keywords_cn + keywords_en:
        if keyword in target:
            return False
    return True

valid_data = []

# less_num = 0
# more_num = 0
# htmls = []
# files = os.listdir('/workspace/hanyu/ryl/phase2/')
# lens = []
# for file in tqdm(files):
#     if file.startswith('obj_') and file.endswith('.json'):
#         with open('/workspace/hanyu/ryl/phase2/'+file, 'r') as f:
#             try:
#                 html = json.load(f)
#                 htmls.append(html)
#                 lens.append(len(html['clickable_list']))
#             except:
#                 continue
# #绘制分布百分比图
# import matplotlib.pyplot as plt
# import numpy as np
# import matplotlib
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# matplotlib.rcParams['axes.unicode_minus'] = False
# lens = np.array(lens)
# lens = lens[lens<100]
# lens = lens[lens>0]
# plt.hist(lens, bins=100, density=True, cumulative=True, histtype='step', label='Empirical')
# plt.xlabel('Number of clickable elements')
# plt.ylabel('Cumulative probability')
# plt.title('Cumulative distribution of clickable elements')
# plt.legend()
# plt.savefig('clickable_elements.png')
with open('stage1.jsonl', 'r') as f:
    for line in f:
        line = json.loads(line)
        target = line['target']
        if 'image' not in line or 'html' not in line:
            continue
        if keyword_rule(target):
            html = line['html'].replace('\xa0', '')
            keywords_cn = ['无法访问', '故障', '错误']
            keywords_en = ['been blocked', 'sorry', 'network error', 'unauthorized', 'forbidden']
            if any(keyword in html for keyword in keywords_cn + keywords_en):
                continue
            line['html'] = html
            valid_data.append(line)

with open('stage1_valid.jsonl', 'w') as f:
    for line in valid_data:
        f.write(json.dumps(line, ensure_ascii=False) + '\n')
            
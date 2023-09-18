import json, random, re

all_data = []

# with open('back_color_.jsonl', 'r') as f:
#     cn_data = []
#     en_data = []
#     data = []
#     for line in f:
#         data = json.loads(line)
#         source = data['source']
#         if not re.search('[\u4e00-\u9fa5]', source):
#             en_data.append(data)
#         else:
#             cn_data.append(data)
#     cn_data = cn_data
#     en_data = random.sample(en_data, 5000-len(cn_data))
#     all_data.extend(cn_data)
#     all_data.extend(en_data)
#     with open('back_color.jsonl', 'w') as f:
#         for data in cn_data+en_data:
#             f.write(json.dumps(data, ensure_ascii=False) + '\n')
            
# with open('elem_size_.jsonl', 'r') as f:
#     cn_data = []
#     en_data = []
#     data = []
#     for line in f:
#         data = json.loads(line)
#         source = data['source']
#         if not re.search('[\u4e00-\u9fa5]', source):
#             en_data.append(data)
#         else:
#             cn_data.append(data)
#     cn_data = cn_data
#     en_data = random.sample(en_data, 5000-len(cn_data))
#     all_data.extend(cn_data)
#     all_data.extend(en_data)
#     with open('elem_size.jsonl', 'w') as f:
#         for data in cn_data+en_data:
#             f.write(json.dumps(data, ensure_ascii=False) + '\n')
    
with open('elem_pos_sample.jsonl', 'r') as f:
    cn_data = []
    en_data = []
    data = []
    for line in f:
        data = json.loads(line)
        source = data['source']
        target = data['target']
        if not re.search('[\u4e00-\u9fa5]', source):
            en_data.append(data)
        else:
            cn_data.append(data)
    cn_data = random.sample(cn_data, 5235)
    en_data = random.sample(en_data, 10655)
    all_data.extend(cn_data)
    all_data.extend(en_data)
    with open('elem_pos_new.jsonl', 'w') as f:
        for data in cn_data+en_data:
            f.write(json.dumps(data, ensure_ascii=False) + '\n')
    
# with open('img_num_.jsonl', 'r') as f:
#     cn_data = []
#     en_data = []
#     data = []
#     for line in f:
#         data = json.loads(line)
#         source = data['source']
#         target = data['target']
#         if not re.search('[\u4e00-\u9fa5]', source):
#             data['target'] = f"The number of images in the page is {target}."
#             en_data.append(data)
#         else:
#             data['target'] = f"页面中的图像数量是{target}。"
#             cn_data.append(data)
#     cn_data = random.sample(cn_data, 5240)
#     en_data = random.sample(en_data, 6452)
#     all_data.extend(cn_data)
#     all_data.extend(en_data)
#     with open('img_num.jsonl', 'w') as f:
#         for data in cn_data+en_data:
#             f.write(json.dumps(data, ensure_ascii=False) + '\n')
    
# with open('all_data_.jsonl', 'w') as f:
#     for data in all_data:
#         f.write(json.dumps(data, ensure_ascii=False) + '\n')
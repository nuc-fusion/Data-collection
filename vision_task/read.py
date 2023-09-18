import json
import os

data = []

with open('elem_pos_sample.jsonl', 'r') as f:
    for line in f:
        data_ = json.loads(line)
        data.append(data_)
        
def read_data(id_):
    data_ = data[id_]
    print(data_)
    img = data_['img']
    #拷贝到sample.png
    os.system(f"cp {img} sample.jpg")
    
read_data(0)
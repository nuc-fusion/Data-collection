import json, os, re, random
from tqdm import tqdm
import PIL.Image as Image

htmls = []
files = os.listdir('/workspace/hanyu/ryl/phase2a/')
for file in tqdm(files[:2000]):
    if file.startswith('obj_') and file.endswith('.json'):
        with open('/workspace/hanyu/ryl/phase2a/'+file, 'r') as f:
            try:
                html = json.load(f)
                htmls.append(html)
            except:
                continue

colors = [('red', 'green'), ('blue', 'orange'), ('yellow', 'purple'), ('pink', 'gray'), ('black', 'white')]

def main():
    data_id = 0
    for html in tqdm(htmls):
        random_pair = random.choice(colors)
        oldpath = f"/workspace/hanyu/ryl/phase2a/screenshot_mark/screenshot_{html['id']}.png"
        newpath = f"/workspace/hanyu/cyx/turbo_data/img_mark_useful/screenshot_{html['id']}.png"
        elems = []
        for elem in html['info'].values():
            if 'label' in elem and elem['rect'] is not None:
                elems.append(elem)
        if elems == []:
            continue
        elem = random.choice(elems)
        query = f"Which color is the color of the center of elem {elem['label']} more similar to, {random_pair[0]} or {random_pair[1]}?"
        if os.path.exists(oldpath) == False:
                    print('no img')
                    continue
        if os.path.exists(newpath) == False:
                    os.system(f"cp {oldpath} {newpath}")
        img = Image.open(newpath)
        width, height = img.size
        x_per = elem['rect']['x'] * width / 1080
        y_per = elem['rect']['y'] * height / 720
        try:
            background_color = img.getpixel((int(x_per), int(y_per)))
        except:
            continue
        pair_0 = None
        pair_1 = None
        if random_pair[0] == 'red':
            pair_0 = (255, 0, 0)
            pair_1 = (0, 255, 0)
        elif random_pair[0] == 'blue':
            pair_0 = (0, 0, 255)
            pair_1 = (255, 165, 0)
        elif random_pair[0] == 'yellow':
            pair_0 = (255, 255, 0)
            pair_1 = (128, 0, 128)
        elif random_pair[0] == 'pink':
            pair_0 = (255, 192, 203)
            pair_1 = (128, 128, 128)
        elif random_pair[0] == 'black':
            pair_0 = (0, 0, 0)
            pair_1 = (255, 255, 255)
        color_dis0 = (background_color[0] - pair_0[0])**2 + (background_color[1] - pair_0[1])**2 + (background_color[2] - pair_0[2])**2
        color_dis1 = (background_color[0] - pair_1[0])**2 + (background_color[1] - pair_1[1])**2 + (background_color[2] - pair_1[2])**2
        
        target = None
        if color_dis0 < color_dis1:
            target = f"The color of the center of elem {elem['label']} is more similar to {random_pair[0]}."
        elif color_dis0 > color_dis1:
            target = f"The color of the center of elem {elem['label']} is more similar to {random_pair[1]}."
        else:
            target = f"The color of the center of elem {elem['label']} is equally similar to {random_pair[0]} and {random_pair[1]}."
        
        if target is not None:
            with open('elem_color.jsonl', 'a') as f:
                f.write(json.dumps({'url': html['url'], 'target': target, 'img': newpath, 'html':html['html'] , 'source':query, 'id': data_id}, ensure_ascii=False) + '\n')
        
        data_id += 1

if __name__ == '__main__':
    main()
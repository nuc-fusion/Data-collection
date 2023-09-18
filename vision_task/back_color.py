import json, os, re, random
from tqdm import tqdm
import PIL.Image as Image

cn_urls = []

with open('web_cn.txt', 'r') as f:
    for line in f:
        url = line.strip()
        url = "http://" + url if not url.startswith("http") else url
        cn_urls.append(url)


no_img = 0
htmls = []
files = os.listdir('/workspace/hanyu/ryl/phase2/')
for file in tqdm(files[:20000]):
    if file.startswith('obj_') and file.endswith('.json'):
        with open('/workspace/hanyu/ryl/phase2/'+file, 'r') as f:
            try:
                html = json.load(f)
                htmls.append(html)
            except:
                continue

colors = [('red', 'green'), ('blue', 'orange'), ('yellow', 'purple'), ('pink', 'gray'), ('black', 'white')]

def main():
    data_id = 0
    for html in tqdm(htmls):
        url = html['url']
        oldpath = f"/workspace/hanyu/ryl/phase2/screenshot_mark/screenshot_{html['id']}.png"
        newpath = f"/workspace/hanyu/cyx/turbo_data/img_mark_useful/screenshot_{html['id']}.png"
        if os.path.exists(oldpath) == False:
                    print('no img')
                    continue
        if os.path.exists(newpath) == False:
                    os.system(f"cp {oldpath} {newpath}")
        try:
            img = Image.open(newpath)
            width, height = img.size
            all_color = []
            for x, y in [(0, 0), (width-1, 0), (0, height-1), (width-1, height-1)]:
                all_color.append(img.getpixel((x, y)))
            background_color = max(all_color, key=all_color.count)
        except:
            continue
        min_color_dis = 10000000
        color_rgb = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 165, 0), (255, 255, 0), (128, 0, 128), (255, 192, 203), (128, 128, 128), (0, 0, 0), (255, 255, 255)]
        for rgb in color_rgb:
            color_dis = (background_color[0] - rgb[0])**2 + (background_color[1] - rgb[1])**2 + (background_color[2] - rgb[2])**2
            if color_dis < min_color_dis:
                min_color_dis = color_dis
                min_color = rgb
        if min_color_dis > 1000:
            continue
        if min_color == (255, 0, 0):
            random_pair = ('red', 'green')
        elif min_color == (0, 255, 0):
            random_pair = ('red', 'green')
        elif min_color == (0, 0, 255):
            random_pair = ('blue', 'orange')
        elif min_color == (255, 165, 0):
            random_pair = ('blue', 'orange')
        elif min_color == (255, 255, 0):
            random_pair = ('yellow', 'purple')
        elif min_color == (128, 0, 128):
            random_pair = ('yellow', 'purple')
        elif min_color == (255, 192, 203):
            random_pair = ('pink', 'gray')
        elif min_color == (128, 128, 128):
            random_pair = ('pink', 'gray')
        elif min_color == (0, 0, 0):
            random_pair = ('black', 'white')
        elif min_color == (255, 255, 255):
            random_pair = ('black', 'white')
        querys = []
        if url not in cn_urls:
            querys.append(f"Which color is the background color of the page more similar to, {random_pair[0]} or {random_pair[1]}?")
            querys.append(f"Which color, {random_pair[0]} or {random_pair[1]}, is the background color of the page more similar to?")
            querys.append(f"Is the background color of the page closer in resemblance to {random_pair[0]} or {random_pair[1]}?")
            querys.append(f"Which color is the background color of the page resembling more, {random_pair[0]} or {random_pair[1]}?")
            querys.append(f"Is the background color of the page more alike {random_pair[0]} or {random_pair[1]}?")
            querys.append(f"Which color, {random_pair[0]} or {random_pair[1]}, does the background color of the page resemble more?")
            querys.append(f"Is the background color of the page closer in shade to {random_pair[0]} or {random_pair[1]}?")
            querys.append(f"Which color is the background color of the page more akin to, {random_pair[0]} or {random_pair[1]}?")
            querys.append(f"Does the background color of the page have a stronger resemblance to {random_pair[0]} or {random_pair[1]}?")
            querys.append(f"Which color, {random_pair[0]} or {random_pair[1]}, is the background color of the page more akin to in similarity?")
            query = random.choice(querys)        
        else:
            if random_pair[0] == 'red':
                cn_pair = ('红色', '绿色')
            elif random_pair[0] == 'blue':
                cn_pair = ('蓝色', '橙色')
            elif random_pair[0] == 'yellow':
                cn_pair = ('黄色', '紫色')
            elif random_pair[0] == 'pink':
                cn_pair = ('粉色', '灰色')
            elif random_pair[0] == 'black':
                cn_pair = ('黑色', '白色')
            querys.append(f"页面的背景色更类似于{cn_pair[0]}还是{cn_pair[1]}？")
            querys.append(f"在颜色方面，页面的背景色更接近{cn_pair[0]}还是{cn_pair[1]}？")
            querys.append(f"页面的背景色更像{cn_pair[0]}还是{cn_pair[1]}？")
            querys.append(f"页面的背景颜色更类似于{cn_pair[0]}还是{cn_pair[1]}？")
            querys.append(f"页面的背景色更趋近于{cn_pair[0]}还是{cn_pair[1]}？")
            querys.append(f"页面的背景色更接近于{cn_pair[0]}还是{cn_pair[1]}？")
            querys.append(f"页面的背景色更类似于{cn_pair[0]}还是{cn_pair[1]}的色调？")
            querys.append(f"在颜色相似性方面，页面的背景色更接近{cn_pair[0]}还是{cn_pair[1]}？")
            querys.append(f"页面的背景色更类似于{cn_pair[0]}还是{cn_pair[1]}的色彩？")
            querys.append(f"在色彩方面，页面的背景色更趋近于{cn_pair[0]}还是{cn_pair[1]}？")
            querys.append(f"页面的背景色更类似于{cn_pair[0]}还是{cn_pair[1]}的色彩？")
            query = random.choice(querys)
        width, height = img.size
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
        if url not in cn_urls:
            if color_dis0 < color_dis1:
                target = f"The background color of the page is more similar to {random_pair[0]}."
            elif color_dis0 > color_dis1:
                target = f"The background color of the page is more similar to {random_pair[1]}."
            else:
                target = f"The background color of the page is equally similar to {random_pair[0]} and {random_pair[1]}."
        else:
            if color_dis0 < color_dis1:
                target = f"页面的背景色更接近{cn_pair[0]}。"
            elif color_dis0 > color_dis1:
                target = f"页面的背景色更接近{cn_pair[1]}。"
            else:
                target = f"页面的背景色更接近{cn_pair[0]}和{cn_pair[1]}。"
        
        if target is not None:
            with open('back_color_.jsonl', 'a') as f:
                f.write(json.dumps({'url': html['url'], 'target': target, 'img': newpath, 'html':html['html'] , 'source':query, 'id': data_id}, ensure_ascii=False) + '\n')
        
        data_id += 1

if __name__ == '__main__':
    main()
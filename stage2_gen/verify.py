from tree_tool import TreeTool
from playwright.async_api import async_playwright

ACT_TIME_OUT = 10000
NAV_TIME_OUT = 25000

def get_xpath(tree, tag):
    xpath = tree.get_xpath_by_label(tag)
    
    if xpath is not None:
        return xpath

    print('==== ERROR ====')
    print('Cannot find the tag with given ID')
    return None

async def get_rect(page, xpath_dict):
    rect_list = {}

    for _, xp in xpath_dict.items():
        act_xp = xp.replace("xpath", "xpath=", 1).replace("//*[", "/*[")
        elem_rect = None
        
        try:
            elem = await page.query_selector(act_xp)
            bounding = await elem.bounding_box()
            
            if bounding is not None:
                elem_rect = {
                    "x": bounding['x'],
                    "y": bounding['y'],
                    "width": bounding['width'],
                    "height": bounding['height'],
                    "top": bounding['y'],
                    "bottom": bounding['y'] + bounding['height'],
                    "left": bounding['x'],
                    "right": bounding['x'] + bounding['width'],
                }
        except:
            pass
        
        rect_list[xp] = elem_rect
    
    return rect_list
 
async def verify(p, url: str, act_type: str, param: str):
    browser = await p.chromium.launch(headless=True)
    context = await browser.new_context(viewport={"width": 1080, "height": 720})
    # await context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    page = await context.new_page()

    await page.goto(url)
    
    await page.wait_for_load_state()

    # get page content
    ctx = await page.content()
    tree = TreeTool(ctx)
   
    tree.set_window({
            "top": 0,
            "left": 0,
            "bottom": 720,
            "right": 1080,
            "x": 1080,
            "y": 720
        })
        
    xpath_dict = tree.get_xpath_dict()
        
    rect_list = await get_rect(page, xpath_dict)
    tree.set_rect_list(rect_list)
        
        
    packet = tree.parse_tree()
    page_html, id_list, labels = packet['html'], packet['clickable_list'], packet['clickable_labels']
    
    try:
        if act_type == 'Exit':
            pass
        if act_type == "Scroll up":
            n = param[0]
            delta_y = int(-720 * n) # height * n pages
            await page.mouse.wheel(0, delta_y)
        if act_type == "Scroll down":
            n = param[0]
            delta_y = int(720 * n) # height * n pages
            await page.mouse.wheel(0, delta_y)
        elif act_type == "Click":
            tag = param[0]
            xpath = get_xpath(tree, tag)
            await page.click(xpath, timeout=ACT_TIME_OUT)
        elif act_type == "Goto":
            url = param
            await page.goto(url, timeout=ACT_TIME_OUT)
        elif act_type == "Go backward":
            await page.go_back(timeout=ACT_TIME_OUT)
        elif act_type == "Go forward":
            await page.go_forward(timeout=ACT_TIME_OUT)
        elif act_type == "Hover":
            tag = param[0]
            xpath = get_xpath(tree, tag)
            await page.hover(xpath, timeout=ACT_TIME_OUT)
        elif act_type == "Type":
            tag, text = param[0], param[1]
            xpath = get_xpath(tree, tag)
            await page.fill(xpath, text, timeout=ACT_TIME_OUT)
        elif act_type == "Answer":
            text = param[0]
            print("The Answer is: " + text)
        elif act_type == "Login":
            input("Encounter Login Page, Please Login and Press Enter to Continue")
        elif act_type == "Verify":
            input("Encounter Verification Page, Please Login and Press Enter to Continue")
        else:
            pass
        
        await context.close()
        await browser.close()
        return True
    except Exception as e:
        print(e)
        await context.close()
        await browser.close()
        return False
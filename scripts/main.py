import pyautogui, time, utils, judge, config
import pygetwindow as gw

def save_target_image(x, y):
    """
    Pass in x and y and save the target needed to recognized picture
    @params:
    x: int, left position
    y: int, top position
    @return:
    im_path: str, saved image path
    """
    im = pyautogui.screenshot(region=(int(x - 95), int(y - 10), 145, 55))
    im_path = utils.complete_path("images/cache1.png")
    im.save(im_path)
    time.sleep(0.1)
    return im_path

def save_target_attr_image(x, y):
    """
    Pass in shenghai.left and shenghai.top and save the target's attr needed to recognized picture
    @params:
    x: int, shenghai left position
    y: int, shenghai top position
    @return:
    im_path: str, saved image path
    """
    im = pyautogui.screenshot(region=(int(x + 1055), int(y + 315), 40, 38))
    im_path = utils.complete_path("images/cache2.png")
    im.save(im_path)
    time.sleep(0.1)
    return im_path

def save_target_COST_image(x, y):
    """
    Pass in shenghai.left and shenghai.top and save the target's COST needed to recognized picture
    @params
    x: int, shenghai left position
    y: int, shenghai top position
    @return
    im_path: str, saved image path
    """
    im = pyautogui.screenshot(region=(int(x + 1374), int(y + 135), 110, 30))
    im_path = utils.complete_path("images/cache3.png")
    im.save(im_path)
    time.sleep(0.1)
    return im_path

def save_target_handle_image(x, y):
    """
    Pass in shenghai.left and shenghai.top and save the target's handle message needed to recognized picture
    @params
    x: int, shenghai left position
    y: int, shenghai top position
    @return
    im_path: str, saved image path
    """
    im = pyautogui.screenshot(region=(int(x + 1330), int(y + 220), 160, 40))
    im_path = utils.complete_path("images/cache4.png")
    im.save(im_path)
    time.sleep(0.1)
    return im_path

def check_is_bottom(x, y):
    """
    Check to see if you have scrolled to the end
    @params:
    x: int, shenghai left position
    y: int, shenghai top position
    @return:
    is_bottom: bool, if is bottom
    """
    im = pyautogui.screenshot(region=(int(x + 968), int(y + 735), 18, 20))
    im_path = utils.complete_path('images/cache.png')
    im.save(im_path)
    mathced_degree = judge.get_matched_degree(im_path, utils.complete_path('images/is_bottom.png'))
    if mathced_degree == 1.0:
        return True
    else:
        return False

def check_is_locked(im_path):
    """
    check target if is locked
    @params
    im_path: str, target image path
    @return
    is_locked: bool, if is locked
    """
    matched_degree_locked, matched_degree_not_locked = judge.get_matched_degree(im_path, utils.complete_path('images/is_locked.png')), judge.get_matched_degree(im_path, utils.complete_path('images/is_not_locked.png'))
    # print(f'DEBUG: locked---{matched_degree_locked} not-locked---{matched_degree_not_locked}')
    return matched_degree_locked < matched_degree_not_locked

def check_is_discarded(im_path):
    """
    check target if is discarded
    @params
    im_path: str, target image path
    @return
    is_discarded, bool, if is discarded
    """
    matched_degree_discarded, matched_degree_not_discarded = judge.get_matched_degree(im_path, utils.complete_path('images/is_discarded.png')), judge.get_matched_degree(im_path, utils.complete_path('images/is_not_discarded.png'))
    # print(f'DEBUG: discarded---{matched_degree_discarded} not-discarded---{matched_degree_not_discarded}')
    return matched_degree_discarded < matched_degree_not_discarded

def start_selection(target_handle_path, suit_name, attr_name, COST):
    """
    Filters the current target based on the contents of config
    @params
    target_handle_path: str, target handle message image path
    suit_name: str, suit name
    attr_name: str, attr name
    COST: str, COST
    @return
    None
    """
    if suit_name in config.config.keys():
        if attr_name in config.config[suit_name][COST]:
            if not config.ignore_handled:
                pyautogui.press('c')
            elif not check_is_locked(target_handle_path):
                pyautogui.press('c')
            else:
                print('DEBUG: 已锁定')
        else:
            if not config.ignore_handled:
                pyautogui.press('z')
            elif not check_is_discarded(target_handle_path):
                pyautogui.press('z')
            else:
                print('DEBUG: 已弃置')
    time.sleep(0.5)

def get_suit_name(im_path):
    """
    Get target suit name
    @params
    im_path: str, target image path
    @return
    suit_name: str, target image suit name
    """
    mathced_degree_arr = [(judge.get_matched_degree(im_path, utils.complete_path(f'images/suit_{i}_{j}.png')), suit_name) for (i, j), suit_name in judge.suit.items()]
    suit_name = min(mathced_degree_arr)[1]
    return suit_name

def get_attr_name(im_path):
    """
    Get target attr name
    @params
    im_path: str, target attr image path
    @return
    attr_name: str, target image attr name
    """
    mathced_degree_arr = [((judge.get_matched_degree(im_path, utils.complete_path(f'images/attr_{i}.png')), attr_name)) for i, attr_name in judge.attr.items()]
    attr_name = min(mathced_degree_arr)[1]
    return attr_name

def get_COST(im_path):
    """
    Get target COST
    @params
    im_path: str, target COST image path
    @return
    COST: str, target COST
    """
    mathced_degree_arr = [((judge.get_matched_degree(im_path, utils.complete_path(f'images/COST_{i}.png'))), f'COST {i}') for i in (1, 3, 4)]
    COST = min(mathced_degree_arr)[1]
    return COST

def create_scroller():
    """
    create a scroller to scroll the screen
    """
    i = 0
    def scroll():
        nonlocal i
        if i == 0:
            for _ in range(6):
                pyautogui.scroll(-157)
                time.sleep(0.4)
        else:
            for _ in range(6):
                pyautogui.scroll(-156)
                time.sleep(0.4)
        i = (i + 1) % 3
    return scroll


# Focus on Wuthering Waves
try:
    window = gw.getWindowsWithTitle("鸣潮")[0]
    if window:
        window.activate()
        time.sleep(1)
    else:
        print('未找到鸣潮')
except IndexError:
    print('未找到鸣潮')

# start project
try:
    # Anchor the position through the icon
    shenghai_image_path = utils.complete_path('images\\shenghai.png')
    shenghai_position = pyautogui.locateOnScreen(shenghai_image_path, confidence=0.6)

    if shenghai_position:
        scroller = create_scroller()
        while check_is_bottom(shenghai_position.left, shenghai_position.top):
            # the first target position
            x, y = shenghai_position.left + 220, shenghai_position.top + 180

            # every row has six items
            for _ in range(6):
                pyautogui.click(x, y)
                time.sleep(0.2)

                # if ignore handled target
                target_handle_path = save_target_handle_image(shenghai_position.left, shenghai_position.top)
                
                if config.ignore_handled and check_is_locked(target_handle_path):
                    print('DEBUG: 已锁定')
                    # change left position
                    x += 138
                    continue
                elif config.ignore_handled and check_is_discarded(target_handle_path):
                    print('DEBUG: 已弃置')
                    # change left position
                    x += 138
                    continue

                target_path = save_target_image(x, y)
                target_attr_path = save_target_attr_image(shenghai_position.left, shenghai_position.top)
                target_COST_path = save_target_COST_image(shenghai_position.left, shenghai_position.top)

                suit_name = get_suit_name(target_path)
                attr_name = get_attr_name(target_attr_path)
                COST = get_COST(target_COST_path)

                print(f'DEBUG: {suit_name} {attr_name} {COST}')

                # start selection
                start_selection(target_handle_path, suit_name, attr_name, COST)

                # change left position
                x += 138
            
            # refresh left position
            x = shenghai_position.left + 220

            # scroll the screen
            scroller()
except pyautogui.ImageNotFoundException:
    print('未打开背包声骸界面')
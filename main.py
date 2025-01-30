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
    im = pyautogui.screenshot(region=(int(x - 95), int(y - 120), 145, 175))
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

try:
    window = gw.getWindowsWithTitle("鸣潮")[0]
    if window:
        window.activate()
    else:
        print('未找到鸣潮')
except IndexError:
    print('未找到鸣潮')

time.sleep(1)


try:
    shenghai_image_path = utils.complete_path('images\\shenghai.png')
    shenghai_position = pyautogui.locateOnScreen(shenghai_image_path, confidence=0.6)

    if shenghai_position:
        while check_is_bottom(shenghai_position.left, shenghai_position.top):
            x, y = shenghai_position.left + 220, shenghai_position.top + 180
            for _ in range(6):
                pyautogui.click(x, y)

                im_path = save_target_image(x, y)
                mathced_degree_arr = [(judge.get_matched_degree(im_path, utils.complete_path(f'images/suit_{i}_{j}.png')), suit_name) for (i, j), suit_name in judge.suit.items()]
                suit_name = min(mathced_degree_arr)[1]
                
                im_path = save_target_attr_image(shenghai_position.left, shenghai_position.top)
                mathced_degree_arr = [((judge.get_matched_degree(im_path, utils.complete_path(f'images/attr_{i}.png')), attr_name)) for i, attr_name in judge.attr.items()]
                attr_name = min(mathced_degree_arr)[1]

                print(f'DEBUG: {suit_name} {attr_name}')

                if suit_name in config.config.keys():
                    if attr_name in config.config[suit_name]:
                        matched_degree = judge.get_matched_degree(utils.complete_path('images/cache1.png'), utils.complete_path('images/lock.png'))
                        print('DEBUG:' + str(matched_degree))
                        if matched_degree > 0.1:
                            pyautogui.press('c')
                        else:
                            print('DEBUG: 已锁定')
                    else:
                        matched_degree = judge.get_matched_degree(utils.complete_path('images/cache1.png'), utils.complete_path('images/discard.png'))
                        print('DEBUG:' + str(matched_degree))
                        if matched_degree > 0.06:
                            pyautogui.press('z')
                        else:
                            print('DEBUG: 已弃置')
                time.sleep(3.2)

                x += 138
            x = shenghai_position.left + 220
            y += 170

            for _ in range(6):
                pyautogui.scroll(-157)
                time.sleep(0.4)
except pyautogui.ImageNotFoundException:
    print('未打开背包声骸界面')
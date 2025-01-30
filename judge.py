import cv2, utils

suit = {
    (1, 1): "凝夜冰霜",
    (1, 2): "熔山裂谷",
    (1, 3): "彻空冥雷",
    (1, 4): "啸谷长风",
    (1, 5): "浮星祛暗",
    (1, 6): "沉日劫明",
    (1, 7): "隐世回光",
    (1, 8): "轻云出月",
    (1, 9): "不绝余音",
    (2, 1): "凌冽决断之心",
    (2, 2): "此间永驻之光",
    (2, 3): "幽夜隐匿之帷",
    (2, 4): "高天共奏之曲",
    (2, 5): "无惧浪涛之勇"
}

attr = {
    1: "生命值百分比",
    2: "攻击力百分比",
    3: "防御力百分比",
    4: "暴击率",
    5: "暴击伤害",
    6: "治疗效果加成",
    7: "冷凝伤害加成",
    8: "热熔伤害加成",
    9: "导电伤害加成",
    10: "气动伤害加成",
    11: "衍射伤害加成",
    12: "湮灭伤害加成",
    13: "共鸣效率"
}

def get_matched_degree(path1, path2):
    """
    A single template matches a single target
    @params
    path1: str, target's file path
    path2: str, template's file path
    @return
    matched_degree: float, template's matched degree in target, the closer it's to 1.0, the better the match
    """
    # 加载目标图片
    target = cv2.imread(path1, cv2.IMREAD_COLOR)
    template = cv2.imread(path2, cv2.IMREAD_COLOR)

    if template is None:
        print(f"错误：无法加载目标图片")
        return False

    # 使用模板匹配
    result = cv2.matchTemplate(target, template, cv2.TM_SQDIFF_NORMED)

    return cv2.minMaxLoc(result)[0] # 返回min_val

# arr = [(get_matched_degree(utils.complete_path("images/test.png"), utils.complete_path(f"images/attr_{i}.png")), attr_name) for i, attr_name in attr.items()]
# print(min(arr)[1])
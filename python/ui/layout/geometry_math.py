# [FUNCTION]: 提供 UI 元素的物理几何计算，确保窗口绝对对齐。

def calculate_base_width(text_width: float) -> float:
    """[核心灵感]: 根据数字宽度动态计算悬浮底座长度，比例锁定为 1.1"""
    return text_width * 1.1

def get_bottom_center_pos(screen_w, screen_h, win_w, win_h, offset_y=60):
    """
    [物理主权]: 计算窗口在屏幕底部居中的物理坐标。
    offset_y: 距离屏幕最底部的距离，60px 刚好可以越过标准任务栏。
    """
    x = (screen_w - win_w) // 2
    y = screen_h - win_h - offset_y
    return x, y

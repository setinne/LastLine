# [FUNCTION]: 绘制 1.1x 悬浮底座，并实时计算数字的几何中心。
from ui.layout.geometry_math import calculate_base_width

def draw_suspension_dock(canvas, text_id, color="#0078D7"):
    """在数字正下方绘制 1.1 倍宽的进度条底座"""
    x1, y1, x2, y2 = canvas.bbox(text_id)
    text_w = x2 - x1
    base_w = calculate_base_width(text_w)
    
    padding = (base_w - text_w) / 2
    
    # 绘制底座矩形
    return canvas.create_rectangle(
        x1 - padding, y2 + 5, x2 + padding, y2 + 10,
        fill=color, outline=""
    )
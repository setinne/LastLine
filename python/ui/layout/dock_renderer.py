# 删掉之前的 from ui.layout.geometry_math ...
# 改用相对引用
from .geometry_math import calculate_base_width

def draw_suspension_dock(canvas, text_id, color="#0078D7"):
    coords = canvas.bbox(text_id)
    if not coords: return
    x1, y1, x2, y2 = coords
    
    text_w = x2 - x1
    # 这里的调用必须匹配 geometry_math 里的函数名
    base_w = calculate_base_width(text_w)
    
    padding = (base_w - text_w) / 2
    return canvas.create_rectangle(
        x1 - padding, y2 + 5, x2 + padding, y2 + 10,
        fill=color, outline=""
    )
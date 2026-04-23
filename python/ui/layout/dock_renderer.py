from .geometry_math import calculate_base_width

def update_suspension_dock(canvas, text_id, color="#0078D7"):
    """
    [渲染主权]: 先删后画，确保 1.1x 蓝条永远精准对齐中文字符。
    """
    # 这一步非常重要，否则每 30 秒就会多画一条线，最后变粗变乱
    canvas.delete("dock_line") 
    
    coords = canvas.bbox(text_id)
    if not coords: return
    
    text_w = coords[2] - coords[0]
    base_w = calculate_base_width(text_w)
    padding = (base_w - text_w) / 2
    
    # 重新绘制并打上 Tag
    canvas.create_rectangle(
        coords[0] - padding, coords[3] + 8,
        coords[2] + padding, coords[3] + 13,
        fill=color, outline="",
        tags="dock_line"
    )
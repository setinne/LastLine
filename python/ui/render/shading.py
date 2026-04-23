# [FUNCTION]: 为数字 Canvas 增加中线阴影，模拟实体翻页钟的折痕感与背景渐变。

def apply_flip_crease(canvas, canvas_id, color="#000000"):
    """在 Canvas 对象中心横切一条 1px 的半透明阴影线"""
    coords = canvas.bbox(canvas_id)
    mid_y = (coords[1] + coords[3]) / 2
    canvas.create_line(
        coords[0], mid_y, coords[2], mid_y,
        fill=color, stipple="gray50", width=1
    )
# [FUNCTION]: 借鉴 FlipIt，在数字 Canvas 上叠加渐变阴影，制造立体翻页质感。

def apply_center_shadow(canvas, x, y, w, h):
    """在数字正中央绘制一条极细的透明渐变带，模拟折痕"""
    # 使用 Alpha 混合的矩形覆盖
    canvas.create_rectangle(
        x, y + h//2 - 1, x + w, y + h//2 + 1,
        fill="#000000", stipple="gray25", outline=""
    )
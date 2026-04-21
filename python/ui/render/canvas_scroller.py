# [FUNCTION]: 实现“滚动胶片”动效，通过 Canvas 坐标偏移消除数字切换时的视觉闪烁。

def scroll_digit(canvas, old_id, new_id, height, steps=12):
    """
    [灵感项]: 建立 (0, -H) 到 (0, 0) 的平滑位移逻辑
    old_id: 正在离开的数字对象
    new_id: 正在进入的数字对象
    """
    dy = height / steps
    for i in range(steps):
        canvas.move(old_id, 0, dy)
        canvas.move(new_id, 0, dy)
        canvas.update() # 强制 UI 线程刷新，确保平滑感
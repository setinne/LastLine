# [FUNCTION]: 实现“余量寄语消融”算法，动态裁切 Canvas 文本以配合进度条增长。

def get_motto_clip_box(progress_ratio: float, total_width: int):
    """计算寄语的剩余可见区域（Crop Box）"""
    # 随着进度（0.0 -> 1.0）增加，起始坐标向右推移
    start_x = int(total_width * progress_ratio)
    return (start_x, 0, total_width, 50) # 返回裁剪后的矩形区域
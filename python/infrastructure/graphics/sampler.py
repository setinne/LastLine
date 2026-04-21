# [FUNCTION]: 自动采样桌面壁纸色彩，利用对比度算法避开极端色，实现环境感知融入。
from PIL import ImageGrab, ImageStat

def get_wallpaper_accent():
    """采样屏幕特定区域（挂件预设位置）的色彩，返回互补或高对比色"""
    # 截取一小块屏幕背景进行分析
    img = ImageGrab.grab(bbox=(100, 100, 200, 200))
    stat = ImageStat.Stat(img)
    avg_color = stat.mean # 获取平均 RGB
    
    # 简单的亮度计算：(R*299 + G*587 + B*114) / 1000
    brightness = (avg_color[0]*299 + avg_color[1]*587 + avg_color[2]*114) / 1000
    return "#FFFFFF" if brightness < 128 else "#333333"
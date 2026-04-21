import ctypes

def apply_high_dpi_awareness():
    """[行政指令]: 强制 Windows 进程进入 Per-Monitor V2 模式，确保物理像素 1:1 对齐"""
    try:
        # 针对 Win10 1703 及以后版本（华为笔记本主流系统）
        ctypes.windll.shcore.SetProcessDpiAwareness(2) 
    except Exception:
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except Exception:
            ctypes.windll.user32.SetProcessDPIAware()

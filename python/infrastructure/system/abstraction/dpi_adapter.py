# [FUNCTION]: 强制开启进程级 DPI 感知，通过底层 Win32 API 抹除高分屏导致的坐标偏移。
import ctypes

def apply_high_dpi_awareness():
    """对接 Rust 侧物理位置接管前的环境预处理，兼容 XP 到 Win11"""
    try:
        # 尝试 Win10 1703+ 的 Per-Monitor V2
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except (AttributeError, Exception):
        try:
            # 尝试 Win7/XP 的基础适配
            ctypes.windll.user32.SetProcessDPIAware()
        except:
            # 即使全部失败也不崩溃，确保后续影子自愈逻辑继续执行
            pass
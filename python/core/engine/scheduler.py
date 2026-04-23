# [FUNCTION]: 核心调度器：执行“500ms 强制归位”逻辑，确保在异形屏下坐标绝对精准。
import time

def schedule_position_lock(root_window, rust_api):
    """
    系统启动或分辨率改变后，延迟 500ms 重新执行物理像素校准。
    """
    def task():
        time.sleep(0.5) # 500ms 黄金等待期，等待桌面环境稳定
        # 调用 Rust 编译的原生接口强制归位
        hwnd = root_window.winfo_id()
        rust_api.force_wallpaper_stick(hwnd)
        
    import threading
    threading.Thread(target=task, daemon=True).start()
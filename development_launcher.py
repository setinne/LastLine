import sys
import ctypes
import tkinter as tk
from pathlib import Path
from datetime import datetime

# 1. 路径主权
BASE_DIR = Path(__file__).parent
sys.path.insert(0, str(BASE_DIR / "python"))

# 2. 物理劫持加载
try:
    rust_lib = ctypes.cdll.LoadLibrary(str(BASE_DIR / "python" / "lastline_core.pyd"))
    print("[SUCCESS]: Rust 物理劫持引擎已就绪。")
except Exception as e:
    print(f"[WARNING]: 加载 Rust 模块失败: {e}")
    rust_lib = None

# 3. 原子组件导入
from infrastructure.system.abstraction.dpi_adapter import apply_high_dpi_awareness
from infrastructure.time.engine import get_countdown_physics
from infrastructure.time.formatter import format_countdown_string
import ui.layout.geometry_math as geo
from ui.window.base_canvas import BaseCanvas
from ui.layout.dock_renderer import update_suspension_dock

class LastLineFinalPreview:
    def __init__(self):
        apply_high_dpi_awareness()
        self.root = tk.Tk()
        self.target_time = datetime(2026, 6, 7, 9, 0)
        
        # 1. 窗口样式主权
        win_w, win_h = 600, 200
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        pos_x, pos_y = geo.get_bottom_center_pos(screen_w, screen_h, win_w, win_h)
        
        self.root.geometry(f"{win_w}x{win_h}+{pos_x}+{pos_y}")
        self.root.overrideredirect(True)      # 无边框
        self.root.attributes("-topmost", False) # 绝不置顶
        self.root.configure(bg="black")
        self.root.attributes("-transparentcolor", "black")
        
        # 2. 绕过任务栏 (真正的独立插件感)
        self.root.attributes("-toolwindow", True) 

        self.canvas = BaseCanvas(self.root, bg="black")
        self.text_id = self.canvas.create_text(
            300, 100, text="STARTING...", fill="#FFFFFF", font=("Segoe UI Semibold", 42)
        )
        
        # 3. 初始渲染
        self.refresh_heartbeat()
        self.root.update()

        # 4. 关键：另起炉灶的“底层压制”
        # 我们手动调用 Windows API 将窗口置于底部，而不进入 WorkerW
        self.set_to_bottom()

        self.root.bind("<Escape>", lambda e: self.root.destroy())

    def set_to_bottom(self):
        """[底层主权]: 强行将窗口推至所有普通窗口下方"""
        HWND_BOTTOM = 1
        SWP_NOMOVE = 0x0002
        SWP_NOSIZE = 0x0001
        SWP_NOACTIVATE = 0x0010
        
        hwnd = self.root.winfo_id()
        ctypes.windll.user32.SetWindowPos(
            hwnd, HWND_BOTTOM, 0, 0, 0, 0, 
            SWP_NOMOVE | SWP_NOSIZE | SWP_NOACTIVATE
        )
        print(f"[ACTION]: 窗口已执行底层压制 (HWND_BOTTOM)")

    def refresh_heartbeat(self):
        """[心跳引擎]: 恢复常规更新逻辑"""
        try:
            d, h, m = get_countdown_physics(self.target_time)
            display_txt = format_countdown_string(d, h, m)
            
            # 恢复简单的更新，因为不再受 WorkerW 缓存干扰
            self.canvas.itemconfig(self.text_id, text=display_txt)
            update_suspension_dock(self.canvas, self.text_id)
            
            # 每 10 秒尝试刷新一次底层状态，防止被其他窗口意外挤上来
            self.set_to_bottom()
            
            print(f"[HEARTBEAT]: {display_txt}")
        except Exception as e:
            print(f"[ERROR]: {e}")
            
        self.root.after(10000, self.refresh_heartbeat)
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = LastLineFinalPreview()
    app.run()

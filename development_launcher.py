import sys
from pathlib import Path
import ctypes
import tkinter as tk
from datetime import datetime

# [路径主权]: 确保能识别 python/ 目录下的原子模块
BASE_DIR = Path(__file__).parent
sys.path.insert(0, str(BASE_DIR / "python"))

# 加载 Rust 肌肉
try:
    rust_lib = ctypes.cdll.LoadLibrary(str(BASE_DIR / "python" / "lastline_core.pyd"))
    print("[SUCCESS]: Rust 物理劫持引擎已就绪。")
except Exception as e:
    print(f"[WARNING]: 加载 Rust 模块失败: {e}")
    rust_lib = None

# 原子组件导入 - 匹配你 GitHub 的最新命名
from infrastructure.system.abstraction.dpi_adapter import apply_high_dpi_awareness
import ui.layout.geometry_math as geo
from ui.window.base_canvas import BaseCanvas
from ui.layout.dock_renderer import draw_suspension_dock

# 时间引擎导入 - 必须匹配 engine.py 里的函数名
from infrastructure.time.engine import get_countdown_physics
from infrastructure.time.formatter import format_countdown_string

class LastLineFinalPreview:
    def __init__(self):
        apply_high_dpi_awareness()
        self.root = tk.Tk()
        
        # 2026 高考目标：6月7日 9:00
        self.target_time = datetime(2026, 6, 7, 9, 0)
        
        # 窗口基础配置
        win_w, win_h = 500, 180
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        pos_x, pos_y = geo.get_bottom_center_pos(screen_w, screen_h, win_w, win_h)
        
        self.root.geometry(f"{win_w}x{win_h}+{pos_x}+{pos_y}")
        self.root.overrideredirect(True)
        self.root.configure(bg="black")
        self.root.attributes("-transparentcolor", "black")
        
        # 画布与初始文本
        self.canvas = BaseCanvas(self.root, bg="black")
        self.text_id = self.canvas.create_text(
            250, 80, text="", fill="#FFFFFF", font=("Segoe UI Semibold", 42)
        )
        
        # 刷新并执行 Rust 劫持
        self.root.update()
        if rust_lib:
            rust_lib.embed_to_desktop(self.root.winfo_id())
            print(f"[ACTION]: 句柄嵌入桌面，开始心跳自刷新。")

        # 启动核心心跳
        self.refresh_loop()
        self.root.bind("<Escape>", lambda e: self.root.destroy())

    def refresh_loop(self):
        """[心跳引擎]: 驱动时间与底座的动态对齐"""
        # 1. 物理计算
        d, h, m = get_countdown_physics(self.target_time)
        # 2. 格式化翻译
        txt = format_countdown_string(d, h, m)
        
        # 3. 更新 UI
        self.canvas.itemconfig(self.text_id, text=txt)
        draw_suspension_dock(self.canvas, self.text_id)
        
        # 4. 每 30 秒跳动一次 (30000ms)
        self.root.after(30000, self.refresh_loop)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = LastLineFinalPreview()
    app.run()

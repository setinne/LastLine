import sys
import tkinter as tk
from pathlib import Path

# 强制注入路径
BASE_DIR = Path(__file__).parent
sys.path.insert(0, str(BASE_DIR / "python"))

from infrastructure.system.abstraction.dpi_adapter import apply_high_dpi_awareness
import ui.layout.geometry_math as geo
from ui.window.base_canvas import BaseCanvas
from ui.layout.dock_renderer import draw_suspension_dock

class LastLineFinalPreview:
    def __init__(self):
        # 1. 开启 DPI 感知
        apply_high_dpi_awareness()
        
        self.root = tk.Tk()
        
        # 2. 设定窗口尺寸（适当加宽以容纳 1.1x 底座）
        win_w, win_h = 500, 180
        
        # 3. 核心修正：获取实时的屏幕物理宽高
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        
        # 4. 计算置底居中位置
        pos_x, pos_y = geo.get_bottom_center_pos(screen_w, screen_h, win_w, win_h)
        
        # 5. 强制应用几何主权
        self.root.geometry(f"{win_w}x{win_h}+{pos_x}+{pos_y}")
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.configure(bg="black")

        self.canvas = BaseCanvas(self.root, bg="black")
        
        # 渲染数字：确保在 Canvas 内部也居中
        self.text_id = self.canvas.create_text(
            250, 80, text="47 DAYS", fill="#FFFFFF", font=("Segoe UI Semibold", 52)
        )
        
        # 绘制 1.1x 悬浮底座
        draw_suspension_dock(self.canvas, self.text_id, color="#0078D7")

        self.root.bind("<Escape>", lambda e: self.root.destroy())

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    print(f"[SYSTEM]: GPL v3.0 协议已激活。正在执行物理对齐...")
    app = LastLineFinalPreview()
    app.run()

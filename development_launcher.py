# [FUNCTION]: 开发态集成启动器（修正版）：实现屏幕物理对齐，强制居中置底。
import sys
import tkinter as tk
from pathlib import Path

BASE_DIR = Path(__file__).parent
sys.path.append(str(BASE_DIR / "python"))

try:
    from infrastructure.system.abstraction.dpi_adapter import apply_high_dpi_awareness
    from ui.layout.geometry_math import get_bottom_center_pos, calculate_base_width
    from ui.window.base_canvas import BaseCanvas
    from ui.layout.dock_renderer import draw_suspension_dock
    from ui.render.flip_effect import apply_center_shadow
except ImportError as e:
    print(f"[ERROR]: 模块缺失，请检查路径。{e}")
    sys.exit()

class LastLineCorrectedPreview:
    def __init__(self):
        apply_high_dpi_awareness()
        self.root = tk.Tk()
        
        # 定义窗口尺寸
        win_w, win_h = 500, 200
        
        # --- 核心修正：获取屏幕真实的物理尺寸 ---
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        
        # 计算居中置底坐标
        pos_x, pos_y = get_bottom_center_pos(screen_w, screen_h, win_w, win_h)
        
        # 强制应用坐标
        self.root.geometry(f"{win_w}x{win_h}+{pos_x}+{pos_y}")
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.configure(bg="black")

        self.canvas = BaseCanvas(self.root, bg="black")
        
        # 渲染
        self.text_id = self.canvas.create_text(
            200, 60, text="47 DAYS", fill="#FFFFFF", font=("Segoe UI Semibold", 48)
        )
        draw_suspension_dock(self.canvas, self.text_id, color="#0078D7")
        
        x1, y1, x2, y2 = self.canvas.bbox(self.text_id)
        apply_center_shadow(self.canvas, x1, y1, x2-x1, y2-y1)

        self.root.bind("<Escape>", lambda e: self.root.destroy())

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    print("[SYSTEM]: 正在执行物理对齐校准...")
    app = LastLineCorrectedPreview()
    app.run()
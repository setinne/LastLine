# [FUNCTION]: 螃蟹工程最高指挥部：整合 DPI、Rust 驱动、Canvas 渲染与影子自愈逻辑。
import tkinter as tk
from infrastructure.system.abstraction.dpi_adapter import apply_high_dpi_awareness
from core.engine.scheduler import schedule_position_lock
from ui.window.base_canvas import BaseCanvas
from ui.layout.dock_renderer import draw_suspension_dock

class LastLineEngine:
    def __init__(self):
        # 1. 物理环境初始化
        apply_high_dpi_awareness()
        
        self.root = tk.Tk()
        self.root.overrideredirect(True) # 此时配合 Rust 侧的 WorkerW 劫持
        
        # 2. 建立渲染画布
        self.canvas = BaseCanvas(self.root, bg="black")
        
        # 3. 绘制灵感项：1.1倍底座
        self.text_id = self.canvas.create_text(
            100, 50, text="Gaokao 2026", fill="white", font=("Segoe UI", 40)
        )
        draw_suspension_dock(self.canvas, self.text_id)

    def run(self, rust_lib):
        # 4. 执行 500ms 强制归位锁定
        schedule_position_lock(self.root, rust_lib)
        
        print("LastLine Monolith is now Breathing...")
        self.root.mainloop()
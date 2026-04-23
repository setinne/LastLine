import sys
import ctypes
import tkinter as tk
from pathlib import Path
from datetime import datetime

# ==========================================
# 1. 路径主权：将 python/ 目录注入搜索路径
# ==========================================
BASE_DIR = Path(__file__).parent
sys.path.insert(0, str(BASE_DIR / "python"))

# ==========================================
# 2. 物理劫持：加载 Rust 编译的底层模块
# ==========================================
try:
    # 这里的 .pyd 实际上是 rename 后的 .dll
    rust_lib = ctypes.cdll.LoadLibrary(str(BASE_DIR / "python" / "lastline_core.pyd"))
    print("[SUCCESS]: Rust 物理劫持引擎已就绪。")
except Exception as e:
    print(f"[WARNING]: 加载 Rust 模块失败: {e}")
    rust_lib = None

# ==========================================
# 3. 原子组件导入：完全对齐 GitHub 仓库路径
# ==========================================
# 系统基础设施
from infrastructure.system.abstraction.dpi_adapter import apply_high_dpi_awareness
# 时间引擎 (极致原子化：计算与翻译分离)
from infrastructure.time.engine import get_countdown_physics
from infrastructure.time.formatter import format_countdown_string
# UI 渲染层
import ui.layout.geometry_math as geo
from ui.window.base_canvas import BaseCanvas
from ui.layout.dock_renderer import update_suspension_dock

class LastLineFinalPreview:
    def __init__(self):
        # 初始化系统感知
        apply_high_dpi_awareness()
        self.root = tk.Tk()
        
        # --- 设定目标：2026 高考 (6月7日 09:00) ---
        self.target_time = datetime(2026, 6, 7, 9, 0)
        
        # --- 窗口物理参数 ---
        win_w, win_h = 500, 180
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        pos_x, pos_y = geo.get_bottom_center_pos(screen_w, screen_h, win_w, win_h)
        
        # --- 窗口样式主权 ---
        self.root.geometry(f"{win_w}x{win_h}+{pos_x}+{pos_y}")
        self.root.overrideredirect(True)       # 无边框
        self.root.configure(bg="black")       # 背景涂黑以配合透明
        self.root.attributes("-transparentcolor", "black") # 黑色消融
        
        # --- 画布挂载 ---
        self.canvas = BaseCanvas(self.root, bg="black")
        
        # 预创建文本对象 (Segoe UI 字号 42，适合中文字符串)
        self.text_id = self.canvas.create_text(
            250, 80, text="", fill="#FFFFFF", font=("Segoe UI Semibold", 42)
        )
        
        # --- 执行底层劫持 ---
        self.root.update() # 必须先刷新以生成句柄
        hwnd = self.root.winfo_id()
        
        if rust_lib:
            # 执行 Rust 里的 embed_to_desktop 函数实现置底
            rust_lib.embed_to_desktop(hwnd)
            print(f"[ACTION]: 句柄 {hwnd} 已执行物理压制，强行置底。")

        # --- 启动动态心跳 ---
        self.refresh_heartbeat()
        
        # 退出快捷键
        self.root.bind("<Escape>", lambda e: self.root.destroy())

    def refresh_heartbeat(self):
        """
        [心跳逻辑]: 每 30 秒执行一次原子闭环
        1. 物理计算 -> 2. 格式翻译 -> 3. UI 映射 -> 4. 渲染底座
        """
        # 1. 物理计算 (获取日、时、分)
        d, h, m = get_countdown_physics(self.target_time)
        
        # 2. 格式化翻译 (转为中文字符串)
        display_txt = format_countdown_string(d, h, m)
        
        # 3. 更新画布上的文字内容
        self.canvas.itemconfig(self.text_id, text=display_txt)
        
        # 4. 驱动渲染器更新 1.1x 动态底座
        update_suspension_dock(self.canvas, self.text_id)
        
        # 递归调用实现心跳循环 (30,000 毫秒)
        self.root.after(30000, self.refresh_heartbeat)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = LastLineFinalPreview()
    app.run()

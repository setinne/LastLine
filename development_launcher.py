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
        
        # 窗口物理参数
        win_w, win_h = 600, 200 # 稍微放大一点，防止中文溢出
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        pos_x, pos_y = geo.get_bottom_center_pos(screen_w, screen_h, win_w, win_h)
        
        self.root.geometry(f"{win_w}x{win_h}+{pos_x}+{pos_y}")
        self.root.overrideredirect(True)
        self.root.configure(bg="black")
        self.root.attributes("-transparentcolor", "black")
        
        # 4. 关键：先建立画布
        self.canvas = BaseCanvas(self.root, bg="black")
        
        # 5. 关键：预填充内容，防止 BBox 塌陷
        # 先用 LOADING 占位，确保窗口在劫持前不是空的
        self.text_id = self.canvas.create_text(
            300, 100, text="INITIALIZING...", fill="#FFFFFF", font=("Segoe UI Semibold", 42)
        )
        
        # 6. 核心动作：先执行一次真实的数据刷新
        self.refresh_heartbeat()
        
        # 7. 渲染锁定：强迫窗口立刻绘制所有像素
        self.root.update_idletasks()
        self.root.update()
        
        # 8. 最后一步：物理劫持
        # 只有当窗口里已经有东西了，才把它塞进桌面
        if rust_lib:
            rust_lib.embed_to_desktop(self.root.winfo_id())
            print(f"[ACTION]: 句柄 {self.root.winfo_id()} 已嵌入桌面。")

        self.root.bind("<Escape>", lambda e: self.root.destroy())

    def refresh_heartbeat(self):
        """
        [渲染主权]: 强迫 Windows 对嵌入桌面的窗口进行物理重绘
        """
        try:
            # 1. 物理计算
            d, h, m = get_countdown_physics(self.target_time)
            display_txt = format_countdown_string(d, h, m)
            
            # 2. 检查是否有变化
            current_txt = self.canvas.itemcget(self.text_id, "text")
            if display_txt != current_txt:
                # 更新文字内容
                self.canvas.itemconfig(self.text_id, text=display_txt)
                # 更新底座宽度
                update_suspension_dock(self.canvas, self.text_id)
                
                # --- 关键：三段式物理唤醒 ---
                # A. 强迫 Tkinter 更新内部渲染队列
                self.root.update_idletasks()
                
                # B. 强迫窗口重绘（防止在 WorkerW 层被冻结）
                self.canvas.update() 
                
                # C. (可选) 稍微移动 1 像素再移回来，触发系统级感知
                # 这种“位移抖动”是处理置底窗口不刷新的玄学但有效的方案
                curr_geo = self.root.geometry()
                # 提取当前的 x, y 并微调
                print(f"[HEARTBEAT]: 物理刷新成功 -> {display_txt}")
            
        except Exception as e:
            print(f"[ERROR]: 心跳同步失败: {e}")
        
        # 将频率提高到 10 秒，确保分钟切换的视觉延迟降到最低
        self.root.after(10000, self.refresh_heartbeat)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = LastLineFinalPreview()
    app.run()

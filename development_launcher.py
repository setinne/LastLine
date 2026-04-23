import sys
from pathlib import Path

# [路径主权]: 确保 Python 能看到 python/ 目录下的所有原子模块
BASE_DIR = Path(__file__).parent
sys.path.insert(0, str(BASE_DIR / "python"))

# 现在才能安全导入
from infrastructure.time.engine import calculate_remaining_time
from infrastructure.time.formatter import format_countdown_string

# 加载 Rust 肌肉
try:
    rust_lib = ctypes.cdll.LoadLibrary(str(BASE_DIR / "python" / "lastline_core.pyd"))
    print("[SUCCESS]: Rust 物理劫持引擎已就绪。")
except Exception as e:
    print(f"[WARNING]: 加载 Rust 模块失败: {e}")
    rust_lib = None

# 引入原子组件
from infrastructure.system.abstraction.dpi_adapter import apply_high_dpi_awareness
import ui.layout.geometry_math as geo
from ui.window.base_canvas import BaseCanvas
from ui.layout.dock_renderer import draw_suspension_dock

class LastLineFinalPreview:
    def __init__(self):
        # ... DPI, root, geometry, Rust 劫持 ...
        self.target = datetime(2026, 6, 7, 9, 0) # 高考开考
        self.render_heartbeat()

    def render_heartbeat(self):
        # 1. 物理计算
        d, h, m = calculate_remaining_time(self.target)
        # 2. 格式化
        txt = format_countdown_string(d, h, m)
        
        # 3. UI 映射
        self.canvas.itemconfig(self.text_id, text=txt)
        update_suspension_dock(self.canvas, self.text_id)
        
        # 30秒一次心跳，省电且精准
        self.root.after(30000, self.render_heartbeat)
    def __init__(self):
        # 1. 优先级最高：开启 DPI 感知
        apply_high_dpi_awareness()
        
        # 2. 核心：必须先创建 root 实例！
        self.root = tk.Tk()
        
        # 3. 设定窗口尺寸与位置
        win_w, win_h = 500, 180
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        pos_x, pos_y = geo.get_bottom_center_pos(screen_w, screen_h, win_w, win_h)
        
        # 4. 配置窗口属性
        self.root.geometry(f"{win_w}x{win_h}+{pos_x}+{pos_y}")
        self.root.overrideredirect(True)      # 去掉边框
        # ... 之前的配置 ...
        self.root.configure(bg="black")
        
        # [视觉主权]: 将黑色定义为透明色
        # 这样窗口中所有黑色的部分都会变成透明，直接露出后面的芙宁娜壁纸
        self.root.attributes("-transparentcolor", "black")
        
        # 5. 挂载画布 (注意 Canvas 的背景也要是黑色，才能被透明化)
        self.canvas = BaseCanvas(self.root, bg="black")
        
        # ... 剩下的渲染与 Rust 劫持逻辑保持不变 ...
        self.text_id = self.canvas.create_text(
            250, 80, text="47 DAYS", fill="#FFFFFF", font=("Segoe UI Semibold", 56)
        )
        draw_suspension_dock(self.canvas, self.text_id, color="#0078D7")
        
        # 6. 核心：刷新窗口并执行 Rust 劫持
        self.root.update() 
        hwnd = self.root.winfo_id()
        
        if rust_lib:
            # 执行 Rust 里的 embed_to_desktop
            # 注意：如果 Rust 里的函数名没变，这里直接调用
            rust_lib.embed_to_desktop(hwnd)
            print(f"[ACTION]: 句柄 {hwnd} 已沉入桌面底层。")

        self.root.bind("<Escape>", lambda e: self.root.destroy())

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = LastLineFinalPreview()
    app.run()

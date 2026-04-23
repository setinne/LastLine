import tkinter as tk

class BaseCanvas(tk.Canvas):
    def __init__(self, master, **kwargs):
        # [逻辑主权]: 确保默认没有边框，但允许通过 kwargs 覆盖
        kwargs.setdefault('highlightthickness', 0)
        kwargs.setdefault('borderwidth', 0)
        
        super().__init__(master, **kwargs)
        self.pack(fill=tk.BOTH, expand=True)

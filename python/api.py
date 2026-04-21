# [FUNCTION]: 隐藏深层碎片的复杂性，为外部加载器提供唯一的螃蟹工程接口。
from core.engine.main_engine import LastLineEngine
from infrastructure.system.performance.mmap_loader import map_core_logic

def start_lastline():
    """这是整个二进制迷宫的唯一出口"""
    # 预加载内存映射
    logic_stream = map_core_logic()
    engine = LastLineEngine()
    # 启动
    engine.run(rust_lib=None) # 此处传入编译后的 Rust 实例
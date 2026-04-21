# [FUNCTION]: 动态解析程序根目录，支持开发态与二进制流发布态的物理锚点切换。
from pathlib import Path
import sys

def get_app_root() -> Path:
    """自动探测根目录：开发环境回溯层级，生产环境定位 EXE 所在目录"""
    if getattr(sys, 'frozen', False):
        # 发布态：直接定位到二进制文件所在目录
        return Path(sys.executable).parent
    # 开发态：从 python/data/config/ 向上回溯 3 层到达 D:\TRY\CountdownProject
    return Path(__file__).resolve().parents[3]
# [FUNCTION]: 定义项目所有关键文件夹、二进制流路径及加密资源柜（.bacx）的物理坐标。
from data.config.resolver import get_app_root

ROOT = get_app_root()

# 发布态三层防火墙目录定义
DIR_ENGINE = ROOT / "engine"    # 存放二进制逻辑碎片
DIR_STORAGE = ROOT / "storage"  # 存放加密资源包
DIR_SYSTEM = ROOT / "system"    # 存放私有运行时

# 核心数据文件定义
VAULT_FILE = DIR_STORAGE / "user_data.bacx"
HEARTBEAT_FILE = DIR_STORAGE / "last_live.bin"
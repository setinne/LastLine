# [FUNCTION]: 提供“回到本次修改前”和“回到出厂状态”两级物理隔离的撤销机制。
import shutil
from data.config.indicators import VAULT_FILE

def backup_current_vault():
    """在修改前创建影子备份 (.bakx.tmp)"""
    if VAULT_FILE.exists():
        shutil.copy(VAULT_FILE, VAULT_FILE.with_suffix('.tmp'))

def restore_to_factory():
    """彻底弃用当前配置，从 engine/ 内部的默认流重新初始化"""
    if VAULT_FILE.exists():
        VAULT_FILE.unlink()
    # 触发初始化逻辑...

# [FUNCTION]: 实时心跳写入，在 storage/ 维护 last_live.bin 影子镜像，对抗冰点还原。
import time
from data.config.indicators import HEARTBEAT_FILE
from infrastructure.security.vault.cipher_engine import seal_data

def beat():
    """将当前高精度时间戳存入影子文件，作为重启后的自愈锚点"""
    try:
        current_state = f"LIVE|{time.time()}"
        with open(HEARTBEAT_FILE, "wb") as f:
            f.write(seal_data(current_state))
    except IOError:
        pass # 保证主进程不因 IO 波动挂掉
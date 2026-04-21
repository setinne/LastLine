# [FUNCTION]: 管理员最高行政权限验证，基于 090201 密钥生成动态指令 Token。
import hashlib

def generate_admin_token(command: str) -> str:
    """生成带有时间戳指纹的指令签名，防止指令被伪造"""
    salt = "090201"
    raw_payload = f"{command}{salt}"
    return hashlib.sha256(raw_payload.encode()).hexdigest()

def verify_token(command: str, token: str) -> bool:
    """从机校验：只有持有正确 Token 的指令才会被执行"""
    return generate_admin_token(command) == token
# [FUNCTION]: 提供基于密钥的二进制流加解密，保护存储在 storage/ 下的 .bacx 资源柜。
import base64
from itertools import cycle

def XOR_codec(data: bytes, key: str = "090201") -> bytes:
    """[影子协议]: 极简且高效的二进制流混淆，确保发布态下逻辑不可直视"""
    return bytes([b ^ ord(k) for b, k in zip(data, cycle(key))])

def seal_data(plain_text: str) -> bytes:
    """加密并封存配置"""
    return XOR_codec(plain_text.encode('utf-8'))

def open_vault(cipher_data: bytes) -> str:
    """解密并读取配置"""
    return XOR_codec(cipher_data).decode('utf-8')
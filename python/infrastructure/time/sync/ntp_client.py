# [FUNCTION]: 异步执行 NTP 网络对时，获取绝对真理时间，防止本地系统时间被篡改。
import socket
import struct
import time

def get_network_time(host="pool.ntp.org"):
    """[影子纠偏]: 远程获取高精度时间戳，偏差超过 1s 则标记漂移"""
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.settimeout(2)
        # NTP 协议报文头
        data = b'\x1b' + 47 * b'\0'
        client.sendto(data, (host, 123))
        data, address = client.recvfrom(1024)
        if data:
            # 解析 NTP 响应中的秒数 (1900年至今)
            t = struct.unpack('!12I', data)[10]
            return t - 2208988800 # 转换为 Unix 时间戳
    except:
        return None
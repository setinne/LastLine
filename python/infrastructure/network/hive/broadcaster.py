# [FUNCTION]: 局域网意志同频广播，向所有从属节点发送同步指令。
import socket

def send_hive_command(msg: str):
    """UDP 广播：一机修改，全网同频"""
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    # 模拟发送：[COMMAND]|[TOKEN]
    token = generate_admin_token(msg)
    client.sendto(f"{msg}|{token}".encode(), ('<broadcast>', 9021))
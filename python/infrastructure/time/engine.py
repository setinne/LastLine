from datetime import datetime

def get_countdown_physics(target_dt: datetime):
    """[原子计算]: 仅输出物理残余数值"""
    now = datetime.now()
    delta = target_dt - now
    
    if delta.total_seconds() <= 0:
        return 0, 0, 0
        
    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    
    return days, hours, minutes
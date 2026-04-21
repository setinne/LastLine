def calculate_base_width(text_width):
    return float(text_width) * 1.1

def get_bottom_center_pos(screen_w, screen_h, win_w, win_h, offset_y=70):
    x = (int(screen_w) - int(win_w)) // 2
    y = int(screen_h) - int(win_h) - int(offset_y)
    return x, y
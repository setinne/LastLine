// [FUNCTION]: 实现 WorkerW 桌面句柄劫持与 Windows 物理坐标锁定，对抗 Win+D 最小化。
// [PERFORMANCE]: HIGH_PRIORITY (将编译为 engine/ 目录下的核心二进制流)

use std::ptr;
use winapi::shared::windef::HWND;
use winapi::um::winuser::{FindWindowW, SetWindowPos, HWND_BOTTOM};

#[no_mangle]
pub extern "C" fn force_wallpaper_stick(hwnd: isize) {
    /* 逻辑：通过 Win32 API 寻找 WorkerW 句柄。
        发布态将以二进制形式潜伏，不留源码痕迹。
    */
    unsafe {
        let h_hwnd = hwnd as HWND;
        // 强行将窗口位置设为 HWND_BOTTOM 且取消 TopMost，实现嵌入壁纸
        SetWindowPos(h_hwnd, HWND_BOTTOM, 0, 0, 0, 0, 0x0013); 
    }
}
use windows::Win32::Foundation::{HWND};
use windows::Win32::UI::WindowsAndMessaging::{
    FindWindowW, SetParent, GetWindowLongPtrW, SetWindowLongPtrW, 
    SetWindowPos, GWL_EXSTYLE, WS_EX_TOOLWINDOW, HWND_BOTTOM, SWP_NOMOVE, SWP_NOSIZE
};

#[no_mangle]
pub extern "C" fn embed_to_desktop(target_hwnd: isize) {
    let hwnd = HWND(target_hwnd);
    
    unsafe {
        let progman = FindWindowW(windows::core::w!("Progman"), None);
        
        if progman.0 != 0 {
            // 1. 建立父子关系
            SetParent(hwnd, progman);
            
            // 2. 行政降级：强行压到 Z 轴底部 (HWND_BOTTOM)
            // 这一步是解决“还是挡着”的关键
            let _ = SetWindowPos(hwnd, HWND_BOTTOM, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE);
            
            // 3. 抹除任务栏存在感
            let mut ex_style = GetWindowLongPtrW(hwnd, GWL_EXSTYLE);
            ex_style |= WS_EX_TOOLWINDOW.0 as isize;
            SetWindowLongPtrW(hwnd, GWL_EXSTYLE, ex_style);
        }
    }
}
import win32gui


# List all running windows application titles
def winEnumHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible( hwnd ):
        print(hex(hwnd), win32gui.GetWindowText( hwnd ))
win32gui.EnumWindows( winEnumHandler, None )
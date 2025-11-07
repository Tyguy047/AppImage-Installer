import tkinter as tk
from utils import *
from elements import *

def appimage_path():
    appimage = open_file_dialog()
    print(f"AppImage: {appimage}")

def app_icon_path():
    global icon_path
    icon_path = open_file_dialog()
    icon_path = icon_preview(tk, icon_prev_frame, icon_path=icon_path)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("AppImage Installer")
    root.geometry("600x400")

    icon_path = None

    btn_frame = button_frame(tk, root)
    icon_prev_frame = icon_preview_frame(tk, root)

    select_appimage_btn(tk, btn_frame, appimage_path)
    select_app_icon_btn(tk, btn_frame, app_icon_path)

    icon_preview(tk, icon_prev_frame, icon_path=icon_path)

    check_for_app_folder()
    root.mainloop()
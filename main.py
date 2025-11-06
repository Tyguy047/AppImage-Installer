import tkinter as tk
from utils import *

def appimage_path():
    appimage = open_file_dialog()
    print(f"AppImage: {appimage}")

def app_icon_path():
    icon = open_file_dialog()
    print(f"App Icon: {icon}")

root = tk.Tk()
root.title("AppImage Installer")
root.geometry("600x400")

appimage_selection_button = tk.Button(root, text="Choose An App Image", command=app_icon_path)
appimage_selection_button.pack(pady=20)

app_icon_selection_button = tk.Button(root, text="Choose An Icon", command=app_icon_path)
app_icon_selection_button.pack(pady=20)

root.mainloop()
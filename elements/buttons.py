def select_appimage_btn(tk, btn_frame, appimage_path):
    appimage_selection_button = tk.Button(btn_frame, text="Choose An App Image", command=appimage_path, width=20)
    appimage_selection_button.pack(pady=10, anchor='w')

def select_app_icon_btn(tk, btn_frame, app_icon_path):
    app_icon_selection_button = tk.Button(btn_frame, text="Choose An Icon", command=app_icon_path, width=20)
    app_icon_selection_button.pack(pady=10, anchor='w')
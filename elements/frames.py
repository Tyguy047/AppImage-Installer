def button_frame(tk, root):
    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.LEFT, padx=20, pady=20, anchor='nw')
    return button_frame

def icon_preview_frame(tk, root):
    icon_preview_frame = tk.Frame(root)
    icon_preview_frame.pack(side=tk.RIGHT, padx=20, pady=20, anchor='ne')
    return icon_preview_frame
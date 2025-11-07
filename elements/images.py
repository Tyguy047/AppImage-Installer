from PIL import Image, ImageTk

def icon_preview(tk, icon_prev_frame, icon_path=None):
    # Clear existing widgets in the frame
    for widget in icon_prev_frame.winfo_children():
        widget.destroy()
    
    if icon_path:
        img = Image.open(icon_path)
        img = img.resize((128, 128), Image.LANCZOS)
        preview = ImageTk.PhotoImage(img)

        label = tk.Label(icon_prev_frame, image=preview)
        label.image = preview
        label.pack()

    else:
        label = tk.Label(icon_prev_frame, text="No icon selected", width=20, height=8, bg="lightgray")
        label.pack()

    return label
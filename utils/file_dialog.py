from tkinter import filedialog

def open_file_dialog():
    file_path = filedialog.askopenfilename()
    return file_path
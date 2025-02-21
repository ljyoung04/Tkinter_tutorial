import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
import glob


class ImageConverter(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Image Converter")
        self.geometry("300x100")
        self.resizable(False,False)
        self.folder_path = ""

        self.ui()

    def ui(self):
        select_btn = tk.Button(self,text="Open Folder",width=10,command=self.get_folder_path)
        self.convert_btn = tk.Button(self,text="Convert",width=10,command=self.convert,state='disabled')

        select_btn.pack(expand=True)
        self.convert_btn.pack(expand=True)

    def get_folder_path(self):
        folder_path = filedialog.askdirectory()

        if folder_path:
            self.folder_path = folder_path
            self.convert_btn.config(state='normal')
            

    def convert(self):
        files = glob.glob(self.folder_path + r"\*.png")
        for file in files:
            img = Image.open(file).convert('RGB')
            img.save(file.replace(".png",".pdf"))
        messagebox.showinfo("Success","Convert finish")

if __name__ == "__main__":
    conv = ImageConverter()
    conv.mainloop()

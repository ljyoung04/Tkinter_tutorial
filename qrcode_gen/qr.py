import qrcode
import tkinter as tk 
import uuid
import os

class QrCodeGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("QrCode Generator")
        self.geometry("300x150")
        self.resizable(False,False)
        self.ui()
    
    def ui(self):

        self.addr_field = tk.Entry(self,width=20)
        make_btn = tk.Button(self,text="Make",width=15,command=self.qrgen)

        self.addr_field.pack(pady=30)
        make_btn.pack(pady=10)


    def qrgen(self):
        addr = self.addr_field.get()
        path = f"{os.path.dirname(os.path.abspath(__file__))}\{uuid.uuid4().hex[0:8]}.png"

        qr = qrcode.make(addr)
        qr.show()
        qr.save(path)

if __name__ == "__main__" :
    qr = QrCodeGenerator()
    qr.mainloop()

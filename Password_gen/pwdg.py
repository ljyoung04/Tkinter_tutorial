import tkinter as tk 
import secrets
import string
import os
from tkinter import messagebox, ttk

class PasswordGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator")
        self.geometry("640x400")
        self.resizable(False,False)

        self.ui()

    def ui(self):
        self.password_field = tk.Entry(self,state='readonly')
        self.password_field.pack()

        self.password_len_scale = tk.Scale(self,orient="horizontal",sliderlength=20,length=150,from_=10, to=25)
        self.password_len_scale.pack()

        self.gen_btn = tk.Button(self,text="Generate",command=self.generator)
        self.gen_btn.pack(pady=5)

        sep1 = ttk.Separator(self, orient='horizontal')
        sep1.pack(pady=10,ipadx=80)

        self.save_name = tk.Entry(self)
        self.save_name.pack()

        self.save_btn = tk.Button(self,text='Save',command=self.save_password)
        self.save_btn.pack(pady=5)


    def generator(self):
        len = int(self.password_len_scale.get())
        pwd = self.make_password(len)

        self.password_field.config(state='normal')
        self.password_field.delete(0,25)
        self.password_field.insert(0,pwd)
        self.password_field.config(state='readonly')

    def make_password(self,len):
        charset = string.ascii_letters + string.digits + string.punctuation
        pwd = "".join(secrets.choice(charset) for _ in range(len)) 
        return pwd

    def save_password(self):
        save_name = self.save_name.get()
        save_password = self.password_field.get()

        save_data = f"{save_name} : {save_password}\n"
        try:
            with open(os.path.dirname(os.path.abspath(__file__)) + r"\save.txt",'a') as f:
                f.write(save_data)
            messagebox.showinfo("Success","저장 완료")

        except:
            messagebox.showerror("Error","파일 쓰기에 실패했습니다.")



if __name__ == "__main__":
    pwdg = PasswordGenerator()
    pwdg.mainloop()


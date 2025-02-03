import tkinter as tk 
from tkinter import messagebox

class Timer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.running = False
        self.window_setting()
        self.timer_UI()
        self.btn_UI()

    def window_setting(self):
        self.title("Timer")
        self.geometry("640x400")
        self.resizable(False,False)

    def timer_UI(self):
        #timer
        self.timer_label = tk.Label(self,text="00:00:00",font=("Arial",40))
        self.timer_label.place(relx=0.5,rely=0.5,anchor='center')

    def btn_UI(self):

        #inc btn

        for i in range(3):
            btn = tk.Button(self,relief='flat',text='↑',font=("Arial",30),
                            command=lambda i = i: self.inc(i) )
            btn.place(relx=0.385+(0.115*i),rely=0.35,anchor='center')

        #dec btn

        for i in range(3):
            btn = tk.Button(self,relief='flat',text='↓',font=("Arial",30),
                            command=lambda i = i: self.dec(i))
            btn.place(relx=0.385+(0.115*i),rely=0.65,anchor='center')

        #start, stop btn
        self.pannel = tk.PanedWindow(relief='flat')
        self.pannel.pack(pady=30,anchor='center')

        self.start_btn = tk.Button(self,text="Start",command=self.start_timer)
        self.pannel.add(self.start_btn)

        self.stop_btn = tk.Button(self,text="Stop",state='disabled',command=self.stop_timer)
        self.pannel.add(self.stop_btn)

    def inc(self,key):
        h,m,s = map(int,self.timer_label.cget("text").split(":"))

        if key == 0 :
            if h < 99 : 
                h += 1
        elif key == 1 :
            if m < 59 :
                m += 1
        elif key == 2 :
            if s < 59 :
                s += 1
        
        s = "%02d:%02d:%02d"%(h,m,s)

        self.timer_label.config(text=s)

    def dec(self,key):
        h,m,s = map(int,self.timer_label.cget("text").split(":"))

        if key == 0 :
            if h > 0 : 
                h -= 1
        elif key == 1 :
            if m > 0 :
                m -= 1
        elif key == 2 :
            if s > 0 :
                s -= 1
        
        s = "%02d:%02d:%02d"%(h,m,s)

        self.timer_label.config(text=s)

    def start_timer(self):

        if not self.running:
            self.running = True
            self.update_timer()
            self.start_btn.config(state='disabled')
            self.stop_btn.config(state='normal')

    def update_timer(self):
        h,m,s = map(int,self.timer_label.cget("text").split(":"))
        total_second = s + (m * 60) + (h * 60 * 60)

        if total_second > 0 and self.running:
            total_second -= 1
            self.timer_label.config(text=self.fmt_time(total_second))
            self.after(1000,self.update_timer)
        elif total_second == 0:
            messagebox.showinfo("Timer","타이머가 종료되었습니다.")
            self.start_btn.config(state='normal')

    def fmt_time(self,second):
        min, sec = divmod(second,60)
        hour, min = divmod(min,60)

        return "%02d:%02d:%02d"%(hour,min,sec)

    def stop_timer(self):
        if self.running == True:
            self.running = False
            self.stop_btn.config(state="disabled")
            self.start_btn.config(state='normal')

if __name__ == "__main__":
    timer = Timer()
    timer.mainloop()
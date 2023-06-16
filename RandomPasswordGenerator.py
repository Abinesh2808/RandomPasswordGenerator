from random import sample
from tkinter import *

class RandomPasswordGenerator:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("375x475")
        self.root.title("Random Password Generator")
        self.op1 = IntVar()
        self.op2 = IntVar()
        self.len_gth = StringVar()
        self.msg = StringVar()
        self.frame = Frame(self.root)
        self.frame.pack()
        self.error = None
    def widgets(self):
        entry = Entry(self.frame, textvariable=self.len_gth,width=10)
        label = Label(self.frame, text="Enter Password Length: ",font=("Roboto", 11))
        check1 = Checkbutton(self.frame, text="Do you want to include Numbers ? ",
                             variable=self.op1, width=50,font=("Roboto", 11))
        check2 = Checkbutton(self.frame, text="Do you want to include Special Characters ? ",
                             variable=self.op2, width=50,font=("Roboto", 11))
        msg = Label(self.frame, textvariable=self.msg,font=("Roboto", 11),width=50)
        btn = Button(self.frame, text="Click to Generate Password", command=self.generate,font=("Roboto", 11))

        label.grid(row=1, column=0, padx=90,columnspan=2)
        entry.grid(row=1, column=1, columnspan=3,pady=10)
        check1.grid(row=2, column=0, columnspan=3,pady=10)
        check2.grid(row=3, column=0, columnspan=3,pady=10)
        msg.grid(row=4, column=0, columnspan=3,pady=10)
        btn.grid(row=5, column=0, columnspan=3,pady=10)

        self.frame.place(relx=0.5,rely=0.5,anchor="center")

    def generate(self):
        pass_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        pass_chars_nums = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
        pass_chars_spchars = "@#$%&*ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&*abcdefghijklmnopqrstuvwxyz@#$%&*"
        pass_chars_spchars_nums = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_@#$%&*_@#$%&*abcdefghijklmnopqrstuvwxyz"

        if self.error is not None:
            self.error.destroy()

        try:
            if self.op1.get() == 1 and self.op2.get() == 1:
                p = sample(pass_chars_spchars_nums, int(self.len_gth.get()))
            elif self.op1.get() == 1:
                p = sample(pass_chars_nums, int(self.len_gth.get()))
            elif self.op2.get() == 1:
                p = sample(pass_chars_spchars, int(self.len_gth.get()))
            else:
                p = sample(pass_chars, int(self.len_gth.get()))
            password = ""
            for i in p:
                password += str(i)
            self.msg.set(f"Your password is:  {str(password)}")

        except ValueError:
            self.error = Label(self.frame,text="Enter a Valid number",font=("Roboto", 11),width=50)
            self.error.grid(row=4, column=0, columnspan=3,pady=10)

    def run(self):
        self.widgets()
        self.root.mainloop()

obj = RandomPasswordGenerator()
obj.run()
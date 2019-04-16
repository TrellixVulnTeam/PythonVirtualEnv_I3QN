#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#    Apr 13, 2019 01:04:03 PM +1500  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import page1_support

p="Physics"
c="Chemistry"
m="Maths"
s=" "
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root,p ,c, m ,s
    root = tk.Tk()
    top = Toplevel1 (root)
    page1_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    page1_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+406+121")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#26efdb")

        def call_second_frame_on_top():
           # This function can be called from the first and third windows.
           # Hide the first and third windows and show the second window.
           Frame1.grid_forget()
           Frame2.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

        def call_third_frame_on_top():
           # This function can be called from the first and third windows.
           # Hide the first and third windows and show the second window.
           Frame1.grid_forget()
           Frame3.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

        def make_account():
            name=Entry12.get()
            year=Entry22.get()
            reg_no=Entry32.get()
            email_id=Entry42.get()
            pswd=Entry52.get()
            file1=open("account.txt","a")
            file1.write(name,year,reg_no,email_id,pswd)
            file1.close()


        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.017, rely=0.0, relheight=1.011, relwidth=1.008)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#29dbef")
        self.Frame1.configure(width=605)

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.033, rely=0.022, height=111, width=524)
        self.Label1.configure(activeforeground="#221daa")
        self.Label1.configure(background="#2c8481")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Lucida Fax} -size 24 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''TEST YOURSELF''')
        self.Label1.configure(width=524)

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.149, rely=0.484, height=54, width=117)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Lucida Fax} -size 14")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''REGISTER''')
        self.Button1.configure(width=117)
        self.Button1.configure(command = call_second_frame_on_top())

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.579, rely=0.484, height=54, width=127)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Lucida Fax} -size 14")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''LOGIN''')
        self.Button2.configure(width=127)
        self.Button2.configure(command = call_third_frame_on_top())

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=1.008)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=605)

        self.Name = tk.Label(self.Frame2)
        self.Name.place(relx=0.066, rely=0.11, height=41, width=104)
        self.Name.configure(activebackground="#f9f9f9")
        self.Name.configure(activeforeground="black")
        self.Name.configure(background="#d9d9d9")
        self.Name.configure(disabledforeground="#a3a3a3")
        self.Name.configure(font="-family {Lucida Fax} -size 14")
        self.Name.configure(foreground="#000000")
        self.Name.configure(highlightbackground="#d9d9d9")
        self.Name.configure(highlightcolor="black")
        self.Name.configure(text='''Name''')

        self.Year = tk.Label(self.Frame2)
        self.Year.place(relx=0.066, rely=0.22, height=41, width=84)
        self.Year.configure(activebackground="#f9f9f9")
        self.Year.configure(activeforeground="black")
        self.Year.configure(background="#d9d9d9")
        self.Year.configure(disabledforeground="#a3a3a3")
        self.Year.configure(font="-family {Lucida Fax} -size 14")
        self.Year.configure(foreground="#000000")
        self.Year.configure(highlightbackground="#d9d9d9")
        self.Year.configure(highlightcolor="black")
        self.Year.configure(text='''Year''')

        self.Registration_Number = tk.Label(self.Frame2)
        self.Registration_Number.place(relx=0.083, rely=0.33, height=31
                , width=224)
        self.Registration_Number.configure(activebackground="#f9f9f9")
        self.Registration_Number.configure(activeforeground="black")
        self.Registration_Number.configure(background="#d9d9d9")
        self.Registration_Number.configure(disabledforeground="#a3a3a3")
        self.Registration_Number.configure(font="-family {Lucida Fax} -size 14")
        self.Registration_Number.configure(foreground="#000000")
        self.Registration_Number.configure(highlightbackground="#d9d9d9")
        self.Registration_Number.configure(highlightcolor="black")
        self.Registration_Number.configure(text='''Registration Number''')

        self.Email = tk.Label(self.Frame2)
        self.Email.place(relx=0.099, rely=0.44, height=21, width=64)
        self.Email.configure(activebackground="#f9f9f9")
        self.Email.configure(activeforeground="black")
        self.Email.configure(background="#d9d9d9")
        self.Email.configure(disabledforeground="#a3a3a3")
        self.Email.configure(font="-family {Lucida Fax} -size 14")
        self.Email.configure(foreground="#000000")
        self.Email.configure(highlightbackground="#d9d9d9")
        self.Email.configure(highlightcolor="black")
        self.Email.configure(text='''Email''')

        self.Password = tk.Label(self.Frame2)
        self.Password.place(relx=0.083, rely=0.527, height=41, width=124)
        self.Password.configure(activebackground="#f9f9f9")
        self.Password.configure(activeforeground="black")
        self.Password.configure(background="#d9d9d9")
        self.Password.configure(disabledforeground="#a3a3a3")
        self.Password.configure(font="-family {Lucida Fax} -size 14")
        self.Password.configure(foreground="#000000")
        self.Password.configure(highlightbackground="#d9d9d9")
        self.Password.configure(highlightcolor="black")
        self.Password.configure(text='''Password''')

        self.Entry12 = tk.Entry(self.Frame2)
        self.Entry12.place(relx=0.529, rely=0.132,height=20, relwidth=0.271)
        self.Entry12.configure(background="white")
        self.Entry12.configure(disabledforeground="#a3a3a3")
        self.Entry12.configure(font="TkFixedFont")
        self.Entry12.configure(foreground="#000000")
        self.Entry12.configure(highlightbackground="#d9d9d9")
        self.Entry12.configure(highlightcolor="black")
        self.Entry12.configure(insertbackground="black")
        self.Entry12.configure(selectbackground="#c4c4c4")
        self.Entry12.configure(selectforeground="black")

        self.Entry22 = tk.Entry(self.Frame2)
        self.Entry22.place(relx=0.529, rely=0.242,height=20, relwidth=0.271)
        self.Entry22.configure(background="white")
        self.Entry22.configure(disabledforeground="#a3a3a3")
        self.Entry22.configure(font="TkFixedFont")
        self.Entry22.configure(foreground="#000000")
        self.Entry22.configure(highlightbackground="#d9d9d9")
        self.Entry22.configure(highlightcolor="black")
        self.Entry22.configure(insertbackground="black")
        self.Entry22.configure(selectbackground="#c4c4c4")
        self.Entry22.configure(selectforeground="black")

        self.Entry32 = tk.Entry(self.Frame2)
        self.Entry32.place(relx=0.529, rely=0.352,height=20, relwidth=0.271)
        self.Entry32.configure(background="white")
        self.Entry32.configure(disabledforeground="#a3a3a3")
        self.Entry32.configure(font="TkFixedFont")
        self.Entry32.configure(foreground="#000000")
        self.Entry32.configure(highlightbackground="#d9d9d9")
        self.Entry32.configure(highlightcolor="black")
        self.Entry32.configure(insertbackground="black")
        self.Entry32.configure(selectbackground="#c4c4c4")
        self.Entry32.configure(selectforeground="black")

        self.Entry42 = tk.Entry(self.Frame2)
        self.Entry42.place(relx=0.529, rely=0.462,height=20, relwidth=0.271)
        self.Entry42.configure(background="white")
        self.Entry42.configure(disabledforeground="#a3a3a3")
        self.Entry42.configure(font="TkFixedFont")
        self.Entry42.configure(foreground="#000000")
        self.Entry42.configure(highlightbackground="#d9d9d9")
        self.Entry42.configure(highlightcolor="black")
        self.Entry42.configure(insertbackground="black")
        self.Entry42.configure(selectbackground="#c4c4c4")
        self.Entry42.configure(selectforeground="black")

        self.Entry52 = tk.Entry(self.Frame2)
        self.Entry52.place(relx=0.529, rely=0.571,height=20, relwidth=0.271)
        self.Entry52.configure(background="white")
        self.Entry52.configure(disabledforeground="#a3a3a3")
        self.Entry52.configure(font="TkFixedFont")
        self.Entry52.configure(foreground="#000000")
        self.Entry52.configure(highlightbackground="#d9d9d9")
        self.Entry52.configure(highlightcolor="black")
        self.Entry52.configure(insertbackground="black")
        self.Entry52.configure(selectbackground="#c4c4c4")
        self.Entry52.configure(selectforeground="black")

        self.SUBMIT = tk.Button(self.Frame2)
        self.SUBMIT.place(relx=0.628, rely=0.725, height=49, width=107)
        self.SUBMIT.configure(activebackground="#ececec")
        self.SUBMIT.configure(activeforeground="#000000")
        self.SUBMIT.configure(background="#23d8d2")
        self.SUBMIT.configure(disabledforeground="#a3a3a3")
        self.SUBMIT.configure(font="-family {Segoe UI} -size 16")
        self.SUBMIT.configure(foreground="#000000")
        self.SUBMIT.configure(highlightbackground="#d9d9d9")
        self.SUBMIT.configure(highlightcolor="black")
        self.SUBMIT.configure(pady="0")
        self.SUBMIT.configure(text='''SUBMIT''')
        self.SUBMIT.configure(command=make_account())




        self.Frame3 = tk.Frame(top)
        self.Frame3.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=1.008)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#d9d9d9")
        self.Frame3.configure(highlightbackground="#d9d9d9")
        self.Frame3.configure(highlightcolor="black")
        self.Frame3.configure(width=605)

        self.Label13 = tk.Label(self.Frame3)
        self.Label13.place(relx=0.083, rely=0.132, height=51, width=94)
        self.Label13.configure(activebackground="#f9f9f9")
        self.Label13.configure(activeforeground="black")
        self.Label13.configure(background="#d9d9d9")
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(font="-family {Lucida Fax} -size 14")
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(highlightbackground="#d9d9d9")
        self.Label13.configure(highlightcolor="black")
        self.Label13.configure(text='''LOGIN ID''')

        self.Label23 = tk.Label(self.Frame3)
        self.Label23.place(relx=0.083, rely=0.308, height=51, width=124)
        self.Label23.configure(activebackground="#f9f9f9")
        self.Label23.configure(activeforeground="black")
        self.Label23.configure(background="#d9d9d9")
        self.Label23.configure(disabledforeground="#a3a3a3")
        self.Label23.configure(font="-family {Lucida Fax} -size 14")
        self.Label23.configure(foreground="#000000")
        self.Label23.configure(highlightbackground="#d9d9d9")
        self.Label23.configure(highlightcolor="black")
        self.Label23.configure(text='''PASSWORD''')
        self.Label23.configure(width=124)

        self.Entry13 = tk.Entry(self.Frame3)
        self.Entry13.place(relx=0.38, rely=0.176,height=20, relwidth=0.288)
        self.Entry13.configure(background="white")
        self.Entry13.configure(disabledforeground="#a3a3a3")
        self.Entry13.configure(font="TkFixedFont")
        self.Entry13.configure(foreground="#000000")
        self.Entry13.configure(highlightbackground="#d9d9d9")
        self.Entry13.configure(highlightcolor="black")
        self.Entry13.configure(insertbackground="black")
        self.Entry13.configure(selectbackground="#c4c4c4")
        self.Entry13.configure(selectforeground="black")

        self.Entry23 = tk.Entry(self.Frame3)
        self.Entry23.place(relx=0.38, rely=0.33,height=20, relwidth=0.288)
        self.Entry23.configure(background="white")
        self.Entry23.configure(disabledforeground="#a3a3a3")
        self.Entry23.configure(font="TkFixedFont")
        self.Entry23.configure(foreground="#000000")
        self.Entry23.configure(highlightbackground="#d9d9d9")
        self.Entry23.configure(highlightcolor="black")
        self.Entry23.configure(insertbackground="black")
        self.Entry23.configure(selectbackground="#c4c4c4")
        self.Entry23.configure(selectforeground="black")

        self.SUBMIT3 = tk.Button(self.Frame3)
        self.SUBMIT3.place(relx=0.678, rely=0.703, height=44, width=107)
        self.SUBMIT3.configure(activebackground="#ececec")
        self.SUBMIT3.configure(activeforeground="#000000")
        self.SUBMIT3.configure(background="#30d8d8")
        self.SUBMIT3.configure(disabledforeground="#a3a3a3")
        self.SUBMIT3.configure(font="-family {Lucida Fax} -size 14")
        self.SUBMIT3.configure(foreground="#000000")
        self.SUBMIT3.configure(highlightbackground="#d9d9d9")
        self.SUBMIT3.configure(highlightcolor="black")
        self.SUBMIT3.configure(pady="0")
        self.SUBMIT3.configure(text='''SUBMIT''')


       
        self.Frame4 = tk.Frame(top)
        self.Frame4.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=1.008)
        self.Frame4.configure(relief='groove')
        self.Frame4.configure(borderwidth="2")
        self.Frame4.configure(relief="groove")
        self.Frame4.configure(background="#d6d6d6")
        self.Frame4.configure(highlightbackground="#d9d9d9")
        self.Frame4.configure(highlightcolor="black")
        self.Frame4.configure(width=605)

        self.Message1 = tk.Message(self.Frame4)
        self.Message1.place(relx=0.083, rely=0.022, relheight=0.127
                , relwidth=0.443)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(font="-family {Lucida Fax} -size 18 -weight bold")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''STUDENT PROFILE''')
        self.Message1.configure(width=268)

        self.Label14 = tk.Label(self.Frame4)
        self.Label14.place(relx=0.017, rely=0.22, height=41, width=144)
        self.Label14.configure(activebackground="#f9f9f9")
        self.Label14.configure(activeforeground="black")
        self.Label14.configure(background="#d9d9d9")
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(font="-family {Lucida Fax} -size 14")
        self.Label14.configure(foreground="#000000")
        self.Label14.configure(highlightbackground="#d9d9d9")
        self.Label14.configure(highlightcolor="black")
        self.Label14.configure(text='''NAME''')

        self.Label24 = tk.Label(self.Frame4)
        self.Label24.place(relx=0.017, rely=0.352, height=41, width=174)
        self.Label24.configure(activebackground="#f9f9f9")
        self.Label24.configure(activeforeground="black")
        self.Label24.configure(background="#d9d9d9")
        self.Label24.configure(disabledforeground="#a3a3a3")
        self.Label24.configure(font="-family {Lucida Fax} -size 14")
        self.Label24.configure(foreground="#000000")
        self.Label24.configure(highlightbackground="#d9d9d9")
        self.Label24.configure(highlightcolor="black")
        self.Label24.configure(text='''STUDENT ID''')
        self.Label24.configure(width=174)

        self.Label34 = tk.Label(self.Frame4)
        self.Label34.place(relx=0.017, rely=0.462, height=61, width=164)
        self.Label34.configure(activebackground="#f9f9f9")
        self.Label34.configure(activeforeground="black")
        self.Label34.configure(background="#d9d9d9")
        self.Label34.configure(disabledforeground="#a3a3a3")
        self.Label34.configure(font="-family {Lucida Fax} -size 14")
        self.Label34.configure(foreground="#000000")
        self.Label34.configure(highlightbackground="#d9d9d9")
        self.Label34.configure(highlightcolor="black")
        self.Label34.configure(text='''SUBJECT''')
        self.Label34.configure(width=164)

        self.TCombobox1 = ttk.Combobox(self.Frame4)
        self.TCombobox1.place(relx=0.496, rely=0.505, relheight=0.046
                , relwidth=0.236)
        self.value_list = [p,c,m]
        self.TCombobox1.configure(values=self.value_list)
        self.TCombobox1.configure(textvariable=s)
        self.TCombobox1.configure(takefocus="")

        self.Message24 = tk.Message(self.Frame4)
        self.Message24.place(relx=0.496, rely=0.374, relheight=0.051
                , relwidth=0.231)
        self.Message24.configure(background="#ffffff")
        self.Message24.configure(foreground="#000000")
        self.Message24.configure(highlightbackground="#d9d9d9")
        self.Message24.configure(highlightcolor="black")
        self.Message24.configure(width=140)

        self.Message34 = tk.Message(self.Frame4)
        self.Message34.place(relx=0.496, rely=0.264, relheight=0.051
                , relwidth=0.215)
        self.Message34.configure(background="#f7f7f7")
        self.Message34.configure(foreground="#000000")
        self.Message34.configure(highlightbackground="#d9d9d9")
        self.Message34.configure(highlightcolor="black")
        self.Message34.configure(width=130)



if __name__ == '__main__':
   vp_start_gui()





import tkinter as ttk
from tkinter import *
from tkinter import messagebox
win=Tk()
win.title("Registration")

variable1=StringVar()
variable2=StringVar()
variable3=StringVar()
variable4=IntVar()
variable5=IntVar()
variable6=IntVar()

i1=Label(win, text="Name")
i1.grid(row=0, column=0, sticky=W)
e1=Entry(win, width=50, textvariable=variable1)
e1.grid(row=0,column=1,sticky=W)

i2=Label(win, text="Course")
i2.grid(row=1, column=0, sticky=W)
e2=Entry(win, width=50, textvariable=variable2)
e2.grid(row=1,column=1,sticky=W)

i3=Label(win, text="Semester")
i3.grid(row=2, column=0, sticky=W)
e3=Entry(win, width=50, textvariable=variable3)
e3.grid(row=2,column=1,sticky=W)

i4=Label(win, text="Form No.")
i4.grid(row=3, column=0, sticky=W)
e4=Entry(win, width=50, textvariable=variable4)
e4.grid(row=3,column=1,sticky=W)

i5=Label(win, text="Contact No.")
i5.grid(row=4, column=0, sticky=W)
e5=Entry(win, width=50, textvariable=variable5)
e5.grid(row=4,column=1,sticky=W)

t1=Label(win,text="Select your gender:")
t1.grid(row=5,column=0,sticky=W)
#b1=Radiobutton(win,text="Male", value="Male")
#b1.grid(row=6,column=0,sticky=W)
#
#b2=Radiobutton(win,text="Female", value="Female")
#b2.grid(row=7,column=0,sticky=W)
#
#b3=Radiobutton(win,text="Other", value="Other")
#b3.grid(row=8,column=0,sticky=W)

#widget_var = ttk.StringVar()
#
#gender=ttk.Combobox(win, width=20, textvariable=widget_var)
#gender["Value"]=("Male", "Female", "Other")
#gender.current(0)
#gender.grid(row=6, column=0)

b4=Checkbutton(win, text="I agree to all the terms and conditions", variable=variable6)
b4.grid(row=9,column=0,sticky=W)

def action():
    N=variable1.get()
    C=variable2.get()
    S=variable3.get()
    Fno=variable4.get()
    Cno=variable5.get()
    Check=variable6.get()
    if Check==0:
       messagebox.showerror("Error!","You need to agree to all the Terms & Conditions before continuing")
    else:
        print(f"Name is: {N} \nCourse: {C} \nSemester: {S} \nForm No. {Fno}")
            

b5=Button(win, text="Submit", bg="red", fg="white", command=action)
b5.grid(row=10,column=1,sticky=W)

win.mainloop()
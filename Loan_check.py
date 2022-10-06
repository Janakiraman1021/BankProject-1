from tkinter import *
import tkinter .messagebox as mb
import time as t
import sqlite3 as s
con = s.connect("bankdet.db")
cur = con.cursor()

def loancheck():
    cur.execute(" SELECT * FROM BANK where ACC_NO = '%s' " %(acno.get()))
    res = cur.fetchall()
    for i in res:
        Label(kj,text = 'Name  :' + str(i[0]) ,fg=fg,bg=bg,font = fnte).place(x=768,y=130)
        Label(kj,text = 'Acc no : ' + str(i[1]) ,fg=fg,bg=bg,font = fnte).place(x=768,y=180)
        Label(kj,text = 'DOB : ' + str(i[2]) ,fg=fg,bg=bg,font = fnte).place(x=768,y=230)
        Label(kj,text = 'Age :  ' + str(i[3]) ,fg=fg,bg=bg,font = fnte).place(x=768,y=280)
        Label(kj,text = 'Gender :  ' + str(i[4]) ,fg=fg,bg=bg,font = fnte).place(x=768,y=330)
        Label(kj,text = 'Acc Type : ' + str(i[6]) ,fg=fg,bg=bg,font = fnte).place(x=768,y=380)
        Label(kj,text = 'Aadhar No :' + str(i[7]) ,fg=fg,bg=bg,font = fnte).place(x=768,y=430)
        Label(kj,text = 'Pan No  : '  + str(i[8]) ,fg=fg,bg=bg,font = fnte).place(x=768,y=480)
        Label(kj,text = 'Mobile No : ' + str(i[11]) ,fg=fg,bg=bg,font = fnte).place(x=768,y=530)
        Label(kj,text = 'Current Loans : ' + str(i[15]) ,fg=fg,bg=bg,font = fnte).place(x=768,y=580)
        loan = i[15]
        if loan==0 or loan<=2:
            mb.showinfo("Hello "," You Are Eligible To Apply A Loan Ar Our Bank")
        else:
            mb.showinfo("Alert "," You Are  Not  Eligible To Apply A Loan Ar Our Bank")
def applyloan():
    cur.execute(" SELECT * FROM BANK where ACC_NO = '%s' " %(acno.get()))
    res = cur.fetchall()
    #res = int(rs)
    for i in res:
        loan = i[15]
        if loan==0 or loan<=2:
            root = Tk()
            root.state('zoomed')
            Label(root,text = 'Loan Applicarion Form',fg=fg1,font=fnt1).place(x=295,y=25)
            Label(root,text='Name',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=100)
            Label(root,text='Account Number ',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=150)
            Label(root,text='Date Of Birth',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=200)
            Label(root,text='Age',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=250)
            Label(root,text='Gender',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=300)
            Label(root,text='Account Type',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=350)
            Label(root,text='Aadhar Number',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=400)
            Label(root,text='Pan Number',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=450)
            Label(root,text='Mobile  Number',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=500)
            Label(root,text='Loan Type',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=550)
            # Entry's & VARIABLE'S
            name = StringVar()
            acc_no=StringVar()
            dob=StringVar()
            age = IntVar()
            gender = StringVar()
            acc_type=StringVar()
            aadhar = IntVar()
            pan = StringVar()
            mobilenum = IntVar()
            
            Entry(kj,textvariable=name,font=fnt,width=20).place(x=500,y = 100)
            Entry(root,textvariable=acc_no,font=fnt,width=20).place(x=500,y = 150)
            Entry(root,textvariable=dob,font=fnt,width=20).place(x=500,y = 200)
            Entry(root,textvariable=age,font=fnt,width=20).place(x=500,y = 250)
            Entry(root,textvariable=gender,font=fnt,width=20).place(x=500,y = 300)
            Radiobutton(root,text='MALE',variable=gender,value='MALE',font=fnt).place(x=500,y=300)
            Radiobutton(root,text='FEMALE',variable=gender,value='FEMALE',font=fnt).place(x=600,y=300)
            acc_type.set('SB')
            Radiobutton(root,text='SAVINGS',variable=acc_type,value='SB',font=fnt).place(x=500,y=400)
            Radiobutton(root,text='CURRENT',variable=acc_type,value='CUR',font=fnt).place(x=650,y=400)
            Entry(root,textvariable=aadhar,font=fnt,width=20).place(x=500,y = 450)
            Entry(root,textvariable=mobilenum,font=fnt,width=20).place(x=500,y = 650)
        

fg1='orange'
fg='blue'
bg='white'
fnt1 = 'Copperplate Gothic Bold',40
fnt = 'Copperplate Gothic Bold',25
fnte = 'Copperplate Gothic Bold',20
kj = Tk()
kj.state('zoomed')
#Label's
Label(kj,text = 'XYZ BANK LOAN APPLICATION FORM',fg=fg1,font=fnt1).place(x=195,y=25)
Label(kj,text = 'Account  Number ',fg=fg,bg=bg,font=fnt).place(x=0,y=130)
#Variable
acno = StringVar()

#Entry's
Entry(kj,textvariable = acno,fg=fg,bg=bg,font=fnte).place(x=359,y=135)

#Button's
Button(kj,text = 'Check Loan Status',fg=fg,bg=bg,font=fnt,command = loancheck).place(x=150,y=200)
#Button(kj,text = 'Apply Loan',fg=fg,bg=bg,font=fnt,command = applyloan).place(x=150,y=300)

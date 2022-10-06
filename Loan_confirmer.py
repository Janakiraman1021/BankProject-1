from tkinter import *
import tkinter.messagebox as mb

def seeloan():
    import sqlite3
    con = sqlite3.connect("bankdet.db")
    cur = con.cursor()
    
    cur.execute(" SELECT * FROM BANK where ACC_NO = '%s' " %(acc_no.get()))
    res = cur.fetchall()
    for i in res:
        global name,accno,loantype,loanamt
        name = i[0]
        accno = i[1]
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
    cur.execute("SELECT * FROM LOANAPPLY where ACC_NO = '%s'"%acc_no.get())
    result = cur.fetchall()
    for j in result:
        loantype = j[9]
        loanamt = j[10]
        Label(kj,text = 'Requsted Loan Type  :' + str(j[9]) ,fg=fg,bg=bg,font = fnte).place(x=768,y=630)
        Label(kj,text = 'Requested Loan Amount : ' + str(j[10]) ,fg=fg,bg=bg,font = fnte).place(x=768,y=680)
    con.commit()
    con.close()
def confirmloan():
    import sqlite3
    con = sqlite3.connect("bankdet.db")
    cur = con.cursor()
    cur.execute(" INSERT INTO LOANCONFIRM (NAME,ACC_NO,LOAN_TYPE,LOAN_AMT) VALUES ('%s','%s','%s',%d)"%(name,accno,loantype,loanamt))
    if loanamt<=10000000:
        st1 = 'YES'
        cur.execute("UPDATE  LOANCONFIRM SET LOAN_STAT = '%s' where ACC_NO = '%s'" %(st1,acc_no.get()))
        cur.execute("UPDATE  BANK SET CUR_LOAN  = CUR_LOAN+1 where ACC_NO = '%s'"%(acc_no.get()))
        cur.execute("UPDATE  BANK SET BALANCE =  BALANCE+%d where ACC_NO = '%s'"%(loanamt,acc_no.get()))
        mb.showinfo("Congratulations","Dear '%s' Your Loan Has Been Sactioned It Will Be Deposited At Your Account Within 24 Hour's"%(name))
    elif loanamt>10000000:
        st = 'NO'
        cur.execute("UPDATE  LOANCONFIRM SET LOAN_STAT = '%s' where ACC_NO = '%s'" %(st,acc_no.get()))
        mb.showinfo("Dear Customer ","I'm Really Sorry To Say That Your Loan Application Has Been cancelled")
    con.commit()
    con.close()
    

def table():
    import sqlite3
    con = sqlite3.connect("bankdet.db")
    cur = con.cursor()
    cur.execute(""" CREATE TABLE LOANCONFIRM (
                              NAME VARCHAR (90),
                              ACC_NO VARCHAR(90),
                              LOAN_TYPE VARCHAR(90),
                              LOAN_AMT INT,
                              LOAN_STAT VARCHAR(90))""")
    mb.showinfo("")    
               

kj = Tk()
kj.state('zoomed')
fg1='orange'
fg='blue'
bg='white'
fnt1 = 'Copperplate Gothic Bold',40
fnt = 'Copperplate Gothic Bold',25
fnte = 'Copperplate Gothic Bold',20
Label(kj,text='Account Number ',font=fnt,fg=fg,bg=bg,width = 20).place(x=50,y=100)
acc_no=StringVar()
Entry(kj,textvariable=acc_no,font=fnt,width=15).place(x=550,y = 100)
Button(kj,text = 'See Requsted Loan',fg=fg,bg=bg,font=fnte,command = seeloan).place(x=150,y=150)
Button(kj,text = 'Confirm Loan',fg=fg,bg=bg,font=fnte,command = confirmloan).place(x=500,y=150)

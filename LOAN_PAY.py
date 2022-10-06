from tkinter import *
import tkinter.messagebox as mb

def seeamt():
    import sqlite3
    con  = sqlite3.connect("bankdet.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM LOANCONFIRM where ACC_NO = '%s'"%(acc_no.get()))
    res = cur.fetchall()
    for i in res:
        amount = i[3]/15
        intrest = int(amount)+(24*20000)
        
        Label(kj,text = "Name :"+str(i[0]),fg=fg,bg=bg,font=fnte,width = 25).place(x=900,y=200)
        Label(kj,text = "Acc No :"+str(i[1]),fg=fg,bg=bg,font=fnte,width = 25).place(x=900,y=300)
        Label(kj,text = "Loan Type :"+str(i[2]),fg=fg,bg=bg,font=fnte,width = 25).place(x=900,y=400)
        Label(kj,text = "Loan Amount :"+str(i[3]),fg=fg,bg=bg,font=fnte,width = 25).place(x=900,y=500)
        Label(kj,text = "Total Amount :"+str(intrest),fg=fg,bg=bg,font=fnte,width = 25).place(x=900,y=600)
        Button(kj,text = "Pay Loan ",fg=fg,bg=bg,font= fnte,command = payloan).place(x=550,y=200)

def payamount():
        import sqlite3
        con  = sqlite3.connect("bankdet.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM LOANCONFIRM where ACC_NO = '%s'"%(acc_no.get()))
        res = cur.fetchall()
        for i in res:
            amount = i[3]/15
            intrest = int(amount)+(24*20000)        
        global totalamtpaid
        totalamtpaid = 0
        cur.execute("SELECT * FROM LOANPAY where ACC_NO = '%s' "%(acc_no.get()))
        result = cur.fetchall()
        for x in result:
            totalamtpaid = 0
        if amt>=0:
                cur.execute("""INSERT INTO LOANPAY (NAME,ACC_NO,LOAN_TYPE,LOAN_AMT,AMT_PAID,TOTAL_LOAN_PAID,AMT_PENDING,TOTAL_LOAN_AMT)
                            VALUES('%s','%s','%s',%d,%d,%d,%d,%d)"""%(name,acc_no.get(),lt,amt,intrest_pay.get() ,intrest_pay.get() ,amt-intrest_pay.get(),intrest))
                pen = intrest - intrest_pay.get()
                mb.showinfo("Alert","Loan Paid SuccessFully\n Pending Amount : %d"%pen)
        con.commit()
        con.close()
        
        

def payloan():
    import sqlite3
    con  = sqlite3.connect("bankdet.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM LOANCONFIRM where ACC_NO = '%s'"%(acc_no.get()))
    res = cur.fetchall()
    for i in res:
        global amount,name,lt,amt
        name = i[0]
        lt = i[2]
        amt = i[3]
    amount = amt/15
    intrest = int(amount)+(24*20000)
    acno = StringVar()
    Label(kj,text = "Total Amount To Be Paid : "+str(intrest),fg=fg,bg=bg,font=fnte,width = 25).place(x=100,y=300)
    Label(kj,text = "Account No ",fg=fg,bg=bg,font=fnt,width = 10).place(x=100,y=400)
    Entry(kj,textvariable = acno,font=fnte,width = 10).place(x=400,y=400)
    Button(kj,text="Pay Amount",fg=fg,bg=bg,font=fnte,command = payamount).place(x=366,y=608)



fg1='orange'
fg='blue'
bg='white'
fnt1 = 'Copperplate Gothic Bold',40
fnt = 'Copperplate Gothic Bold',25
fnte = 'Copperplate Gothic Bold',20
kj = Tk()
kj.state('zoomed')

Label(kj,text="Pay Loan ",fg=fg1,font=fnt1).place(x=600,y=0)
Label(kj,text = "Important For Every Loan Intrest Is 10%",fg=fg,bg=bg,font=fnt).place(x=300,y=100)
Label(kj,text = "Account Number ",fg=fg,bg=bg,font = fnt).place(x=50,y=150)
Label(kj,text = "Amount ",fg=fg,bg=bg,font=fnt,width = 10).place(x=800,y=150)


#Entry's
acc_no = StringVar()
intrest_pay = IntVar()
Entry(kj,textvariable = acc_no ,font=fnte).place(x=400,y=150)
Entry(kj,textvariable = intrest_pay,font = fnte,width = 10).place(x=1050,y=150)


#BUTTON'S
Button(kj,text = "See Total Loan Amount ",fg=fg,bg=bg,font= fnte,command = seeamt).place(x=150,y=200)

      

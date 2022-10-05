from tkinter import *
import tkinter.messagebox as mb

def check():
    global bal
    import sqlite3
    con = sqlite3.connect('bankdet.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM BANK')
    res=cur.fetchall()
    a=0
    for i in res:
        if i[1]==acc_no.get():
            Label(kj,text='Account Holder Name :'+i[0],fg='black',bg='white',font=fnt).place(x=1000,y=200)
            Label(kj,text = 'Account Type :'+i[6],fg='black',bg='white',font=fnt).place(x=1000,y=250)
            Label(kj,text='Balance  :'+str(i[14]),fg='black',bg='white',font=fnt).place(x=1000,y=300)
            bal = i[14]

    
    con.commit()
    con.close()

def trans_cat():
    trans = trans_type.get()
    if trans=='dep':
            import sqlite3
            con = sqlite3.connect('bankdet.db')
            cur = con.cursor()
            trans = trans_type.get()            
            cur.execute("INSERT INTO TRANS (ACC_NO,MODE_PAY,TRANS_TYPE,AMOUNT,DATE,PAY_REASON) VALUES('%s','%s','%s',%d,'%s','%s')"%(acc_no.get(),mode_pay.get(),trans_type.get(),amount.get(),date.get(),reasonpay.get()))
            cur.execute('SELECT * FROM BANK')
            res = cur.fetchall()
            for i in res:
                global amt
                amt = amount.get()
            cur.execute("UPDATE BANK SET BALANCE = BALANCE+%d where ACC_NO = '%s';"%(amount.get(),acc_no.get()))
            con.commit()
            con.close()
            mb.showinfo("Alert","Dear Customer, Your Money Transcation Successfully Your Account\n\tAccount Number : '%s'\n\tThe Amount You Deposited : %d"%(acc_no.get(),amount.get()))            
            
    elif trans=='with_draw':
            if amount.get()<=bal:
                import sqlite3
                con = sqlite3.connect('bankdet.db')
                cur = con.cursor()
                trans = trans_type.get()
                cur.execute("INSERT INTO TRANS (ACC_NO,MODE_PAY,TRANS_TYPE,AMOUNT,DATE,PAY_REASON) VALUES('%s','%s','%s',%d,'%s','%s')"%(acc_no.get(),mode_pay.get(),trans_type.get(),amount.get(),date.get(),reasonpay.get()))
                cur.execute('SELECT * FROM BANK')
                res = cur.fetchall()
                for i in res:
                    amt = amount.get()
                cur.execute("UPDATE BANK SET BALANCE = BALANCE-%d where ACC_NO = '%s';"%(amount.get(),acc_no.get()))
                con.commit()
                con.close()
                mb.showinfo("Alert","Dear Customer, Your Money Transcation Successfully Your Account\n\tAccount Number : '%s'\n\tThe Amount You WithDrawed : %d"%(acc_no.get(),amount.get()))

            else:
                mb.showinfo("Alert","Insuffcient Fund's At Your Account")
    
        

kj= Tk()
kj.state('zoomed')
kj.title('Transcation Page')
font_1='Gill sans MT  ',55
fnt='Gill sans MT  Condensed',20
fg='Red'
bg='white'
wth=25

#Label's
Label(kj,text='XYZ Bank Transcation Page',fg='Orange',font=font_1).place(x=280,y=--15)
Label(kj,text=' Enter Your Account Number ',fg=fg,bg=bg,font=fnt,width=wth).place(x=50,y=150)
Label(kj,text='Mode Of Pay',fg=fg,bg=bg,font=fnt,width=wth).place(x=50,y=240)
Label(kj,text='Reason Of Pay',fg=fg,bg=bg,font=fnt,width=wth).place(x=50,y=330)
Label(kj,text='Transcation Type',fg=fg,bg=bg,font=fnt,width=wth).place(x=50,y=420)
Label(kj,text='Date',fg=fg,bg=bg,font=fnt,width=wth).place(x=50,y=510)
Label(kj,text='Amount',fg=fg,bg=bg,font=fnt,width=wth).place(x=50,y=600)

#Variable Declareation's
acc_no = StringVar()
mode_pay = StringVar()
trans_type = StringVar()
amount = IntVar()
amtwords = StringVar()
date = StringVar()
reasonpay = StringVar()


#Entry's
fg='black'
Entry(kj,textvariable = acc_no,fg=fg,bg=bg,font=fnt).place(x=550,y=150)
mode_pay.set('cash')
Radiobutton(kj,text='Cash',variable = mode_pay,value = 'cash',fg=fg,font=fnt).place(x=550,y=240)
Radiobutton(kj,text='Cheque',variable = mode_pay,value = 'cheque',fg=fg,font=fnt).place(x=700,y=240)
Entry(kj,textvariable = reasonpay,fg=fg,bg=bg,font=fnt).place(x=550,y=330)
Entry(kj,textvariable = date,fg=fg,bg=bg,font=fnt).place(x=550,y=510)
Entry(kj,textvariable = amount,fg=fg,bg=bg,font=fnt).place(x=550,y=600)
trans_type.set('dep')
Radiobutton(kj,text='Deposit',variable = trans_type,value='dep',fg=fg,font=fnt).place(x=550,y=420)
Radiobutton(kj,text='WithDraw',variable = trans_type,value='with_draw',fg=fg,font=fnt).place(x=700,y=420)

#Button's
fg='blue'
wth=20
bg='pink'
fnt='Gill sans MT  Condensed',16
Button(kj,text='Transact Money',fg=fg,bg=bg,font=fnt,width=wth,command = trans_cat).place(x=200,y=780)
Button(kj,text='Exit',fg=fg,bg=bg,font=fnt,width=wth).place(x=900,y=780)
Button(kj,text='Check Account Details',fg=fg,bg=bg,font=fnt,width=wth,command = check).place(x=900,y=150)

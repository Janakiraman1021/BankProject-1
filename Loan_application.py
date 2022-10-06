from tkinter import *
import tkinter .messagebox as mb
import time as t

def create():
    import sqlite3 as s
    con = s.connect("bankdet.db")
    cur = con.cursor()    
    cur.execute(  """ CREATE TABLE LOANAPPLY(
                                    NAME VARCHAR(90),
                                    ACC_NO VARCHAR(90),
                                    DOB VARCHAR(90),
                                    AGE INT,
                                    GENDER VARCHAR(90),
                                    ACC_TYPE VARCHAR(90),
                                    AADHAR INT,
                                    PAN VARCHAR(90),
                                    MOBILENUM VARCHAR(90),
                                    LOAN_TYPE VARCHAR(90),
                                    LOAN_AMT INT) """)
    mb.showinfo("alert","Table Created Successfull")
    con.commit()
    con.close()
                                    
                                    
def loanapply():
    import sqlite3 as s
    con = s.connect("bankdet.db")
    cur = con.cursor()
    cur.execute(" SELECT * FROM BANK where ACC_NO = '%s' " %(acc_no.get()))
    res = cur.fetchall()
    for i in res:
            na = name.get()
            ac = acc_no.get()
            do = dob.get()
            ag = age.get()
            gen = gender.get()
            act = acc_type.get()
            aad = aadhar.get()
            pa = pan.get()
            mn = mobilenum.get()
            ltype  = loantype.get()
            lt = any(ltype)
            lam = loanamount.get()
            if i[0] == na and ac == i[1] and do == i[2] and ag == i[3]and gen == i[4] and act == i[6] and aad == i[7] and pa == i[8] and mn == i[11]  and lt == True:
                mb.showinfo("Alert","Dear Customer,\n\tYour Application Is Submitted Please Wait 10-20 Second's To Know Your Aplication Is Rejected Or Accepted So Kindly Please Wait 10-20 Second's")
                t.sleep(10)
                cur.execute( "INSERT INTO LOANAPPLY(NAME,ACC_NO,DOB,AGE,GENDER,ACC_TYPE,AADHAR,PAN,MOBILENUM,LOAN_TYPE,LOAN_AMT)VALUES('%s','%s','%s',%d,'%s','%s',%d,'%s',%d,'%s',%d)"%(
                                                                                                                                                                                                                                                     na,ac,do,ag,gen,act,aad,pa,mn,
                                                                                                                                                                                                                                                     ltype,lam))
                mb.showinfo("Congratulations","Dear  '%s'\n\t Your Loan Application Has Been Submitted Successfully"%(na))
            elif i[0] != na or ac != i[1] or do != i[2] or ag != i[3]or gen != i[4] or act != i[6] or aad != i[7] or pa != i[8] or mn != i[11]  or lt == True  :
                mb.showinfo("Alert","Dear Customer Your Given Detil's Are Not Matched With The Account Number You Given")
            elif lt==False:
                mb.showinfo("Alert ","Dear Customer Please Select Your Loan Type")
            elif i[0] != na or ac != i[1] or do != i[2] or ag != i[3]or gen != i[4] or act != i[6] or aad != i[7] or pa != i[8] or mn != i[11]  or lt == False  :
                mb.showinfo("Alert","Dear Customer Your Given Detil's Are Not Matched With The Account Number You Given")
            
    con.commit()
    con.close()
                        

def filldet():
    import sqlite3 as s
    con = s.connect("bankdet.db")
    cur = con.cursor()
    cur.execute(" SELECT * FROM BANK where ACC_NO = '%s' " %(acc_no.get()))
    res = cur.fetchall()
    for i in res:
        if acc_no.get()==i[1]:
                    name.set(res[0][0])
                    acc_no.set(res[0][1])
                    dob.set(res[0][2])
                    age.set(res[0][3])
                    gender.set(res[0][4])
                    aadhar.set(res[0][7])
                    acc_type.set(res[0][6])
                    pan.set(res[0][8])
                    mobilenum.set(res[0][11])
                    mb.showinfo("Alert","Dear Customer, \n \t All Your Detail's Are Filled Please Select Your Loan Type And  Please Enter The Loan Amount You Need And Then  Click 'Apply Loan' Button To Apply For Your Loan")
        else:
                mb.showinfo("Alert " ,"You Entered An Incorrect Account Number ")                    
    
    con.commit()
    con.close()

        
        

kj = Tk()
kj.title('Loan_Application')
fg1='orange'
fg='blue'
bg='white'
fnt1 = 'Copperplate Gothic Bold',40
fnt = 'Copperplate Gothic Bold',25
fnte = 'Copperplate Gothic Bold',20
kj.state('zoomed')
Label(kj,text = 'Loan Applicarion Form',fg=fg1,font=fnt1).place(x=295,y=25)
Label(kj,text='Name',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=150)
Label(kj,text='Account Number ',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=100)
Label(kj,text='Date Of Birth',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=200)
Label(kj,text='Age',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=250)
Label(kj,text='Gender',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=300)
Label(kj,text='Account Type',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=350)
Label(kj,text='Aadhar Number',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=400)
Label(kj,text='Pan Number',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=450)
Label(kj,text='Mobile  Number',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=500)
Label(kj,text='Loan Type',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=550)
Label(kj,text='Loan Amount',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=600)
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
loantype = StringVar()
loanamount = IntVar()
            
Entry(kj,textvariable=name,font=fnt,width=20).place(x=600,y = 150)
Entry(kj,textvariable=acc_no,font=fnt,width=20).place(x=600,y = 100)
Entry(kj,textvariable=dob,font=fnt,width=20).place(x=600,y = 200)
Entry(kj,textvariable=age,font=fnt,width=20).place(x=600,y = 250)
gender.set('MALE')
Radiobutton(kj,text='MALE',variable=gender,value='MALE',font=fnt).place(x=600,y=300)
Radiobutton(kj,text='FEMALE',variable=gender,value='FEMALE',font=fnt).place(x=850,y=300)
acc_type.set('SB')
Radiobutton(kj,text='SAVINGS',variable=acc_type,value='SB',font=fnt).place(x=600,y=350)
Radiobutton(kj,text='CURRENT',variable=acc_type,value='CUR',font=fnt).place(x=850,y=350)
Entry(kj,textvariable=aadhar,font=fnt,width=20).place(x=600,y = 400)
Entry(kj,textvariable=pan,font=fnt,width=20).place(x=600,y = 450)
Entry(kj,textvariable=mobilenum,font=fnt,width=20).place(x=600,y = 500)
loans = ['Gold Loan ','Education Loan','Vehicle Loan','Home Loan','Mobile Loan','Personal Loan','Car Finance','Buissness Loan']
OptionMenu(kj,loantype,*loans).place(x=600,y = 550)
Entry(kj,textvariable=loanamount,font=fnt,width=20).place(x=600,y = 600)

#Button's
Button(kj,text = "Apply Loan",fg=fg,bg=bg,font=fnte,width = 20,command = loanapply).place(x=350,y=650)
Button(kj,text = "Fill Details",fg=fg,bg=bg,font=fnte,width = 10,command = filldet).place(x=1100,y=100)

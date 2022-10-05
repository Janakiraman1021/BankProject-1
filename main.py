from tkinter import *
import tkinter.messagebox as mb
class butvar:
    opt=0

def create():
    import sqlite3
    conn = sqlite3.connect('bankdet.db')
    cur= conn.cursor()
    cur.execute("""CREATE TABLE BANK(
                            NAME VARCHAR(40),
                            ACC_NO VARCHAR(90),
                            DOB VARCHAR(90),
                            AGE INT,
                            GENDER VARCHAR(90),
                            COMMUNITY VARCHAR(90),
                            ACC_TYPE VARCHAR(90),
                            AADHAR INT,
                            PAN VARCHAR(90),
                            FNAME VARCHAR(90),
                            FOCC VARCHAR(90),
                            MOBILENUM INT,
                            ADDR VARCHAR(90),
                            DATE VARCHAR(90),
                            BALANCE INT);""")
    conn.commit()
    conn.close()
    mb.showinfo('Hello ')

def add():
    import sqlite3
    conn = sqlite3.connect('bankdet.db')
    cur= conn.cursor()
    if butvar.opt==1:
        cur.execute("""SELECT NUM FROM ACCNUM WHERE TYPE = '%s'""" %(acc_type.get()))
        res = cur.fetchall()
        up = res[0][0]
        up1 = int(up)        
        t=acc_type.get()
        if t=='SB':
            accnum='SB'+str(res[0][0])
        else:
            accnum='CUR'+str(res[0][0])
        curloan = 0
        cur.execute("""INSERT INTO BANK (NAME,ACC_NO,DOB,AGE,GENDER,COMMUNITY,ACC_TYPE,AADHAR,PAN,FNAME,FOCC,MOBILENUM,ADDR,DATE,BALANCE,CUR_LOAN) VALUES ('%s','%s','%s',%d,'%s','%s','%s',%d,'%s','%s','%s',%d,'%s','%s',%d,%d)"""%(name.get(),accnum,dob.get(),age.get(),gender.get(),community.get(),acc_type.get(),aadhar.get(),pan.get(),fname.get(),focc.get(),mobilenum.get(),addr.get(),date.get(),balance.get(),curloan))
        cur.execute("UPDATE ACCNUM SET NUM = %d where TYPE = '%s' " %(int(up1+1),acc_type.get()))        
        conn.commit()
        conn.close()
        Label(kj,text=accnum,font=fnt).place(x=500,y=150)
        mb.showinfo("Hello ","Your Account Added Successfully")
    elif butvar.opt==2:
        import sqlite3
        conn = sqlite3.connect('bankdet.db')
        cur= conn.cursor()
        cur.execute(""" UPDATE BANK SET NAME = '%s',
                                                                DOB = '%s',
                                                                AGE = %d,
                                                                GENDER = '%s',
                                                                COMMUNITY = '%s',
                                                                AADHAR = %d,
                                                                PAN = '%s',
                                                                FNAME = '%s',
                                                                FOCC = '%s',
                                                                MOBILENUM = %d,
                                                                ADDR = '%s'
                                                                where ACC_NO = '%s' """ %(name.get(),
                                                                                                              dob.get(),
                                                                                                              age.get(),
                                                                                                              gender.get(),
                                                                                                              community.get(),
                                                                                                              aadhar.get(),
                                                                                                              pan.get(),
                                                                                                              fname.get(),
                                                                                                              focc.get(),
                                                                                                              mobilenum.get(),
                                                                                                              addr.get(),
                                                                                                              acno))
        conn.commit()
        conn.close()
        mb.showinfo("Hello ","Your Account Updated Successfully")        

def new():
    butvar.opt=1

def show():
    global acno
    acno = accno.get()
    import sqlite3
    conn = sqlite3.connect('bankdet.db')
    cur= conn.cursor()
    cur.execute("""   SELECT * FROM BANK WHERE ACC_NO='%s'  """%(accno.get()))
    res = cur.fetchall()
    if any(res):
        name.set(res[0][0])
        acc_no.set(res[0][1])
        dob.set(res[0][2])
        age.set(res[0][3])
        gender.set(res[0][4])
        community.set(res[0][5])
        aadhar.set(res[0][7])
        pan.set(res[0][8])
        fname.set(res[0][9])
        focc.set(res[0][10])
        mobilenum.set(res[0][11])
        addr.set(res[0][12])
        date.set(res[0][13])
        balance.set(res[0][14])
    else:
        mb.showinfo("Alert","You Entered A Invalid Account Number")

def modify():
    butvar.opt=2
    global accno
    accno = StringVar()
    Label(kj,text='Enter Account Number',fg=fg,bg=bg,font=fnt).place(x=800,y=300)
    Entry(kj,textvariable=accno,font=fnt).place(x=1100,y=300)
    Button(kj,text='Show Details',command=show,font=fnt,fg='green',bg=bg).place(x=1050,y=350)

def clear():
    kj.destroy()


    
kj= Tk()
kj.state('zoomed')
kj.title('Account Details')
font_1='Gill sans MT  ',40,'bold'
fnt='Gill sans MT ',18
fg='Red'
bg='white'


# Label's
Label(kj,text='NEW ACCOUNT or MODIFY ACCOUNT',font=font_1,fg='blue').place(x=300,y=--15)
Label(kj,text='Name',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=100)
Label(kj,text='Account Number ',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=150)
Label(kj,text='Date Of Birth',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=200)
Label(kj,text='Age',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=250)
Label(kj,text='Gender',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=300)
Label(kj,text='Community',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=350)
Label(kj,text='Account Type',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=400)
Label(kj,text='Aadhar Number',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=450)
Label(kj,text='Pan Number',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=500)
Label(kj,text='Father Name',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=550)
Label(kj,text='Father Occupation',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=600)
Label(kj,text='Mobile Number',font=fnt,fg=fg,bg=bg,width = 20).place(x=100,y=650)
Label(kj,text='Address',font=fnt,fg=fg,bg=bg,width = 20).place(x=800,y=100)
Label(kj,text='Date Of Opening Account',font=fnt,fg=fg,bg=bg,width = 20).place(x=800,y=150)
Label(kj,text='Balance',font=fnt,fg=fg,bg=bg,width = 20).place(x=800,y=200)


# Variable Declaration's

name = StringVar()
acc_no=StringVar()
dob=StringVar()
age = IntVar()
gender = StringVar()
community  = StringVar()
acc_type=StringVar()
aadhar = IntVar()
pan = StringVar()
fname= StringVar()
focc = StringVar()
mobilenum = IntVar()
addr = StringVar()
date = StringVar()
balance = IntVar()


#Entry's

Entry(kj,textvariable=name,font=fnt,width=20).place(x=500,y = 100)
#Entry(kj,textvariable=acc_no,font=fnt,width=20).place(x=500,y = 150)
Entry(kj,textvariable=dob,font=fnt,width=20).place(x=500,y = 200)
Entry(kj,textvariable=age,font=fnt,width=20).place(x=500,y = 250)
#Entry(kj,textvariable=gender,font=fnt,width=20).place(x=500,y = 300)
Radiobutton(kj,text='MALE',variable=gender,value='MALE',font=fnt).place(x=500,y=300)
Radiobutton(kj,text='FEMALE',variable=gender,value='FEMALE',font=fnt).place(x=600,y=300)
#Entry(kj,textvariable=community,font=fnt,width=20).place(x=500,y = 350)
community.set('BC')
Radiobutton(kj,text='BC',variable=community,value='BC',font=fnt).place(x=500,y=350)
Radiobutton(kj,text='MBC',variable=community,value='MBC',font=fnt).place(x=600,y=350)
Radiobutton(kj,text='OC',variable=community,value='OC',font=fnt).place(x=700,y=350)
Radiobutton(kj,text='SC\ST',variable=community,value='SC\ST',font=fnt).place(x=800,y=350)
#Entry(kj,textvariable=acc_type,font=fnt,width=20).place(x=500,y = 400)
acc_type.set('SB')
Radiobutton(kj,text='SAVINGS',variable=acc_type,value='SB',font=fnt).place(x=500,y=400)
Radiobutton(kj,text='CURRENT',variable=acc_type,value='CUR',font=fnt).place(x=650,y=400)
Entry(kj,textvariable=aadhar,font=fnt,width=20).place(x=500,y = 450)
Entry(kj,textvariable=pan,font=fnt,width=20).place(x=500,y = 500)
Entry(kj,textvariable=fname,font=fnt,width=20).place(x=500,y = 550)
Entry(kj,textvariable=focc,font=fnt,width=20).place(x=500,y = 600)
Entry(kj,textvariable=mobilenum,font=fnt,width=20).place(x=500,y = 650)
Entry(kj,textvariable=addr,font=fnt,width=20).place(x=1100,y = 100)
Entry(kj,textvariable=date,font=fnt,width=20).place(x=1100,y = 150)
Entry(kj,textvariable=balance,font=fnt,width=20).place(x=1100,y = 200)



# Button's
fg='blue'
bg='white'
Button(kj,text='New Account',font=fnt,fg=fg,bg=bg,width=20,command=new).place(x=10,y=700)
Button(kj,text='Modify Account',font=fnt,fg=fg,bg=bg,width=20,command=modify).place(x=350,y=700)
Button(kj,text='Confirm',font=fnt,fg=fg,bg=bg,width=20,command=add).place(x=690,y=700)
Button(kj,text='Exit',font=fnt,fg=fg,bg=bg,width=20,command=clear).place(x=1000,y=700)

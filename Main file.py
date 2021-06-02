from Tkinter import *
from tkMessageBox import *
import sqlite3
def func(event):
	rootp.destroy()
	con=sqlite3.Connection('mydb')
	cur=con.cursor()
	cur.execute("create table if not exists users (username varchar(20) not null, password varchar(20) not null,score number(5));")
	root=Tk()
	root.title('IQ Test')
	f0=Frame(root,width=300,height=300,bg='lavender')
	wel=Frame(root,width=500,height=250,bg='lavender')
	f1=Frame(root,width=800,height=400,bg='lavender')
	f2=Frame(root,width=500,height=500,bg='lavender')
	f3=Frame(root,width=610,height=350,bg='lavender')
	f4=Frame(root,width=610,height=400,bg='lavender')
	f5=Frame(root,width=800,height=300,bg='lavender')
	f6=Frame(root,width=800,height=300,bg='lavender')
	f7=Frame(root,width=600,height=300,bg='lavender')
	f8=Frame(root,width=390,height=400,bg='lavender')
	f0.grid()
	f0.grid_propagate(0)
	wel.grid_propagate(0)
	f1.grid_propagate(0)
	f2.grid_propagate(0)
	f3.grid_propagate(0)
	f4.grid_propagate(0)
	f5.grid_propagate(0)
	f6.grid_propagate(0)
	f7.grid_propagate(0)
	f8.grid_propagate(0)

	Label(f0,text='IQ TESTER',padx=50,pady=15,font=(None,14),bg='lavender').grid(row=0,columnspan=2)
	Label(f0,text='Username:',padx=5,pady=5,font=(None,11),bg='lavender').grid(row=1,column=0)
	u=Entry(f0)
	u.grid(row=1,column=1)
	Label(f0,text='Password:',padx=5,pady=5,font=(None,11),bg='lavender').grid(row=2,column=0)
	p=Entry(f0,show='*')
	p.grid(row=2,column=1)
	def login():
	    if u.get()=='' or p.get()=='':
	        showerror('Error','Username or password cannot be blank')
	    else:
	        cur.execute("select * from users where username= ? and password =?",[(u.get()),(p.get())])
	        if cur.fetchall():
	            showinfo('Nice','Logged in success')
	            c0()
	        else:
	            showerror('Error','Username not found or password maybe incorrect')
	Button(f0,text='Login',padx=5,pady=5,font=(None,12),width=10,command=login,bg='lavender').grid(row=5,columnspan=2)
	Label(f0,text='Dont have an account? Sign up here!\nType new username and password in the text boxes\nand press Sign up',padx=5,pady=5,font=(None,9),bg='lavender').grid(row=6,columnspan=2)
	def reg():
	    if u.get()=='' or p.get()=='':
	        showerror('Error','Username or password cannot be blank')
	    else:
	        cur.execute("select * from users where username= ?",[(u.get())])
	        if cur.fetchall():
	            showerror('Error','Username already taken')
	        else:
	            showinfo('Nice!','Account created\nNow login!')
	            cur.execute("insert into users(username,password) values(?,?)",[(u.get()),(p.get())])
	            con.commit()
	            u.delete(0,'end')
	            p.delete(0,'end')
	Button(f0,text='Sign up',padx=5,pady=5,font=(None,12),width=10,command=reg,bg='lavender').grid(row=7,columnspan=2)
	def c0():
	    f0.grid_forget()
	    wel.grid()

	Label(wel,text='Hello ,Get ready for this exciting IQ test!',padx=75,pady=30,font=(None,14),bg='lavender').grid(row=0,columnspan=2)
	Label(wel,text='You can perform IQ test or check score if already performed once.!',padx=5,pady=5,font=(None,11),bg='lavender').grid(row=1,columnspan=2)
	def iq():
	    cur.execute("select score from users where username= ?",[(u.get())])
	    o=cur.fetchall()
	    if o[0][0] >=0:
	        showwarning('Oops','Seems like you have already performed IQ test once.\nCheck score')
	    else:
	    	iqt()
	Button(wel,text='IQ Test',padx=5,pady=5,width=15,font=(None,12),command=iq,bg='lavender').grid(row=2,column=0)
	def sc():
	    cur.execute("select score from users where username= ?",[(u.get())])
	    o=cur.fetchall()
	    if o[0][0]==None:
	        showwarning('Oops','You have not given any IQ test yet.!\nDo IQ test!')
	    else:
	        y=o[0][0]
	        if y>=200:
	            q='Genius or near genius'
	        elif y>=180 and y<200:
	            q='Superior intelligence'
	        elif y>=150 and y<180:
	            q='Intelligent'
	        elif y>=80 and y<150:
	            q='Normal or average intelligence'
	        elif y>=40 and y<80:
	            q='Dullness'
	        elif y<40:
	            q='Definite feeble-mindedness'
	        showinfo('Score','Your IQ is '+str(y)+'\nYou lie under '+q)
	        

	Button(wel,text='Check Score',padx=5,pady=5,width=15,font=(None,12),command=sc,bg='lavender').grid(row=2,column=1)
	Label(wel,text='Note: One user can perform IQ test only one time!',padx=5,pady=5,font=(None,10),bg='lavender').grid(row=3,columnspan=2)
	Button(wel,text='Exit',padx=3,pady=3,font=(None,11),command=root.destroy,bg='lavender',width=8).grid(row=4,column=1)
	def iqt():
	    wel.grid_forget()
	    f1.grid()
	Label(f1,text='Part 1 - Perception',padx=5,pady=20,font=(None,15),bg='lavender').grid(row=0,columnspan=2)
	Label(f1,text='This test deals with sets of numbers and letters. Each number set has one number missing from 0 to 9.',padx=5,pady=5,font=(None,11),bg='lavender').grid(row=1,columnspan=2)
	Label(f1,text='Find the number and enter it in the space at the right. Each set of letters has one letter that appears twice.',padx=5,pady=5,font=(None,11),bg='lavender').grid(row=2,columnspan=2)
	Label(f1,text='Find the duplicate letter and enter it in the space at the right.\n\nFor Example:',justify="left",padx=5,pady=5,font=(None,11),bg='lavender').grid(row=3,column=0)
	Label(f1,text=' 460328597 	 1',padx=5,pady=5,font=(None,14),bg='lavender').grid(row=5,column=0)
	Label(f1,text='APEXCLATHON   A',padx=5,pady=5,font=(None,14),bg='lavender').grid(row=5,column=1)
	Label(f1,text='The number 1 is missing from the number set.',padx=5,pady=5,font=(None,11),bg='lavender').grid(row=6,column=0)
	Label(f1,text='The letter A appears twice in the letter set.',padx=5,pady=25,font=(None,11),bg='lavender').grid(row=6,column=1)
	def c1():
	    f1.grid_forget()
	    f2.grid()
	    f1.after(60000,c2)
	Button(f1,text='Next',padx=5,pady=5,command=c1,width=12,font=(None,12),bg='lavender').grid(row=7,columnspan=2)
	Label(f1,text='Note: You will have 1 minute to complete this test. Click next when ready.',padx=5,pady=5,font=(None,11),bg='lavender').grid(row=8,column=0)
	Label(f2,text='Start now you have 1 minute.',padx=120,pady=25,font=(None,14),bg='lavender').grid(row=0,columnspan=4)
	Label(f2,text='802941673',padx=3,pady=2,font=(None,11),bg='lavender').grid(row=1,column=1)
	Label(f2,text='BJXQRMZWNQP',padx=3,pady=2,font=(None,11),bg='lavender').grid(row=2,column=1)
	Label(f2,text='128309674',padx=3,pady=3,font=(None,11),bg='lavender').grid(row=3,column=1)
	Label(f2,text='WKLJSKRUAXE',padx=3,pady=3,font=(None,11),bg='lavender').grid(row=4,column=1)
	Label(f2,text='879201563',padx=3,pady=3,font=(None,11),bg='lavender').grid(row=5,column=1)
	Label(f2,text='JXZAOWNJMVB',padx=3,pady=3,font=(None,11),bg='lavender').grid(row=6,column=1)
	Label(f2,text='861459032',padx=3,pady=3,font=(None,11),bg='lavender').grid(row=7,column=1)
	Label(f2,text='FDKCTOZUONP',padx=3,pady=3,font=(None,11),bg='lavender').grid(row=8,column=1)
	Label(f2,text='605294371',padx=3,pady=3,font=(None,11),bg='lavender').grid(row=9,column=1)
	Label(f2,text='FXEAUBGOFZV',padx=3,pady=3,font=(None,11),bg='lavender').grid(row=10,column=1)
	Label(f2,text='269183504',padx=3,pady=3,font=(None,11),bg='lavender').grid(row=11,column=1)
	Label(f2,text='WODIHAGQJAN',padx=3,pady=3,font=(None,11),bg='lavender').grid(row=12,column=1)
	Label(f2,text='953621478',padx=3,pady=3,font=(None,11),bg='lavender').grid(row=13,column=1)
	Label(f2,text='SZNXIVLPSDE',padx=3,pady=3,font=(None,11),bg='lavender').grid(row=14,column=1)
	Label(f2,text='851293764',padx=3,pady=3,font=(None,11),bg='lavender').grid(row=15,column=1)
	e1=[Entry(f2,width=7) for _ in range(15)]
	for i in range(15):
	    e1[i].grid(row=i+1,column=2,ipadx=0)
	b1=0
	def c2():
	    ans1=['5','Q','5','K','4','J','7','O','8','F','7','A','0','S','0']
	    f2.grid_forget()
	    f3.grid()
	    for i in range(10):
	        if str(e1[i].get())==str(ans1[i]):
	            b1=b1+1    
	Label(f3,text='Part 2 - Logical Reasoning',padx=5,pady=20,font=(None,15),bg='lavender').grid(row=0,columnspan=2)
	Label(f3,text='In each set below you are to insert the next number of the sequence in the blank space.',padx=5,pady=5,font=(None,12),bg='lavender').grid(row=1,columnspan=2)
	Label(f3,text='For Example-',padx=0,pady=5,font=(None,11),bg='lavender').grid(row=2,column=0)
	Label(f3,text='1  5  2  6  3  7  4 __ 	Answer-8',justify="left",padx=5,pady=20,font=(None,14),bg='lavender').grid(row=3,columnspan=2)
	def c3():
	    f3.grid_forget()
	    f4.grid()
	    f3.after(60000,c4)
	Button(f3,text='Next',command=c3,padx=5,pady=5,width=15,font=(None,12),bg='lavender').grid(row=6,columnspan=2)
	Label(f3,text='NOTE: The key to these problems is to break down each set of numbers\ninto groups until you observe a pattern or relationship between them.\nYou will have 1 minute to complete this test.Click Next when ready.',padx=5,pady=5,font=(None,10),bg='lavender').grid(row=7,columnspan=2)
	Label(f4,text='Insert the next item of the sequence in the blank space.',padx=75,pady=25,font=(None,14),bg='lavender').grid(row=0,columnspan=5)
	Label(f4,text='1   3   5   7',padx=3,pady=3,font=(None,11),bg='lavender').grid(row=1,column=1)
	Label(f4,text='2   5   9   14',padx=3,pady=3,font=(None,11),bg='lavender').grid(row=2,column=1)
	Label(f4,text='10   5   8   4   6',padx=3,pady=3,font=(None,11),bg='lavender').grid(row=3,column=1)
	Label(f4,text='3   3   9   8   4   4   16   15   5   5   25',padx=3,pady=3,font=(None,11),bg='lavender').grid(row=4,column=1)
	Label(f4,text='81   27   9   3',padx=3,pady=3,font=(None,11),bg='lavender').grid(row=5,column=1)
	Label(f4,text='25   5   16   4   9',padx=3,pady=3,font=(None,11),bg='lavender').grid(row=6,column=1)
	Label(f4,text='9   5   6   8   4   5   7   3',padx=3,pady=3,font=(None,11),bg='lavender').grid(row=7,column=1)
	Label(f4,text='2   3   5   3   4   7   4   5',padx=3,pady=3,font=(None,11),bg='lavender').grid(row=8,column=1)
	Label(f4,text='2   13   4   11   6   9',padx=3,pady=3,font=(None,11),bg='lavender').grid(row=9,column=1)
	Label(f4,text='16   4   2   25   5   3   36   6',padx=3,pady=3,font=(None,11),bg='lavender').grid(row=10,column=1)
	e2=[Entry(f4,width=5) for _ in range(10)]
	for i in range(10):
	    e2[i].grid(row=i+1,column=2,ipadx=0)
	b2=0
	def c4():
	    ans2=[9,20,3,24,1,3,4,9,8,4]
	    f4.grid_forget()
	    f5.grid()
	    for i in range(10):
	        if str(e2[i].get())==str(ans2[i]):
	            b2=b2+1
	Label(f5,text='Part 3 - Memory',padx=5,pady=20,font=(None,15),bg='lavender').grid(row=0,columnspan=2)
	Label(f5,text='When you click on the next button below you will find 6 different symbols with an assigned number under each symbol.',padx=5,pady=5,font=(None,11),bg='lavender').grid(row=1,columnspan=2)
	Label(f5,text='Study them carefully and concentrate.Try to remember the assigned number that belongs with each symbol.',padx=5,pady=5,font=(None,11),bg='lavender').grid(row=2,columnspan=2)
	Label(f5,text='After 30 seconds the symbols will disappear and will appear again in a different order.\nWrite the correct assigned number in the blank spaces below each symbol.\nYou will have 30 seconds to do this also.',padx=5,pady=5,font=(None,11),bg='lavender').grid(row=3,columnspan=2)
	def c5():
	    f5.grid_forget()
	    f6.grid()
	    f5.after(30000,c6)
	Button(f5,text='Next',command=c5,padx=5,pady=5,width=15,font=(None,12),bg='lavender').grid(row=4,columnspan=2)
	Label(f5,text='NOTE! You must memorize what number belongs to each symbol because the symbols will not appear in the same sequence again.\n',padx=5,pady=5,font=(None,10),bg='lavender').grid(row=5,columnspan=2)
	Label(f6,text='Start you have 30 seconds to memorize these symbols and numbers.',padx=100,pady=50,font=(None,14),bg='lavender').grid(row=0,columnspan=2)
	Label(f6,text='@	%	&	?	!	#',padx=5,pady=7,font=(None,14),bg='lavender').grid(row=1,columnspan=2)
	Label(f6,text='4 	7	2	9	3	5',padx=5,pady=7,font=(None,14),bg='lavender').grid(row=2,columnspan=2)
	def c6(): 
	    f6.grid_forget()
	    f7.grid()
	    f6.after(30000,c7)
	Label(f7,text='You have 30 seconds to submit',padx=150,pady=25,font=(None,14),bg='lavender').grid(row=0,columnspan=4)
	Label(f7,text='#',padx=5,pady=3,font=(None,15),bg='lavender').grid(row=1,column=1)
	Label(f7,text='%',padx=5,pady=3,font=(None,15),bg='lavender').grid(row=2,column=1)
	Label(f7,text='?',padx=5,pady=3,font=(None,15),bg='lavender').grid(row=3,column=1)
	Label(f7,text='@',padx=5,pady=3,font=(None,15),bg='lavender').grid(row=4,column=1)
	Label(f7,text='!',padx=5,pady=3,font=(None,15),bg='lavender').grid(row=5,column=1)
	Label(f7,text='&',padx=5,pady=3,font=(None,15),bg='lavender').grid(row=6,column=1)

	e3=[Entry(f7,width=5) for _ in range(6)]
	for i in range(6):
	    e3[i].grid(row=i+1,column=2)
	b3=0
	def c7():
	    ans3=[5,7,9,4,3,2]
	    f7.grid_forget()
	    f8.grid()
	    for i in range(6):
	        if str(e3[i].get())==str(ans3[i]):
	            b3=b3+1
	Label(f8,text='Result!',padx=50,pady=15,font=(None,16),bg='lavender').grid(row=0,columnspan=2)
	Label(f8,text='The rating system of this test is as follows-',padx=5,pady=5,font=(None,14),bg='lavender').grid(row=1,column=0)
	Label(f8,text='Above 200 - Genius or near genius',padx=5,pady=5,font=(None,10),bg='lavender').grid(row=2,column=0)
	Label(f8,text='180 - 200 - Superior intelligence',padx=5,pady=5,font=(None,10),bg='lavender').grid(row=3,column=0)
	Label(f8,text='150 - 180 -Intelligent',padx=5,pady=5,font=(None,10),bg='lavender').grid(row=4,column=0)
	Label(f8,text='80 - 150 - Normal or average intelligence',padx=5,pady=5,font=(None,10),bg='lavender').grid(row=5,column=0)
	Label(f8,text='40 - 80 - Dullness',padx=5,pady=5,font=(None,10),bg='lavender').grid(row=6,column=0)
	Label(f8,text='Under 40 - Definite feeble-mindedness',padx=5,pady=5,font=(None,10),bg='lavender').grid(row=7,column=0)
	def c8():
	    b=b1+b2+b3
	    b=b*10
	    cur.execute("update users set score=? where username=?",[b,(u.get())])
	    con.commit()
	    if b>=200:
	        s='Genius or near genius'
	    elif b>=180 and b<200:
	        s='Superior intelligence'
	    elif b>=150 and b<180:
	        s='Intelligent'
	    elif b>=80 and b<150:
	        s='Normal or average intelligence'
	    elif b>=40 and b<80:
	        s='Dullness'
	    elif b<40:
	        s='Definite feeble-mindedness'
	    showinfo('Score','Your IQ is '+str(b)+'\nYou lie under '+s)
	    xd.grid_forget()
	    def yo():
	        f8.grid_forget()
	        f0.grid()
	        u.delete(0,'end')
	        p.delete(0,'end')
	    Button(f8,text='Back to Login',command=yo,padx=5,pady=5,font=(None,11),width=15,bg='lavender').grid(row=8,columnspan=2)
	    Label(f8,text='',pady=10,bg='lavender').grid(row=9,column=0)
	    Button(f8,text='Exit',padx=3,pady=3,font=(None,11),command=root.destroy,bg='lavender',width=8).grid(row=10,column=0)
	    
	xd=Button(f8,text='Score',command=c8,padx=5,pady=5,font=(None,11),width=8,bg='lavender')
	xd.grid(row=8,columnspan=2)
	root.mainloop()

rootp=Tk()
rootp.configure(background='seashell2')
Label(rootp,text='Bharat Hasija',font=(None,12),width=25,bg='seashell2',fg='DeepSkyBlue4').grid(row=0,column=0,columnspan=2)
Label(rootp,text='',bg='seashell2').grid(row=1,column=0)
Label(rootp,text='Enrollment No',font=(None,12),bg='seashell2',fg='gray2').grid(row=2,column=0)
Label(rootp,text='171B167',font=(None,12),bg='seashell2',fg='gray2').grid(row=2,column=1)

Label(rootp,text='Batch',font=(None,12),bg='seashell2',fg='gray2').grid(row=3,column=0)
Label(rootp,text='B5',font=(None,12),bg='seashell2',fg='gray2').grid(row=3,column=1)

Label(rootp,text='Email Id',font=(None,12),bg='seashell2',fg='gray2').grid(row=4,column=0)
Label(rootp,text='bharathasija6@gmail.com',font=(None,12),bg='seashell2',fg='gray2').grid(row=4,column=1)

Label(rootp,text='Phone Number',font=(None,12),bg='seashell2',fg='gray2').grid(row=5,column=0)
Label(rootp,text='9935975955',font=(None,12),bg='seashell2',fg='gray2').grid(row=5,column=1)

Label(rootp,text='',bg='seashell2').grid(row=6,column=0)
rootp.bind('<Motion>',func)
rootp.mainloop()

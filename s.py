from tkinter import *

def check():
    clrMessage()
    f=open("Car_db.txt",'a')
    x1=s1.get()     # car_id
    x2=s2.get()     # car_name
    x3=s3.get()     # colour
    x4=s4.get()     # seater
    x5=a1.get()     # price
    if(x1!="" and x2!="" and x3!="" and x4!="" and x5!=""):
        f.writelines(x1.ljust(20)+x2.ljust(20)+x3.ljust(20)+x4.ljust(20)+x5.ljust(3)+'\n')
        print('Record added!!')
    else:
        clr()
        a2.set("Please enter required details of CAR!!! ")
   

count=0
def prev_rec():
    clrMessage()
    f=open("Car_db.txt",'r')
    global count
    count=count-1
    i=0
    try:
        while(i<=count-1):
            l1=f.readline()
            i=i+1                
        l2=l1.split()
        s1.set(l2[0])
        s2.set(l2[1])
        s3.set(l2[2])
        s4.set(l2[3])
        a1.set(l2[4])
    except (UnboundLocalError,IndexError):
        clr()
        a2.set("You have searched whole database"+"\n"+"Press CLR!!!!")
    f.close()    
        

def next_rec():
    clrMessage()
    f=open("Car_db.txt",'r')
    global count
    i=0
    try:
        while(i<=count):
            l1=f.readline()
            i=i+1
  
        l2=l1.split()    
        s1.set(l2[0])
        s2.set(l2[1])
        s3.set(l2[2])
        s4.set(l2[3])
        a1.set(l2[4])
        print(l1)
        count=count+1
    except (IndexError,UnboundLocalError):
        clr()
        a2.set("No more records in database"+"\n"+" press CLR or > to start again!!!")
    f.close()    

        
def clr():
    global count
    count=0
    l1=""
    s1.set(l1)
    s2.set(l1)
    s3.set(l1)
    s4.set(l1)
    a1.set(l1)
    a2.set(l1)

def clrMessage():
    l1=""
    a2.set(l1)


def search():
    clrMessage()
    x=s1.get()  # Searching element
    print("Searched car_Id : "+x)
    f=open('Car_db.txt','r')
    line=f.readlines()
    
    for l1 in line:
        l2=l1.split()
        if(x==l2[0]):
            print(l1)
            print(l2)
            s1.set(l2[0])
            s2.set(l2[1])
            s3.set(l2[2])
            s4.set(l2[3])
            a1.set(l2[4])
            
    f.close()


def delete():
    clrMessage()
    f=open("Car_db.txt","r")
    x=[s1.get(),s2.get(),s3.get(),s4.get(),a1.get()]
    print(x)
    line=f.readlines()
    f.close()
    f=open("Car_db.txt","w")
    for l1 in line:
        l2=l1.split()
        if(l2[0]!=x[0]):
             f.writelines(l2[0].ljust(20)+l2[1].ljust(20)+l2[2].ljust(20)+l2[3].ljust(20)+l2[4].ljust(3)+"\n")
    f.close()


def update():
    x1=s1.get()
    x2=s2.get()
    x3=s3.get()
    x4=s4.get()
    x5=a1.get()
    f=open("Car_db.txt","r")
    line=f.readlines()
    f.close()
    f=open("Car_db","w")
    for l1 in line:
        l2=l1.split()
        if(l2[0]!=x1):
            f.writelines(l2[0].ljust(20)+l2[1].ljust(20)+l2[2].ljust(20)+l2[3].ljust(20)+l2[4].ljust(3)+"\n")
    
        else:
            f.writelines(l2[0].ljust(20)+x2.ljust(20)+x3.ljust(20)+x4.ljust(20)+x5.ljust(3)+"\n")
    f.close()
   



root=Tk()
root.title("Car Databases")
# marquee=MARQUEE(root,text="car database",height=1,width=20)
# marquee.pack()

c1=Canvas(root,height=500,width=500)
c1.pack(side=BOTTOM)

#i1=PhotoImage(file="car7.png")
#image=c1.create_image(450,20,anchor=NE,image=i1)

lbl=Label(root,font=('Segoe Script',30,'bold','italic'),text='BBT BigBoyToyz!!!',fg='steel blue',bg='black')
lbl.pack()

c1.pack()
'''
f1=Frame(root,width=200,height=50,bg='powder blue',relief=SUNKEN)
f1.pack(side=TOP)
lbl=Label(f1,font=('arial',20,'bold','italic'),text='Car Database',fg='steel blue')
lbl.pack()
'''
l1=Label(root,text="CarId :",font=('arial',12,'bold','italic'))
l2=Label(root,text="CarName :",font=('arial',12,'bold','italic'))
l3=Label(root,text="Colour :",font=('arial',12,'bold','italic'))
l4=Label(root,text="Seater :",font=('arial',12,'bold','italic'))
l5=Label(root,text="Price $ :",font=('arial',12,'bold','italic'))

l1.place(x=20,y=80)
l2.place(x=20,y=120)
l3.place(x=20,y=160)
l4.place(x=20,y=200)
l5.place(x=20,y=240)

s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
a1=StringVar()

t1=Entry(root,text=s1)
t2=Entry(root,text=s2)
t3=Entry(root,text=s3)
t4=Entry(root,text=s4)
t5=Entry(root,text=a1)

t1.place(x=110,y=80)
t2.place(x=110,y=120)
t3.place(x=110,y=160)
t4.place(x=110,y=200)
t5.place(x=110,y=240)


a2=StringVar()
m1=Message(root,textvariable=a2,relief=RAISED,fg='black',font=('arial','10'))
m1.place(x=110,y=270)

b1=Button(root,text="ADD",command=check,bg="black",fg='white',font=('arial','10'))
b1.place(x=150,y=350,width=100,height=30)

b2=Button(root,text="<",bg="black",fg='white',font=('arial','40','bold'),command=prev_rec)
b2.place(x=40,y=350,width=100,height=30)

b3=Button(root,text=">",bg="black",fg='white',font=('arial','40','bold'),command=next_rec)
b3.place(x=260,y=350,width=100,height=30)

b4=Button(root,text="CLR",bg="black",fg='white',font=('arial','10'),command=clr)
b4.place(x=40,y=400,width=100,height=30)

b5=Button(root,text="SEARCH",bg="black",fg='white',font=('arial','10'),command=search)
b5.place(x=150,y=400,width=100,height=30)

b6=Button(root,text="DELETE",bg="black",fg='white',font=('arial','10'),command=delete)
b6.place(x=260,y=400,width=100,height=30)

b7=Button(root,text="UPDATE",bg="black",fg='white',font=('arial','15'),command=update)
b7.place(x=40,y=450,width=320,height=30)


root.mainloop()




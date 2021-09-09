from tkinter import *
from tkinter import messagebox
root=Tk()
def getvals():
    print("Accepted")
root.geometry("900x900")
root.title("MARKSHEET")
msg="STUDENT MARKS DETALIS"
msg=Message(root,text=msg)
msg.config(fg="purple",width=1000)
msg.pack()

root.configure(background="lightBlue")

l1=Label(root,text="First Name:").place(x=500,y=100)
l2=Label(root,text="Last Name:").place(x=1000,y=100)
l3=Label(root,text="Fathers Name:").place(x=500,y=130)
l4=Label(root,text="Mother's Name:").place(x=1000,y=130)
l5=Label(root,text="Address:").place(x=500,y=160)
l6=Label(root,text="State:").place(x=1000,y=160)
l7=Label(root,text="Phone Number:").place(x=500,y=270)
l8=Label(root,text="City:").place(x=1000,y=270)


e1=Entry(root,width=30).place(x=675,y=100)
e2=Entry(root,width=30).place(x=1175,y=100)

e3=Entry(root,width=30).place(x=675,y=130)
e4=Entry(root,width=30).place(x=1175,y=130)
e5=Entry(root,width=30).place(x=675,y=160,height=100)
e6=Entry(root,width=30).place(x=1175,y=160)
e7=Entry(root,width=30).place(x=675,y=270)


l9=Label(root,text="Gender").place(x=500,y=300)
r1=Radiobutton(root,text="Male",value=1).place(x=675,y=300)
r2=Radiobutton(root,text="female",value=2).place(x=800,y=300)

var=StringVar()
om1=OptionMenu(root,var,"dehradun","Maassorie","HAridwar","Rishikesh","Roorkee").place(x=1175,y=270)
l8=Label(root,text="MARKS OF THE STUDENT",fg="red").place(x=820,y=400)

l10=Label(root,text="Maths").place(x=500,y=500)
l11=Label(root,text="Science").place(x=500,y=550)
l12=Label(root,text="Hindi").place(x=500,y=600)
l13=Label(root,text="English").place(x=500,y=650)
l14=Label(root,text="Computer").place(x=500,y=700)

e8=Entry(root,width=30)
e8.place(x=675,y=500,height=30)
e9=Entry(root,width=30)
e9.place(x=675,y=550,height=30)
e10=Entry(root,width=30)
e10.place(x=675,y=600,height=30)
e11=Entry(root,width=30)
e11.place(x=675,y=650,height=30)
e12=Entry(root,width=30)
e12.place(x=675,y=700,height=30)
#e13=Entry(root,width=30)
#e13.place(x=675,y=700,height=30)

l15=Label(root,text="Total").place(x=900,y=500)
l15=Label(root,text="Avg").place(x=900,y=550)
l15=Label(root,text="Result").place(x=900,y=600)
#l15=Label(root,txt="div").place(x=900,y=650)

class Total():
    def total(self):
        self.add=int(e8.get())+int(e9.get())+int(e10.get())+int(e11.get())+int(e12.get())
        Sum.set(self.add)

class Avg(Total):
    def avg(self):
        self.avg=self.add/5
        average.set(self.avg)

class Result(Avg):
    def result(self):
        if(self.avg>90 and self.avg<=100):
            res.set("A+")
        if(self.avg>80 and self.avg<=90):
            res.set("A")
        if(self.avg>70 and self.avg<=80):
            res.set("B+")
        if(self.avg>60 and self.avg<=70):
            res.set("B")
        if(self.avg>50 and self.avg<=60):
            res.set("C+")
        if(self.avg>40 and self.avg<=50):
            res.set("D")
        if(self.avg<40):
            res.set("Fail")

fn=Result()
Sum=StringVar()
average=StringVar()
res=StringVar()

b1=Button(root,text="total",fg='red',command=fn.total).place(x=1200,y=500)
b2=Button(root,text="Average",fg="red",command=fn.avg).place(x=1200,y=550)
b3=Button(root,text="Result",fg="red",command=fn.result).place(x=1200,y=600)

l16=Label(root,text="",textvariable=Sum).place(x=1100,y=500)
l17=Label(root,text="",textvariable=average).place(x=1100,y=550)
l18=Label(root,text="",textvariable=res).place(x=1100,y=600)
sbmitbtn=Button(root,text="Submit",activebackground="black",activeforeground="blue",command=getvals()).place(x=750,y=750)
#messagebox.askquestion("confirm","DO you want to save your file")

root.mainloop()






















































from this import d
from tkinter import *
import random
import time

from werkzeug.datastructures import Range
from collections import defaultdict
root = Tk()
root.geometry("1500x700+0+0")
root.title("Restaurant Management System")

Tops=Frame(root,width=1600,height = 50, bg = "powder blue", relief = SUNKEN)
Tops.pack(side=TOP)
f1=Frame(root,width=800,height = 700, bg = "powder blue", relief = SUNKEN)
f1.pack(side=LEFT)
f2=Frame(root,width=300,height = 700, bg = "powder blue", relief = SUNKEN)
f2.pack(side=RIGHT)
#==================time-----------------------
localtime=time.asctime(time.localtime(time.time()))
#================Info-----------------------
lblinfo = Label(Tops, font=('arial', 50,'bold'), text = "Restaurant Management System",fg="steel blue",bd=10,anchor='s')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=('arial', 20,'bold'), text = localtime,fg="steel blue",bd=10,anchor='s')
lblinfo.grid(row=1,column=0)
#==================Calculator------------------
txtInput=StringVar()
operator=""
def btnClick(number):
    global operator
    operator=operator+str(number)
    txtInput.set(operator)
def btnClearDisply():
    global operator
    operator=""
    txtInput.set(operator)
def btnEqualDisply():
    global operator
    sumup = str(eval(operator))
    txtInput.set(sumup)
    operator=sumup
txtDisplay=Entry(f2,font=('arial',20,'bold'),textvariable=txtInput,bd=30 , insertwidth=4,
                 bg='powder blue', justify=RIGHT)
txtDisplay.grid(columnspan=4)

btn7= Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="7",bg="powder blue",command= lambda: btnClick(7)).grid(row=2,column=0)
btn8= Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="8",bg="powder blue",command= lambda: btnClick(8)).grid(row=2,column=1)
btn9= Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="9",bg="powder blue",command= lambda: btnClick(9)).grid(row=2,column=2)
btnAdd= Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="+",bg="powder blue",command= lambda: btnClick("+")).grid(row=2,column=3)

btn4= Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="4",bg="powder blue",command= lambda: btnClick(4)).grid(row=3,column=0)
btn5= Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="5",bg="powder blue",command= lambda: btnClick(5)).grid(row=3,column=1)
btn6= Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="6",bg="powder blue",command= lambda: btnClick(6)).grid(row=3,column=2)
btnSub= Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="-",bg="powder blue",command= lambda: btnClick("-")).grid(row=3,column=3)

btn1= Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="1",bg="powder blue",command= lambda: btnClick(1)).grid(row=4,column=0)
btn2= Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="2",bg="powder blue",command= lambda: btnClick(2)).grid(row=4,column=1)
btn3= Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="3",bg="powder blue",command= lambda: btnClick(3)).grid(row=4,column=2)
btnMul= Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="*",bg="powder blue",command= lambda: btnClick("*")).grid(row=4,column=3)

btn0= Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="0",bg="powder blue",command= lambda: btnClick(0)).grid(row=5,column=1)
btnEqual= Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="=",bg="powder blue",command= lambda: btnEqualDisply()).grid(row=5,column=2)
btnDiv= Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="/",bg="powder blue",command= lambda: btnClick("/")).grid(row=5,column=3)
btnClear= Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="C",bg="powder blue",command= lambda: btnClearDisply()).grid(row=5,column=0)
n=0
for labs in ("Reference","Large Fries","Burger Meal","Fish Meal","Chicken Meal","Cheese Meal"):
    Label(f1, font=('arial', 20, 'bold'), text=labs, fg="steel blue", bd=10, anchor='s').grid(row=n, column=0)
    n=n+1
r=0
for labs in ("Drinks","Cost of Meal","CGST","SGST","Total Cost"):
    Label(f1, font=('arial', 20, 'bold'), text=labs, fg="steel blue", bd=10, anchor='s').grid(row=r, column=3)
    r=r+1


    rand = StringVar()
    Entry(f1, font=('arial', 15, 'bold'), textvariable=rand, bd=10, insertwidth=2,
                       bg='powder blue', justify=RIGHT).grid(row=0, column=1)
    fries= StringVar()
    Entry(f1, font=('arial', 15, 'bold'), textvariable=fries, bd=10, insertwidth=2,
                       bg="#ffffff", justify=RIGHT).grid(row=1, column=1)

    Burger = StringVar()
    Entry(f1, font=('arial', 15, 'bold'), textvariable=Burger, bd=10, insertwidth=2,
          bg="#ffffff", justify=RIGHT).grid(row=2, column=1)
    Fish = StringVar()
    Entry(f1, font=('arial', 15, 'bold'), textvariable=Fish, bd=10, insertwidth=2,
          bg="#ffffff", justify=RIGHT).grid(row=3, column=1)
    Chicken = StringVar()
    Entry(f1, font=('arial', 15, 'bold'), textvariable=Chicken, bd=10, insertwidth=2,
          bg="#ffffff", justify=RIGHT).grid(row=4, column=1)
    Cheese = StringVar()
    Entry(f1, font=('arial', 15, 'bold'), textvariable=Cheese, bd=10, insertwidth=2,
          bg="#ffffff", justify=RIGHT).grid(row=5, column=1)
    Drink = StringVar()
    Entry(f1, font=('arial', 15, 'bold'), textvariable=Drink, bd=10, insertwidth=2,
          bg="#ffffff", justify=RIGHT).grid(row=0, column=4)
    TotalCost = StringVar()
    Entry(f1, font=('arial', 15, 'bold'), textvariable=TotalCost, bd=10, insertwidth=2,
          bg="#ffffff", justify=RIGHT).grid(row=1, column=4)


    Cgst = StringVar()
    Entry(f1, font=('arial', 15, 'bold'), textvariable=Cgst, bd=10, insertwidth=2,
          bg="#ffffff", justify=RIGHT).grid(row=2, column=4)
    Sgst = StringVar()
    Entry(f1, font=('arial', 15, 'bold'), textvariable=Sgst, bd=10, insertwidth=2,
          bg="#ffffff", justify=RIGHT).grid(row=3, column=4)
    Finalbill = StringVar()
    Entry(f1, font=('arial', 15, 'bold'), textvariable=Finalbill, bd=10, insertwidth=2,
          bg="#ffffff", justify=RIGHT).grid(row=4, column=4)

def sumcost():
    x= random.randint(12345,99999)
    randref=str(x)
    rand.set(x)
    Cof = float(fries.get())
    CoB = float(Burger.get())
    Cofi = float(Fish.get())
    Cochi = float(Chicken.get())
    Coche = float(Cheese.get())
    CoD= float(Drink.get())

    CostofFries = Cof*59
    CostofBurger = CoB * 50
    CostofFish= Cofi * 150
    Costofchicken = Cochi * 110
    Costofcheese = Coche*70
    CostofDrink = CoD*30

    FinalCost = "Rs.",str('%.2f'% (CostofDrink + CostofFries + CostofBurger + Costofcheese + Costofchicken + CostofFish))
    TotalCost.set(FinalCost)
    cg = (CostofDrink + CostofFries + CostofBurger + Costofcheese + Costofchicken + CostofFish)*0.025
    Cgst.set(cg)
    sg = (CostofDrink + CostofFries + CostofBurger + Costofcheese + Costofchicken + CostofFish)*0.025
    Sgst.set(sg)
    fbill="Rs.",str('%.2f'% (CostofDrink + CostofFries + CostofBurger + Costofcheese + Costofchicken + CostofFish+cg+sg))
    Finalbill.set(fbill)

def exitfn():
    root.destroy()

def clearfn():
    rand.set("")
    fries.set("")
    Drink.set("")
    Burger.set("")
    Fish.set("")
    Chicken.set("")
    Cheese.set("")
    TotalCost.set("")
    Cgst.set("")
    Sgst.set("")
    Finalbill.set("")


TotalButton= Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="Total",bg="powder blue",command= lambda: sumcost()).grid(row=6,column=1)
ExitBtn= Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="Exit",bg="powder blue",command= lambda: exitfn()).grid(row=6,column=2)
ClearBtn= Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
        text="Clear",bg="powder blue",command= lambda: clearfn()).grid(row=6,column=3)

root.mainloop()
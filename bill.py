from tkinter import *
from tkinter import messagebox as tmsg
from datetime import datetime, date
import random
import os
import tempfile
root=Tk()

def message():
    a=tmsg.askokcancel("Retail Management", "Do you want to exit ?")
    if a==True:
        root.destroy()


def printdate():
    today=date.today()
    return(today.strftime("%d/%m/%Y"))

#.............................Save bill.....................................................
def savefile():
    a=tmsg.askyesno("Retail Management","Do you want to save you bill ?")
    if a==True:
        billdata=textarea.get('1.0', END)
        f=open(f"Bills/{billnovar.get()}"+".txt","w")
        f.write(billdata)
        f.close()
        tmsg.showinfo("Retail Management", f"Bill no {billnovar.get()} has saved successfully")

#...............................Print the bill.............................................
def print():
    a=tmsg.askyesno("Retail Management","Do you want to print the bill?")
    if a==True:
        q=textarea.get('1.0',END)
        filename=tempfile.mktemp(".txt")
        f=open(filename,"w")
        f.write(q)
        os.startfile(filename ,"print")

#.......Price list...................
def PriceList():
    top=Toplevel()
    w=500
    h=500
    ws=top.winfo_screenwidth()          #Screen Width and Screen Height...........
    hs=top.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    top.geometry('%dx%d+%d+%d' %(w,h,x,y))
    top.iconbitmap(r'C:\Users\umang\Downloads\favicon2.ico')
    top.title("Price List")
    top.maxsize(height=380,width=300)
    my_list=Listbox(top,selectmode="single", font="calibri 15 bold")
    my_list.pack(expand=YES, fill=BOTH)
    l=["Grossery Items :- ", "Rice : 50Rs per kg","Foodoil : 45Rs per kg","Daal : 50rs per kg","Wheat : 65Rs per kg","Sugar : 90Rs per kg","Tea : 95Rs per kg", 
        "\n","Cold Drinks :- " ,"Pepsi : 50Rs", "Maaza : 45Rs", "Fruti : 45Rs" ,"Limca : 90Rs","Sprite : 90Rs","Mountaindew : 91Rs"]
    for i in range(len(l)):
        my_list.insert(END,l[i])
        my_list.itemconfig(i, bg="yellow" if i%2==0 else "cyan")


#........................................................Search the bill.............................................................................
def search():
    present="no"
    for i in os.listdir("bills/"):
        if i.split('.')[0]==billnovar.get():
            f=open(f"bills/{i}","r")
            textarea.delete('1.0',END)
            for items in f:
                textarea.insert(END, items)
            f.close()
            present="yes"
    if present=="no":
        tmsg.showerror("Retail Management",f"Bill no {billnovar.get()} not found")


    
root.geometry("800x800+120+120")
root.config(bg="light green")
root.title("Retail Management System")
root.iconbitmap(r'C:\Users\umang\Downloads\favicon2.ico')
f1=Frame(root,bg="light green", padx=200)
text1=Label(f1, text="Retail System", bg="light green", font="timesnewroman 50 bold")
text1.grid(row=0, column=0,padx=350,sticky="nw")
f1.grid(row=0,padx=0, sticky="nw")

#..........................................................Exit Button..................................................................

b1=Button(text="Exit", command=message , padx=50, fg='black', font="calibri 15 bold",bg="light blue", borderwidth=5, relief=GROOVE)
b1.grid(row=1,column=0, sticky="nw")

#.........................................................Customer Details...............................................................

f2=Frame(root, borderwidth=5, relief=SUNKEN, bg="light yellow")
f2.grid(sticky="nw", ipady=15, ipadx=800)
text2=Label(f2,text="Customer Details", font="arial 18 bold",bg="light yellow")
text2.grid(row=0, column=0)
namevar=StringVar()
emailvar=StringVar()
contactvar=StringVar()
contactvar.set("+91 ")
billnovar=StringVar()
x=random.randint(1000, 9500)
billnovar.set(str(x))
text3=Label(f2, text="Name", font="calibri 12 bold",bg="light yellow")
text3.grid(row=5, column=0)
namevalue=Entry(f2, textvar=namevar,borderwidth=5, relief=GROOVE, font="perpetua 12")
namevalue.grid(row=5, column=1, ipadx=50)
text4=Label(f2, text="Email", font="calibri 12 bold",bg="light yellow")
text4.grid(row=5, column=11)
emailvalue=Entry(f2, textvar=emailvar,borderwidth=5, relief=GROOVE, font="perpetua 12")
emailvalue.grid(row=5, column=14, ipadx=80, pady=20)
contactvalue=Entry(f2, textvar=contactvar,borderwidth=5, relief=GROOVE, font="perpetua 12")
contactvalue.grid(row=5, column=19, ipadx=80, pady=20)
text5=Label(f2, text="Contact No", font="calibri 12 bold",bg="light yellow")
text5.grid(row=5, column=16)
text6=Label(f2, text="Bill No", font="calibri 12 bold", bg="light yellow")
text6.grid(row=5, column=20)
billnovalue=Entry(f2, textvar=billnovar,borderwidth=5, relief=GROOVE, font="perpetua 12 bold")
billnovalue.grid(row=5, column=22, ipadx=20, pady=20)
b=Button(f2, text="Search", command=search, font="calibri 12 bold", borderwidth=5, relief=GROOVE,bg="light blue").grid(row=5, column=24)


#.............................................Grossery Items with their quantity.......................................................

ricevalue=DoubleVar()
foodoilvalue=DoubleVar()
daalvalue=DoubleVar()
wheatvalue=DoubleVar()
sugarvalue=DoubleVar()
teavalue=DoubleVar()
f4=Frame(root, borderwidth=5, relief=SUNKEN, bg="light sky blue")
grocery=Label(f4, text="Grossery", font=("times new roman", 14, "bold"), bg="light sky blue")
grocery.grid(row=4, column=0,ipady=25)
f4.grid(row=4, column=0, sticky="w", ipadx=25, ipady=20)
rice=Label(f4, text="Rice", font="calibri 12 bold", bg="light sky blue")
rice.grid(row=6, column=0, padx=5)
riceentry=Entry(f4, textvar=ricevalue,borderwidth=5, relief=GROOVE, font="arial 8 bold")
riceentry.grid(row=6, column=3, ipadx=50)
foodoil=Label(f4, text="Food Oil", font="calibri 12 bold", bg="light sky blue")
foodoil.grid(row=8, column=0, padx=5)
foodoilentry=Entry(f4, textvar=foodoilvalue,borderwidth=5, relief=GROOVE, font="arial 8 bold")
foodoilentry.grid(row=8, column=3, ipadx=50)
daal=Label(f4, text="Daal", font="calibri 12 bold", bg="light sky blue")
daal.grid(row=10, column=0, padx=5)
daalentry=Entry(f4,textvar=daalvalue,borderwidth=5, relief=GROOVE, font="arial 8 bold")
daalentry.grid(row=10, column=3, ipadx=50)
wheat=Label(f4, text="Wheat", font="calibri 12 bold", bg="light sky blue")
wheat.grid(row=12, column=0, padx=5)
wheatentry=Entry(f4, textvar=wheatvalue,borderwidth=5, relief=GROOVE, font="arial 8 bold")
wheatentry.grid(row=12, column=3, ipadx=50)
sugar=Label(f4, text="Sugar", font="calibri 12 bold", bg="light sky blue")
sugar.grid(row=14, column=0, padx=5)
sugarentry=Entry(f4, textvar=sugarvalue,borderwidth=5, relief=GROOVE, font="arial 8 bold")
sugarentry.grid(row=14, column=3, ipadx=50)
tea=Label(f4, text="Tea", font="calibri 12 bold", bg="light sky blue")
tea.grid(row=16, column=0, padx=5)
teaentry=Entry(f4, textvar=teavalue,borderwidth=5, relief=GROOVE, font="arial 8 bold")
teaentry.grid(row=16, column=3, ipadx=50)


#....................................................Cold Drink details with quantity.....................................................

pepsivalue=DoubleVar()
mazavalue=DoubleVar()
frutivalue=DoubleVar()
limcavalue=DoubleVar()
spritevalue=DoubleVar()
mountaindewvalue=DoubleVar()
f4=Frame(root, borderwidth=5, relief=SUNKEN, bg="light sky blue")
f4.grid(row=4, column=0, sticky="nw", padx=350, ipadx=20, ipady=20)
colddrinks=Label(f4, text="Cold Drinks", font=("times new roman", 14, "bold"), bg="light sky blue")
colddrinks.grid(row=4, column=0,ipady=25)
pepsi=Label(f4, text="Pepsi", font="calibri 12 bold", bg="light sky blue")
pepsi.grid(row=7, column=0, padx=5)
pepsientry=Entry(f4, textvar=pepsivalue,borderwidth=5, relief=GROOVE, font="arial 8 bold").grid(row=7, column=3, ipadx=50)
maza=Label(f4, text="Maaza", font="calibri 12 bold", bg="light sky blue")
maza.grid(row=8, column=0, padx=5)
mazaentry=Entry(f4, textvar=mazavalue,borderwidth=5, relief=GROOVE, font="arial 8 bold").grid(row=8, column=3, ipadx=50)
fruti=Label(f4, text="Fruti", font="calibri 12 bold", bg="light sky blue")
fruti.grid(row=9, column=0, padx=5)
frutientry=Entry(f4, textvar=frutivalue,borderwidth=5, relief=GROOVE, font="arial 8 bold").grid(row=9, column=3, ipadx=50)
limca=Label(f4, text="Limca", font="calibri 12 bold", bg="light sky blue")
limca.grid(row=10, column=0, padx=5)
limcaentry=Entry(f4, textvar=limcavalue,borderwidth=5, relief=GROOVE, font="arial 8 bold").grid(row=10, column=3, ipadx=50)
sprite=Label(f4, text="Sprite", font="calibri 12 bold", bg="light sky blue")
sprite.grid(row=11, column=0, padx=5)
spriteentry=Entry(f4, textvar=spritevalue,borderwidth=5, relief=GROOVE, font="arial 8 bold").grid(row=11, column=3, ipadx=50)
mountaindew=Label(f4, text="Mountain Dew", font="calibri 12 bold", bg="light sky blue")
mountaindew.grid(row=12, column=0, padx=5)
mountaindewentry=Entry(f4, textvar=mountaindewvalue,borderwidth=5, relief=GROOVE, font="arial 8 bold").grid(row=12, column=3, ipadx=50)



#............................................Bill Area Details.......................................................................

f5=Frame(root, borderwidth=5, relief=SUNKEN, bg="violet")
f5.place(rely=0.123, relx=0.01,x=750, y=180, width=750, height=500)
billtitle=Label(f5, text="Bill Details", font="calibri 25 bold", bg="violet").pack()
scrol_y=Scrollbar(f5, orient=VERTICAL)
textarea=Text(f5, yscrollcommand=scrol_y.set)
scrol_y.pack(side=RIGHT, fill=Y)
scrol_y.config(command=textarea.yview)
textarea.pack(fill=BOTH, expand=1)
def welcome():
    textarea.delete('1.0',END)
    textarea.insert(END,"\t\t\t\t**Welcome to Apna Bazar**")
    textarea.insert(END,f"\n\n\n\tBill No       : {billnovar.get()}")
    textarea.insert(END,f"\n\n\tCustomer Name : {namevar.get()}\t\t\t\t\t\t\tPhone No : {contactvar.get()}")
    date=printdate()
    textarea.insert(END,f"\n\tEmail Id : {emailvar.get()}\t\t\t\t\t\t\tDate : {date}")
    textarea.insert(END,"\n\n\t===============================================================================")
    textarea.insert(END,"\n\t\tProduct\t\t\tQuantity\t\t\tPrice(In Rs)")
    textarea.insert(END,"\n\t===============================================================================")
welcome()

def clear():
    a=tmsg.askyesno("Retail Management","Do you want to clear all ?")
    if a==True:
        textarea.delete('1.0',END)
        namevar.set("")
        contactvar.set("")
        emailvar.set("")
        billnovar.set("")
        cgvalue.set("")
        cdvalue.set("")
        tvalue.set("0.0Rs")
        ricevalue.set(0)
        foodoilvalue.set(0)
        daalvalue.set(0)
        wheatvalue.set(0)
        sugarvalue.set(0)
        teavalue.set(0)
        pepsivalue.set(0)
        mazavalue.set(0)
        frutivalue.set(0)
        limcavalue.set(0)
        spritevalue.set(0)
        mountaindewvalue.set(0)
        welcome()

def getbill():
    welcome()
    calculate()
    c=0
    if(ricevalue.get()!=0):
        textarea.insert(END,f"\n\t\tRice\t\t\t{ricevalue.get()}\t\t\t{ricevalue.get()*50}")
        c+=1
    if(foodoilvalue.get()!=0):
        textarea.insert(END,f"\n\t\tFood Oil\t\t\t{foodoilvalue.get()}\t\t\t{foodoilvalue.get()*50}")
        c+=1
    if(daalvalue.get()!=0):
        textarea.insert(END,f"\n\t\tDaal\t\t\t{daalvalue.get()}\t\t\t{daalvalue.get()*50}")
        c+=1
    if(wheatvalue.get()!=0):
        textarea.insert(END,f"\n\t\tWheat\t\t\t{wheatvalue.get()}\t\t\t{wheatvalue.get()*65}")
        c+=1
    if(sugarvalue.get()!=0):
        textarea.insert(END,f"\n\t\tSugar\t\t\t{sugarvalue.get()}\t\t\t{sugarvalue.get()*50}")
        c+=1
    if(teavalue.get()!=0):
        textarea.insert(END,f"\n\t\tTea\t\t\t{teavalue.get()}\t\t\t{teavalue.get()*50}")
        c+=1
    if(pepsivalue.get()!=0):
        textarea.insert(END,f"\n\t\tPepsi\t\t\t{pepsivalue.get()}\t\t\t{pepsivalue.get()*50}")
        c+=1
    if(mazavalue.get()!=0):
        textarea.insert(END,f"\n\t\tMaaza\t\t\t{mazavalue.get()}\t\t\t{mazavalue.get()*45}")
        c+=1
    if(frutivalue.get()!=0):
        textarea.insert(END,f"\n\t\tFruti\t\t\t{frutivalue.get()}\t\t\t{frutivalue.get()*45}")
        c+=1
    if(limcavalue.get()!=0):
        textarea.insert(END,f"\n\t\tLimca\t\t\t{limcavalue.get()}\t\t\t{limcavalue.get()*90}")
        c+=1
    if(spritevalue.get()!=0):
        textarea.insert(END,f"\n\t\tSprite\t\t\t{spritevalue.get()}\t\t\t{spritevalue.get()*90}")
        c+=1
    if(mountaindewvalue.get()!=0):
        textarea.insert(END,f"\n\t\tMountain Dew\t\t\t{mountaindewvalue.get()}\t\t\t{mountaindewvalue.get()*91}")
        c+=1
    textarea.insert(END,"\n\n\n\n\n\t===============================================================================")
    textarea.insert(END, f"\n\tTotal products : {c}")
    textarea.insert(END,f"\n\tTotal payble amount : {tvalue.get()}")
    textarea.insert(END,"\n\t===============================================================================")
        


    
#..............................................Billing Menu..................................................................
cgvalue=StringVar()
cdvalue=StringVar()
tvalue=StringVar()
tvalue.set("0.0Rs")
f6=Frame(root,  borderwidth=5, relief=SUNKEN, bg="light pink")
f6.place(rely=0.73)
text18=Label(f6, text="Billing Menu", font="calibri 18 bold", bg="light pink").grid(row=18, column=0)
cg=Label(f6, text="Calculate Grossery", font="calibri 14 bold", bg="light pink")
cg.grid(row=20, column=0)
cgentry=Entry(f6,textvar=cgvalue,borderwidth=5, relief=GROOVE, font="arial 12 bold", state=DISABLED).grid(row=20, column=3, padx=25, ipadx=100)
cd=Label(f6, text="Calculate Cold Drink", font="calibri 14 bold", bg="light pink")
cd.grid(row=28, column=0)
cdentry=Entry(f6,textvar=cdvalue,borderwidth=5, relief=GROOVE, font="arial 12 bold", state=DISABLED).grid(row=28, column=3, padx=25, ipadx=100)
t=Label(f6, text="Total Amount", font="calibri 14 bold", bg="light pink")
t.grid(row=30, column=0, ipady=5)
tentry=Entry(f6,textvar=tvalue,borderwidth=5, relief=GROOVE,bg='light gray', font="arial 12 bold", state=DISABLED).grid(row=30, column=3, padx=25, ipadx=100)


def calculate():
    price_rice=50
    price_foodoil=45
    price_daal=50
    price_wheat=65
    price_sugar=90
    price_tea=95
    total1=float((ricevalue.get()*price_rice) + (foodoilvalue.get()*price_foodoil) + (daalvalue.get()*price_daal) + (wheatvalue.get()*price_wheat) + (sugarvalue.get()*price_sugar) + (teavalue.get()*price_tea))
    cgvalue.set(str(total1)+ "Rs")

    price_pepsi=50
    price_maza=45
    price_fruti=45
    price_limca=90
    price_sprite=90
    price_mountaindew=91
    total2=float((pepsivalue.get()*price_pepsi) + (mazavalue.get()*price_maza) + (frutivalue.get()*price_fruti) + (limcavalue.get()*price_limca) + (spritevalue.get()*price_sprite) + (mountaindewvalue.get()*price_mountaindew))
    cdvalue.set(str(total2)+ "Rs")
    
    grandtotal=total1 + total2
    tvalue.set(str(grandtotal)+"Rs")


b3=Button(root, text="Total", font="calibri 15 bold", command=calculate,borderwidth=5, relief=GROOVE, bg="light blue", width=10)
b3.place(relx=0.0, rely=0.92)
b4=Button(root, text="Generate Bill", font="calibri 15 bold", command=getbill ,bg="light blue",borderwidth=5, relief=GROOVE, width=11).place(relx=0.08, rely=0.92)
b5=Button(root, text="Save", font="calibri 15 bold", command=savefile,borderwidth=5,bg="light blue" ,relief=GROOVE, width=10 ).place(relx=0.167, rely=0.92)
b6=Button(root, text="Print", font="calibri 15 bold", command=print,borderwidth=5,bg="light blue" ,relief=GROOVE, width=10 ).place(relx=0.248, rely=0.92)
b6=Button(root, text="Clear", font="calibri 15 bold", command=clear,borderwidth=5,bg="light blue" ,relief=GROOVE, width=10 ).place(relx=0.329, rely=0.92)
b7=Button(root, text="Price List", font="calibri 15 bold", command=PriceList,borderwidth=5,bg="light blue" ,relief=GROOVE, width=10 ).place(relx=0.4101, rely=0.92)
root.mainloop()
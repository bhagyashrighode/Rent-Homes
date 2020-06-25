from tkinter import *
from PIL import Image,ImageTk 
from tkinter import ttk

root=Tk()
root.title('RentHome')
root.geometry("600x600")
root.config(bg='skyblue')
v=IntVar()
type=StringVar()
bhk=StringVar()
budget=StringVar()

l1=Label(root,text="Welome to Pune",font=("Times",20,"bold"),fg='red',bg='skyblue').pack()

l2=Label(root,text="Choose One:",font=('Times',16),fg='grey',bg='skyblue').pack(side=TOP,padx=5,pady=5)

r1=Radiobutton(root,text="Pune",font=('Times',16),fg='grey',bg='skyblue',variable=v,value=1).pack(side=TOP,padx=5,pady=5)
r2=Radiobutton(root,text="Pimpri-Chinchwad",font=('Times',16),fg='grey',bg='skyblue',variable=v,value=2).pack(padx=5,pady=5)

canvas = Canvas(root, width = 200, height = 100,bg='skyblue')  
canvas.pack(side=TOP)  
img = ImageTk.PhotoImage(Image.open('home.jpeg'))  
canvas.create_image(40,40,image=img)
Label(root,text="Struggling to find perfect home & area?\nLet us do the searching for you.",font=('Times',16),fg='Blue',bg='skyblue').pack()

Label(root,text="BHK",font=('Times',16),fg='grey',bg='skyblue').pack(padx=5,pady=5)
c=ttk.Combobox(root,textvariable=bhk,width=12,state='readonly')
c['values']=('1RK','1BHK','2BHK','3BHK','4BHK')
c.set('-Select-')
c.pack(padx=5,pady=5)

Label(root,text="Rent Budget",font=('Times',16),fg='grey',bg='skyblue').pack(padx=10,pady=5)
c1=ttk.Combobox(root,textvariable=budget,width=12,state='readonly')
c1['values']=(3000,5000,7000,9000,10000,11000,12000,15000,20000,25000,30000,35000,40000,45000,50000,60000)
c1.set('-Select-')
c1.pack(padx=5,pady=5)

Label(root,text="Furnishing Type",font=('Times',16),fg='grey',bg='skyblue').pack(padx=15,pady=5)
c2=ttk.Combobox(root,textvariable=type,width=12,state='readonly')
c2['values']=('Furished','Unfurnished','SemiFurnished')
c2.set('-Select-')
c2.pack(padx=5,pady=5)
b=Button(root,text="Search").pack()
Label(root,text="Good Area for you within your budget:",font=('Times',16),fg='Blue',bg='skyblue').pack()
Entry(root,text="Choose all Options First",font=('Times',16),fg='grey',bg='skyblue').pack()

root.mainloop()

import tkinter

root = tkinter.Tk()
root.geometry("300x250")
root.title("Quadratic calculator")

a = tkinter.Label(root,text="Hodnota a: ")
a.pack()
aa = tkinter.Entry(root,width=40)
aa.pack()

b = tkinter.Label(root,text="Hodnota b: ")
b.pack()
bb = tkinter.Entry(root,width=40)
bb.pack()

c = tkinter.Label(root,text="Hodnota c: ")
c.pack()
cc = tkinter.Entry(root,width=40)
cc.pack()

x = tkinter.Label(root,text="Výsledok:")
x.pack()
xx = tkinter.Entry(root,width=40)
xx.pack()

#Pocitanie
def executor():
    print(aa.get(),bb.get(),cc.get())
    ka = int(aa.get())
    kb = int(bb.get())
    kc = int(cc.get())
    d = kb**2 - 4*ka*kc
    if d<0:
        xx.insert(0,"Nemá riešenie v R")
    elif d == 0:
        x = -kb/(2*ka)
        xx.insert(0,x)
        xx.insert(0,"x = ")
    else:
        x1 = round(((-kb+d ** 0.5)/(2*ka)),4)
        x2 = round(((-kb-d ** 0.5)/(2*ka)),4)
        xx.insert(0,x2)
        xx.insert(0," ; x2= ")
        xx.insert(0,x1)
        xx.insert(0,"x1= ")

def clear():
    xx.delete(0, 'end')
    aa.delete(0, 'end')
    bb.delete(0, 'end')
    cc.delete(0, 'end')

label = tkinter.Label(root,text="")
label.pack()
button = tkinter.Button(root,text="Počítaj", padx = 10, pady = 5,command=executor)
button.pack()
button2 = tkinter.Button(root,text="Clear",command=clear)
button2.pack()
root.mainloop()

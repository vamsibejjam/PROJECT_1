from tkinter import *
import math
# CREATE GUI WINDOW
calci=Tk()
calci.title('CALUCLATOR')
calci.geometry('500x400')
result=Entry(fg='black',bd=5,font=('arial bold',30 ),bg='cyan')
result.grid(row=0,column=0,columnspan=4,padx=25,pady=2)
result.focus_set()

#..BUTTONS..
num0=Button(text='0',font=('arial bold',15 ),bg='orange',bd=5,width=5, command=lambda :insert('0'))
num0.grid(row=1,column=0, padx=3, pady=3)

num1=Button(text='1',font=('arial bold',15 ),bg='orange',bd=5,width=5, command=lambda:insert('1'))
num1.grid(row=1,column=1, padx=3, pady=3)

num2=Button(text='2',font=('arial bold',15 ),bg='orange',bd=5,width=5, command=lambda:insert('2'))
num2.grid(row=1,column=2, padx=3, pady=3)

num0=Button(text='+',font=('arial bold',15 ),bg='teal',bd=5,width=5, command=lambda:insert('+'))
num0.grid(row=1,column=3, padx=3, pady=3)

num3=Button(text='3',font=('arial bold',15),bg='orange',bd=5,width=5, command=lambda:insert('3'))
num3.grid(row=2,column=0, padx=3, pady=3)

num4=Button(text='4',font=('arial bold',15 ),bg='orange',bd=5,width=5, command=lambda:insert('4'))
num4.grid(row=2,column=1, padx=3, pady=3)

num5=Button(text='5',font=('arial bold',15 ),bg='orange',bd=5,width=5, command=lambda:insert('5'))
num5.grid(row=2,column=2, padx=3, pady=3)

num6=Button(text='-',font=('arial bold',15 ),bg='teal',bd=5,width=5, command=lambda:insert('-'))
num6.grid(row=2,column=3, padx=3, pady=3)

num7=Button(text='7',font=('arial bold',15 ),bg='orange',bd=5,width=5, command=lambda:insert('7'))
num7.grid(row=3,column=0, padx=3, pady=3)

num8=Button(text='8',font=('arial bold',15 ),bg='orange',bd=5,width=5, command=lambda:insert('8'))
num8.grid(row=3,column=1, padx=3, pady=3)

num9=Button(text='9',font=('arial bold',15 ),bg='orange',bd=5,width=5, command=lambda:insert('9'))
num9.grid(row=3,column=2, padx=3, pady=3)

num9=Button(text='/',font=('arial bold',15 ),bg='teal',bd=5,width=5, command=lambda:insert('/'))
num9.grid(row=3,column=3, padx=3, pady=3)

num10=Button(text='DEL',font=('arial bold',15 ),bg='orange',bd=5,width=5, command=lambda:erase())
num10.grid(row=4,column=0, padx=3, pady=3)

num11=Button(text='C',font=('arial bold',15 ),bg='orange',bd=5,width=5, command=lambda:erase_all())
num11.grid(row=4,column=1, padx=3, pady=3)

num12=Button(text='=',font=('arial bold',15 ),bg='orange',bd=5,width=5, command=lambda:Eval())
num12.grid(row=4,column=2, padx=3, pady=3)

num13=Button(text='*',font=('arial bold',15 ),bg='teal',bd=5,width=5, command=lambda:insert('*'))
num13.grid(row=4,column=3, padx=3, pady=3)

num14=Button(text='SIN',font=('arial bold',15 ),bg='teal',bd=5,width=5, command=lambda:f_sin())
num14.grid(row=5,column=0, padx=3, pady=3)

num15=Button(text='COS',font=('arial bold',15 ),bg='teal',bd=5,width=5, command=lambda:f_cos())
num15.grid(row=5,column=1, padx=3, pady=3)

num16=Button(text='TAN',font=('arial bold',15 ),bg='teal',bd=5,width=5, command=lambda:f_tan())
num16.grid(row=5,column=2, padx=3, pady=3)

num17=Button(text='e',font=('arial bold',15 ),bg='teal',bd=5,width=5, command=lambda:f_exp())
num17.grid(row=5,column=3, padx=3, pady=3)

num18=Button(text='log',font=('arial bold',15 ),bg='teal',bd=5,width=5, command=lambda:log())
num18.grid(row=6,column=0, padx=3, pady=3)

num19=Button(text='(',font=('arial bold',15 ),bg='teal',bd=5,width=5, command=lambda:insert('('))
num19.grid(row=6,column=1, padx=3, pady=3)

num20=Button(text=')',font=('arial bold',15 ),bg='teal',bd=5,width=5, command=lambda:insert(')'))
num20.grid(row=6,column=2, padx=3, pady=3)

num21=Button(text='^',font=('arial bold',15 ),bg='teal',bd=5,width=5, command=lambda:power())
num21.grid(row=6,column=3, padx=3, pady=3)

# TRIGNOMETRY FUNCTIONS:
def f_sin():
    x=result.get()
    # check whether function is repeated...
    if not x:
        result.insert(0, 'sin')
def log():
    x = result.get()
    # check whether function is repeated...
    if not x:
        result.insert(0, 'log')
def f_cos():
    x = result.get()
    # check whether function is repeated...
    if not x:
        result.insert(0, 'cos')
def f_tan():
    x = result.get()
    # check whether function is repeated...
    if not x:
        result.insert(0, 'tan')
def f_exp():
    x = result.get()
    # check whether function is repeated...
    if not x:
        result.insert(0, 'e^')
def power():
    x = result.get()
    # check whether function is repeated...
    if not x:
        result.insert(END, '^')

# USER DEFINED FUNCTIONS:
def insert(x):
    result.insert(END,x)
def erase():
    inserted_val=result.get()
    result.delete(0,'end')
    del_val=inserted_val[:-1]
    result.insert(0,del_val)
def erase_all():
    result.delete(0,'end')

def Eval():
    val=result.get()
    if 'sin' in val:
        y=int(val[4:-1])  # Extracting value from string inserted by user on Enter text box
        z=math.sin(y)

    elif 'cos' in val:
        y = int(val[4:-1]) # Extracting value from string inserted by user on Enter text box
        z=math.cos(y)

    elif 'tan' in val:
        y = int(val[4:-1]) # Extracting value from string inserted by user on Enter text box
        z=math.tan(y)

    elif 'e^' in val:
        y = int(val[2:]) # Extracting value from string inserted by user on Enter text box
        z=math.exp(y)

    elif 'log' in val:
        y = int(val[4:-1]) # Extracting value from string inserted by user on Enter text box
        z=math.log(y)

    else:
        z = eval(val)

    result.delete(0, 'end')
    result.insert(0, z)

calci.mainloop()

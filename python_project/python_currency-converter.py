#source code for python gui

from tkinter import *
converter = Tk()
converter.geometry("800x500")
converter.title("CURRENCY CONVERTER")
OPTIONS ={
    "Australian Dollar":0.019,
    "Brazilian Real":0.077,
    "British Pound":0.010,
    "Bulgarian Lev":0.023,
    "Chinese Yuan":0.090,
    "Euro":0.011,
    "HongKong Dollar":0.10,
    "Indonesian Rupiah":195.72,
    "Japanese Yen":1.40,
    "Pakistani Rupee":2.15,
    "Sri Lankan Rupee":2.47,
    "Swiss Franc":0.012,
    "US Dollar":0.013,
          }
def ok():
    price = rupees.get()
    answer = variable.get()
    DICT = OPTIONS.get(answer,None)
    converted = float(DICT)*float(price)
    result.delete(1.0,END)
    result.insert(INSERT,"Currency in ",INSERT,answer,INSERT," = ",
                    INSERT,converted)

appName = Label(converter,text="Welcome to Currency Converter",
                font=("arial",25,"bold","underline"),fg="red")
appName.grid(row=0,column=1)


result = Text(converter,height=5,width=50,
              font=("arial",10,"bold"),bd=5)
result.grid(row=1,column=1,padx=3)
india = Label(converter,text="Indian Rupees:",
              font=("arial",10,"bold"),fg="black")
india.grid(row=2,column=0)
rupees = Entry(converter,font=("calibri",20))
rupees.grid(row=2,column=1)
choice = Label(converter,text="Choose Country:",
              font=("arial",10,"bold"),fg="black")
choice.grid(row=3,column=0)
variable=StringVar(converter)
variable.set(None)
option = OptionMenu(converter,variable,*OPTIONS)
option.grid(row=3,column=1,sticky="ew")
button = Button(converter,text="Convert",fg="blue",
                font=("calibri",20),bg="powder blue",command=ok)
button.grid(row=3,column=2)
mainloop()

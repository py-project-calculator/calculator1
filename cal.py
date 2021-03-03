from tkinter import *

root=Tk()

root.title("Calculator")      #creating title of gui
root.geometry("500x500")     #dimension of gui
root.minsize(500,500)
root.maxsize(500,500)
root.iconbitmap('D:\pes.ico')  #icon
strvalue=StringVar()          #string variable 
strvalue.set("")               #value is intially null
text1=Label(text="Let's calculate",fg="black",font="lucida 15 italic")
text1.pack()
screen=Entry(root,textvar=strvalue,font="lucida 33 bold",borderwidth=5,relief=SUNKEN)  #screen of calculator
screen.pack(fill=X,ipadx=5,pady=5,padx=5)                     #packing the gui



root.mainloop()         
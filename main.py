from tkinter import *

window=Tk()
window.title("login account")
window.geometry("600x600")

frame=Frame(master=window , height=200 , width=360 , bg="#1eb2cc")
lbl1=Label(frame,text='Full Name',bg='black',fg='white',width=12)
lbl2=Label(frame,text='Email Adderess',bg='black',fg='white',width='12')
lbl3=Label(frame,text='Password',bg='black',fg='white',width='12')

entry1=Entry(frame)
entry2=Entry(frame)
entry3=Entry(frame)

def display():
  name=entry1.get()
  message=name + 'you have sucessfully created a new account!!!'
  textbox.insert(END,message)

btn=Button(text='create account',command=display,bg='black',fg='white')  
textbox=Text(bg='#88918d',fg='white')


frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
entry1.place(x=150, y=20)
lbl2.place(x=20, y=80)
entry2.place(x=150, y=80)
lbl3.place(x=20, y=140)
entry3.place(x=150, y=140)
btn.place(x=130, y=210)
textbox.place(y=250)

window.mainloop()
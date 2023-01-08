from tkinter import *
master=Tk()
demo_text="This is a smple of message widget."
msg=Message(master,text=demo_text)
msg.config(bg='lightgreen',font=('timies',24,'italic'))
msg.pack()

from tkinter import *
import datetime

# Create Window
window = Tk()
window.title("Age Calculator App")
window.geometry("400x400")


def calculate():
	name = name_entry.get()
	year = int(year_entry.get())
	
	today = datetime.date.today()
	
	age = today.year - year
	
	greet = "Hey, "+name+"!"
	message =  "\nYour age is: "+str(age)+" years old."
	textbox.insert(END, greet)
	textbox.insert(END, message)

# Create a frame to organize elements better
frame = Frame(master=window, height=200, width=360, bg="#00ffff")

# create widgets
lbl1 = Label(frame, text = "Name", bg="#CA3433", fg="white", width=12)
lbl2 = Label(frame, text = "Year", bg="#CA3433", fg="white", width=12)
lbl3 = Label(frame, text = "Month", bg="#CA3433", fg="white", width=12)
lbl4 = Label(frame, text = "Date", bg="#CA3433", fg="white", width=12)

name_entry = Entry(frame)
year_entry = Entry(frame)
month_entry = Entry(frame)
date_entry = Entry(frame)

textbox = Text(bg="#BEBEBE", fg="black")

btn = Button(text = "Calculate", command=calculate, bg="red", fg="yellow")

#arrange the widgets
frame.place(x=20,y=0)

lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)

lbl2.place(x=20, y=50)
year_entry.place(x=150, y=50)

lbl3.place(x=20, y=80)
month_entry.place(x=150, y=80)

lbl4.place(x=20, y=110)
date_entry.place(x=150, y=110)

btn.place(x=140, y=210)

textbox.place(y=250)

window.mainloop()
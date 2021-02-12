'''
Connor Kissack
GUI Project
9 February 2021
'''


import tkinter
from tkinter import *

master = Tk()


master.geometry("500x430")
master.title("GUI")
master.configure(background="grey")

def printNow():
    print("A button has been clicked")

# ////////////////////////////////////////////

def change_slider(value):
    print("First slider is working")

# ////////////////////////////////////////////

def change_slider2(value):
    print("Second slider is working")

# ////////////////////////////////////////////

# --------------------
# IGNORE CANVAS COMMENTS
# --------------------

# canvas = Canvas(master, width='200', height='200')

# --- add = Button(master,text= '+', bg="lime green", fg="gray20", highlightbackground="lime green")
# --- add.grid(column=3, row=2)

# global counter
# counter = 0
# def lines():
#     global counter
#     canvas_height = 20
#     canvas_width = 200
#     y = int(canvas_height / 2)
#     canvas.create_line(0, y, canvas_width, y)
#
#     x1 = 0
#     y1 = canvas_width
#     x2 = 0
#     y2 = 0
#
#     canvas.create_line(x1, y1, x2, y2)
#     canvas.create_line(x1, y1+counter, x2, y2+counter)
#     for x in range(0, 200, 20):
#         canvas.create_line(x1, y1, x2, y2)
#         canvas.create_line(x1, y1 + x, x2, y2 + x)
#     counter =+ 50
#
# draw_button1 = Button(master,text= 'Draw Lines', command=lines, bg="yellow", fg="gray20", highlightbackground="yellow")
# draw_button1.grid(column=3, row=2)
# -------------------------------
# canvas.grid(column= 4, row = 4)

# Color coded buttons

blue_button = Button(master, command=printNow, text= ' Blue ', bg="blue", fg="blue2", highlightbackground="blue")
blue_button.grid(sticky=NW)

green_button = Button(master, command=printNow, text='Green ', bg="green", fg="green2", highlightbackground="green")
green_button.grid(sticky=NW)

red_button = Button(master, command=printNow, text=' Red  ', bg="red", fg="red3", highlightbackground="red")
red_button.grid(sticky=NW)

yellow_button = Button(master, command=printNow, text='Yellow', bg="yellow", fg="gold", highlightbackground="yellow")
yellow_button.grid(sticky=NW)

# ////////////////////////////////////////////

# Check boxes

check1 = Checkbutton(master, command=printNow, text=' ✓', bg="gray80")
check1.grid(row=0, column=1, stick=E)


check2 = Checkbutton(master, command=printNow, text=' ✓', bg="gray80")
check2.grid(row=0, column=2)


check3 = Checkbutton(master, command=printNow, text=' ✓', bg="gray80")
check3.grid(row=0, column=3)


check4 = Checkbutton(master, command=printNow, text=' ✓', bg="gray80")
check4.grid(row=0, column=4)


# ////////////////////////////////////////////

# Scales

scale1 = Scale(master, from_=0, to=100, tickinterval=10, command=change_slider)
scale1.grid(row=4, column=0)

scale2 = Scale(master, from_=0, to=100, tickinterval=10, command=change_slider2)
scale2.grid(row=4, column=1)

# ////////////////////////////////////////////

# Labels

label1 = Label(master, text="These").grid(sticky=NW)

label2 = Label(master, text="Are    ").grid(sticky=NW)

label3 = Label(master, text="My     ").grid(sticky=NW)

label4 = Label(master, text="Labels").grid(sticky=NW)

# ////////////////////////////////////////////

# Text boxes

textbox1 = Entry(master, width=5)
textbox1.grid(stick=W, ipadx=8)


textbox2 = Entry(master, width=5)
textbox2.grid(stick=W, ipadx=8)

# ////////////////////////////////////////////

# Scrollbar

scrollbar = Scrollbar(master, width=5)
scrollbar.grid(row=4, column=5)
mylist = Listbox(master, yscrollcommand = scrollbar.set, width=4)
for line in range(100):
   mylist.insert(END, '# ' + str(line))
mylist.grid(row=4, column=4)
scrollbar.config(command = mylist.yview)


# ////////////////////////////////////////////

# Drop menu

dropmenu = Menubutton(master, text="Drop", activebackground='black')
dropmenu.grid(row=0, column=5)
dropmenu.menu = Menu(dropmenu, tearoff=6)
dropmenu["menu"] = dropmenu.menu
drpmnu_select = IntVar()
drpmn_select2 = IntVar()
dropmenu.menu.add_checkbutton(label='Select Me!', variable=drpmnu_select)
dropmenu.menu.add_checkbutton(label='No Select Me!', variable=drpmn_select2)

# ////////////////////////////////////////////

# Radio Buttons

radiob1 = Radiobutton(master, command=printNow, text='Radio 1', value=1).grid(row=0, column=7)
radiob2 = Radiobutton(master, command=printNow, text='Radio 2', value=2).grid(row=1, column=7)
radiob3 = Radiobutton(master, command=printNow, text='Radio 3', value=3).grid(row=0, column=8, ipady=1)
radiob4 = Radiobutton(master, command=printNow, text='Radio 4', value=4).grid(row=1, column=8, stick=N)
radiob5 = Radiobutton(master, command=printNow, text='Radio 5', value=5).grid(row=2, column=8, sticky=N)


# ////////////////////////////////////////////

# Pop up window

win = Toplevel()
win.title("BOO! (Pop Up)")
win.configure(bg="black")


# ////////////////////////////////////////////

# Spinbox

spin_box = Spinbox(master, from_=-50, to=50, width=6)
spin_box.grid(row=3, column=8)

# ////////////////////////////////////////////


master.mainloop()

from tkinter import *
import backend

#Obtaining selected book information and displaying it in entry widgets
def get_sel_row(event):
    try:
        global sel_row
        index = list1.curselection()[0]
        sel_row = list1.get(index)
        
        e1.delete(0,END)
        e1.insert(END,sel_row[1])
        e2.delete(0,END)
        e2.insert(END,sel_row[2])
        e3.delete(0,END)
        e3.insert(END,sel_row[3])
        e4.delete(0,END)
        e4.insert(END,sel_row[4])
    
    except IndexError:
        pass
    

#command functions
def view_all_comm():
    list1.delete(0,END)
    for row in backend.view_all():
        list1.insert(END,row)

def search_entry_comm():
    list1.delete(0,END)
    for row in backend.search_entry(title_value.get(), author_value.get(), year_value.get(), ISBN_value.get()):
        list1.insert(END, row)

def add_entry_comm():
    backend.add_entry(title_value.get(), author_value.get(), year_value.get(), ISBN_value.get())
    list1.delete(0,END)
    list1.insert(END,(title_value.get(), author_value.get(), year_value.get(), ISBN_value.get()))

def delete_comm():
    backend.delete(sel_row[0])

def update_comm():
    backend.update(sel_row[0],title_value.get(), author_value.get(), year_value.get(), ISBN_value.get())

#window declaration
window = Tk()
window.wm_title("Bookstore")

#label widgets
l1 = Label(window, text="Title")
l1.grid(row=0,column=0)

l2 = Label(window, text="Author")
l2.grid(row=0,column=2)

l3 = Label(window, text="Year")
l3.grid(row=1,column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1,column=2)

#entry widgets
title_value = StringVar()
e1 = Entry(window, textvariable=title_value)
e1.grid(row=0,column=1)

author_value = StringVar()
e2 = Entry(window, textvariable=author_value)
e2.grid(row=0,column=3)

year_value = StringVar()
e3 = Entry(window, textvariable=year_value)
e3.grid(row=1,column=1)

ISBN_value = StringVar()
e4 = Entry(window, textvariable=ISBN_value)
e4.grid(row=1,column=3)

#List box and scroll bar 
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#Bind method for cursor selection in listbox
list1.bind("<<ListboxSelect>>",get_sel_row)

#Button/functional widgets
b1 = Button(window, text = "View all", width=13, command=view_all_comm)
b1.grid(row=2,column=3)

b2 = Button(window, text = "Search entry",width=13, command=search_entry_comm)
b2.grid(row=3,column=3)

b3 = Button(window, text = "Add entry",width=13, command=add_entry_comm)
b3.grid(row=4,column=3)

b4 = Button(window, text = "Update",width=13, command=update_comm)
b4.grid(row=5,column=3)

b5 = Button(window, text = "Delete",width=13, command=delete_comm)
b5.grid(row=6,column=3)

b1 = Button(window, text = "Close",width=13, command=window.destroy)
b1.grid(row=7,column=3)





window.mainloop()
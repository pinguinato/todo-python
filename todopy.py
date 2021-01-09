"""
Python Task List by Roberto Gianotto

This project is inspired by: https://cppsecrets.com/users/218111411511410110199104971141051161049764103109971051084699111109/Python-Tkinter-To-do-List.php

"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sq

root = tk.Tk()
root.title('Task List')
root.geometry("400x250+500+300")

# database
connection = sq.connect('todo.db')
cursor = connection.cursor()
cursor.execute('create table if not exists tasks (title text)')

# Task List
task = []

# Functions
def listUpdate():
    clearList()
    for i in task:
        t.insert('end', i)

def clearList():
    t.delete(0, 'end')

def addTask():
    word = e1.get()
    if len(word) == 0:
        messagebox.showinfo('Empty Entry', 'Enter task name')
    else:
        task.append(word)
        cursor.execute('insert into tasks values (?)', (word,))
        listUpdate()
        e1.delete(0, 'end')

def deleteAll():
    mb = messagebox.askyesno('Delete All', 'Are you sure?')
    if mb == True:
        while (len(task) != 0):
            task.pop()
        cursor.execute('delete from tasks')
        listUpdate()

def delOne():
    try:
        val = t.get(t.curselection())
        if val in task:
            task.remove(val)
            listUpdate()
            cursor.execute('delete from tasks where title = ?', (val,))
    except:
        messagebox.showinfo('Cannot Delete', 'No Task Item Selected')

def bye():
    print(task)
    root.destroy()

def retrieveDB():
    while (len(task) != 0):
        task.pop()
    for row in cursor.execute('select title from tasks'):
        task.append(row[0])


# Application Graphics Elements
l1 = ttk.Label(root, text='My Task List')
l2 = ttk.Label(root, text='Enter task title: ')
e1 = ttk.Entry(root, width=21)
t = tk.Listbox(root, height=11, selectmode='SINGLE')
b1 = ttk.Button(root, text='Add task', width=20, command=addTask)
b2 = ttk.Button(root, text='Delete', width=20, command=delOne)
b3 = ttk.Button(root, text='Delete all', width=20, command=deleteAll)
b4 = ttk.Button(root, text='Exit', width=20, command=bye)

retrieveDB()
listUpdate()

# Elements positions
l2.place(x=50, y=50)
e1.place(x=50, y=80)
b1.place(x=50, y=110)
b2.place(x=50, y=140)
b3.place(x=50, y=170)
b4.place(x=50, y =200)
l1.place(x=50, y=10)
t.place(x=220, y=50)

root.mainloop()

connection.commit()
cursor.close()

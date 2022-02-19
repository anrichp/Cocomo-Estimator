from cgitb import text
from operator import index
from pydoc import cli
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Cocomo Estimator")
root.geometry("500x500")

my_tree = ttk.Treeview(root)

# Define Columns
my_tree['columns'] = ("Organic", "Semi-Detached", "Embedded")

# Format Columns
my_tree.column("#0", width=155, minwidth=25)
my_tree.column("Organic", anchor=W, width=120)
my_tree.column("Semi-Detached", anchor=CENTER, width=120)
my_tree.column("Embedded", anchor=W, width=120)

# Create Headings
my_tree.heading("#0", anchor=W)
my_tree.heading("Organic", text="Organic", anchor=W)
my_tree.heading("Semi-Detached", text="Semi-Detached", anchor=CENTER)
my_tree.heading("Embedded", text="Embedded", anchor=W)

# Insert Tree Data
my_tree.insert(parent='', index='end', iid=0,
               text="Variable A")
my_tree.insert(parent='', index='end', iid=1,
               text="Variable B")
my_tree.insert(parent='', index='end', iid=3,
               text="Variable C")
my_tree.insert(parent='', index='end', iid=4,
               text="Variable D")
my_tree.insert(parent='', index='end', iid=5,
               text="KLOC")
my_tree.insert(parent='', index='end', iid=6,
               text="Effort (person/month)")
my_tree.insert(parent='', index='end', iid=7,
               text="Duration (months")
my_tree.insert(parent='', index='end', iid=8,
               text="Staffing (Recommended)")


# Create entry box
e = Entry(root)


# Perform the calculation
def calculate(number):
    return


# Clear all values
def clear():
    e.delete(0, END)


# Define labels
calculate_label = Label(root, text="Enter the estimated lines of code (LOC)")

# Define buttons
button_calculate = Button(root, text="Calculate", padx=50, command=calculate)
button_clear = Button(root, text="Clear", padx=50, command=clear)

# Place buttons and labels
calculate_label.grid(row=0, column=0)
e.grid(row=1, column=0)
button_calculate.grid(row=2, column=0)
button_clear.grid(row=3, column=0)
my_tree.grid(row=4)

root.mainloop()

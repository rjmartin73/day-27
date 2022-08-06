from tkinter import *

window = Tk()
window.title("My Tkinter window")
window.minsize(width=500, height=500)

# Label
my_label = Label(text="This is a label")
my_label.pack()


def button_clicked():
    my_label.config(text=my_input.get())


my_button = Button(text="CLick Me", command=button_clicked)
my_button.pack()

# Entries
my_input = Entry(width=40)
my_input.pack()

# Gets entry
print(my_input.get())

# Text
text = Text(height=5, width=30)
# Puts cursor in textbox
text.focus()
# Adds some default text
text.insert(END, "Example of multi-line text entry.")
# Gets current value in textbox at line 1, character 0.
print(text.get("1.0", END))
text.pack()

# Spinbox
def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=10, command=scale_used)
scale.pack()

# Checkbutton (checkbox)
def checkbox_clicked():
    if checked_state.get() == 1:
        print("Checkbox checked")
    else:
        print("Checkbox not checked")
checked_state = IntVar() # Holds the state of the checkbox
checkbox = Checkbutton(text="Is on?", command=checkbox_clicked, onvalue=1,
                       offvalue=0, variable=checked_state)
checked_state.get()
checkbox.pack()

# Radio buttons
def radio_used():
    print(f"Option {radio_state.get()} selected.")
radio_state = IntVar()
radio_button_1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radio_button_2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radio_button_1.pack()
radio_button_2.pack()

# Listbox
def listbox_clicked(value):
    print(listbox.get(listbox.curselection()))
    print(selection_list.get())
listbox = Listbox(height=5, width=10,)
selection_list = StringVar()
listbox.configure(listvariable=selection_list)
listbox_items = ["Apple", "Banana", "Orange", "Pear"]
for _ in listbox_items:
    listbox.insert(END, _)
listbox.bind("<<ListboxSelect>>", listbox_clicked)

listbox.pack()
window.mainloop()



import tkinter as tk
from tkinter import ttk

# Define functions for the operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Function to handle button clicks and key presses
def on_button_click(value):
    current_text = entry_var.get()
    entry_var.set(current_text + value)

# Function to clear the entry
def clear_entry():
    entry_var.set("")

# Function to calculate the result
def calculate(event=None):
    try:
        expression = entry_var.get()
        # Evaluate the expression
        result = eval(expression)
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")
        print("Error:", e)

# Function to handle key presses
def on_key_press(event):
    key = event.char
    if key.isdigit() or key in "+-*/.":
        on_button_click(key)
    elif key == '\r':  # Enter key
        calculate()
    elif key == '\x08':  # Backspace key
        current_text = entry_var.get()
        entry_var.set(current_text[:-1])

# Create the main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("350x450")
root.resizable(False, False)

# Apply a modern style
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 14), padding=10, foreground='black')
style.configure("TEntry", font=("Helvetica", 18))

# Create a StringVar to hold the entry value
entry_var = tk.StringVar()

# Create and place the entry widget
entry = ttk.Entry(root, textvariable=entry_var, font=('Helvetica', 18), justify='right')
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, padx=0, pady=0, sticky="nsew")

# Create button widgets
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2)
]

for (text, row, column) in buttons:
    btn = ttk.Button(root, text=text, command=lambda t=text: on_button_click(t))
    btn.grid(row=row, column=column, ipadx=10, ipady=10, padx=0, pady=0, sticky="nsew")

# Create a clear button
clear_button = ttk.Button(root, text="C", command=clear_entry)
clear_button.grid(row=4, column=3, ipadx=10, ipady=10, padx=0, pady=0, sticky="nsew")

# Create an equals button
equals_button = ttk.Button(root, text="=", command=calculate)
equals_button.grid(row=5, column=0, columnspan=4, ipadx=10, ipady=10, padx=0, pady=0, sticky="nsew")

# Make the buttons expand evenly
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Bind key events
root.bind('<KeyPress>', on_key_press)

# Run the application
root.mainloop()

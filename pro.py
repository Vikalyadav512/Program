import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("400x500")

# Entry widget for the display
display = tk.Entry(window, font=("Arial", 24), borderwidth=2, relief="solid")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to update the display
def button_click(item):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + item)

# Function to clear the display
def clear_display():
    display.delete(0, tk.END)

# Function to evaluate the expression
def calculate():
    try:
        result = str(eval(display.get()))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == "=":
        tk.Button(window, text=button, width=10, height=3, command=calculate).grid(row=row, column=col, columnspan=2, padx=5, pady=5)
    else:
        tk.Button(window, text=button, width=10, height=3, command=lambda b=button: button_click(b)).grid(row=row, column=col, padx=5, pady=5)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Add Clear button
tk.Button(window, text='C', width=10, height=3, command=clear_display).grid(row=row, column=col, padx=5, pady=5)

# Start the main event loop
window.mainloop()

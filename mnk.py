import tkinter as tk

def clear_display():
    display_var.set("")

def add_to_display(value):
    current_value = display_var.get()
    display_var.set(current_value + value)

def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
    except:
        display_var.set("Error")

# Create main window
root = tk.Tk()
root.title("Modern Calculator")

# Create display
display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=('Arial', 20), justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons
buttons = [
    ('AC', clear_display),
    ('/', lambda: add_to_display('/')),
    ('*', lambda: add_to_display('*')),
    ('-', lambda: add_to_display('-')),
    ('7', lambda: add_to_display('7')),
    ('8', lambda: add_to_display('8')),
    ('9', lambda: add_to_display('9')),
    ('+', lambda: add_to_display('+')),
    ('4', lambda: add_to_display('4')),
    ('5', lambda: add_to_display('5')),
    ('6', lambda: add_to_display('6')),
    ('=', calculate),
    ('1', lambda: add_to_display('1')),
    ('2', lambda: add_to_display('2')),
    ('3', lambda: add_to_display('3')),
    ('0', lambda: add_to_display('0')),
    ('.', lambda: add_to_display('.'))
]

row = 1
col = 0
for button_text, command in buttons:
    tk.Button(root, text=button_text, font=('Arial', 20), width=5, height=2, command=command).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()

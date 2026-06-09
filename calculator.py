import math
import tkinter as tk
from tkinter.constants import END

class HoverButton(tk.Button):
    """Button that changes background on hover."""
    def __init__(self, master, **kw):
        super().__init__(master=master, **kw)
        self._default_bg = self["background"]
        self.bind("<Enter>", lambda e: self.config(background=self["activebackground"]))
        self.bind("<Leave>", lambda e: self.config(background=self._default_bg))

# ----------------------------------------------------------------------
# UI setup
# ----------------------------------------------------------------------
ui = tk.Tk()
ui.title("Calculator")
ui.attributes("-topmost", True)

# Icon (optional – will be ignored if the file is missing)
try:
    ui.iconphoto(False, tk.PhotoImage(file="res/icon.png"))
except Exception:
    pass

_lab_label = tk.Label(ui, text=": )", width=5, borderwidth=3)
_lab_label.grid(row=0, column=4, pady=8, columnspan=2)

def set_lab(val):
    _lab_label.config(text=str(val))

e = tk.Entry(
    ui,
    font=("default", 11),
    insertontime=0,
    bd=5,
    width=21,
    borderwidth=10,
    foreground="#ff0000",
    highlightthickness=5,
    highlightcolor="#f5d0d0",
    highlightbackground="#f5d0d0",
)
e.grid(row=0, rowspan=2, column=0, columnspan=4, padx=5, pady=5)
e.bind("<Key>", lambda ev: "break")  # make entry read‑only

_view_label = tk.Label(
    ui,
    borderwidth=3,
    relief="sunken",
    text="Calculations here",
    width=34,
    bg="#f5d0d0",
    fg="#000000",
)
_view_label.grid(row=2, column=0, columnspan=5, pady=5)

def set_view(val):
    _view_label.config(text=str(val))

# ----------------------------------------------------------------------
# Calculator logic
# ----------------------------------------------------------------------
flag = 0          # indicates that the next number entry should clear the display
operator = None   # current operator (+, -, x, /, root, pow)
first_operand = None

def insert_number(num):
    """Insert a digit or decimal point."""
    global flag
    if flag:
        clear_all()
    e.insert(END, str(num))

def set_operator(op):
    """Store the first operand and the chosen operator."""
    global operator, first_operand
    operator = op
    first_operand = e.get()
    e.delete(0, END)

def compute_root():
    """Prepare UI for a root operation."""
    set_operator("root")

def compute_power():
    """Prepare UI for a power operation."""
    set_operator("pow")

def evaluate(_):
    """Perform the pending calculation."""
    global operator, first_operand, flag
    second_operand = e.get()
    try:
        a = float(first_operand)
        b = float(second_operand)
    except (TypeError, ValueError):
        set_view("Error")
        return

    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "x":
        result = a * b
    elif operator == "/":
        result = a / b if b != 0 else float("inf")
    elif operator == "root":
        # second_operand contains the root degree (e.g., "Root of: 3")
        degree = int(second_operand.split()[-1])
        result = a ** (1 / degree)
    elif operator == "pow":
        # second_operand contains the exponent (e.g., "Power of: 4")
        exponent = int(second_operand.split()[-1])
        result = a ** exponent
    else:
        result = b

    # format result (keep integer style when possible)
    if isinstance(result, float) and result.is_integer():
        result = int(result)
    e.delete(0, END)
    e.insert(0, result)
    flag = 1

    # update view label
    if operator in ("root", "pow"):
        op_name = "root" if operator == "root" else "power"
        set_view(f"{first_operand} {op_name} {second_operand} = {result}")
    else:
        set_view(f"{first_operand} {operator} {second_operand} = {result}")

def clear_all():
    """Reset the calculator."""
    global flag, operator, first_operand
    set_lab(": |")
    set_view("Calculations here")
    flag = 1
    operator = None
    first_operand = None
    e.delete(0, END)

# ----------------------------------------------------------------------
# UI button layout
# ----------------------------------------------------------------------
# Operator buttons
HoverButton(ui, bg="#d0c6f5", activebackground="#ffe46b", text="-", padx=18, pady=15,
            command=lambda: set_operator("-")).grid(row=5, column=3)
HoverButton(ui, bg="#d0c6f5", activebackground="#ffe46b", text="x", padx=17, pady=15,
            command=lambda: set_operator("x")).grid(row=4, column=3)
HoverButton(ui, bg="#d0c6f5", activebackground="#ffe46b", text="/", padx=19, pady=8,
            command=lambda: set_operator("/")).grid(row=3, column=3)
HoverButton(ui, bg="#d0c6f5", activebackground="#ffe46b", text="+", padx=15, pady=42,
            command=lambda: set_operator("+")).grid(row=6, column=3, rowspan=2)

# Number buttons
for txt, r, c, colspan in [
    ("7", 4, 0, 1), ("8", 4, 1, 1), ("9", 4, 2, 1),
    ("4", 5, 0, 1), ("5", 5, 1, 1), ("6", 5, 2, 1),
    ("1", 6, 0, 1), ("2", 6, 1, 1), ("3", 6, 2, 1),
    ("0", 7, 0, 2), (".", 7, 2, 1)
]:
    HoverButton(ui, bg="#f5f0f0", activebackground="#73f5d7", text=txt,
                padx=20, pady=15,
                command=lambda t=txt: insert_number(t)).grid(row=r, column=c, columnspan=colspan)

# Miscellaneous buttons
HoverButton(ui, bg="#6699ff", activebackground="#ff4d4d", text="cls",
            padx=15, pady=8, command=clear_all).grid(row=3, column=0)

HoverButton(ui, bg="#d0c6f5", activebackground="#ffe46b", text="√",
            padx=19, pady=8, command=compute_root).grid(row=3, column=1)
HoverButton(ui, bg="#d0c6f5", activebackground="#ffe46b", text="pow",
            padx=10, pady=8, command=compute_power).grid(row=3, column=2)

HoverButton(ui, bg="#c6f5ea", activebackground="#6dff6b", text="=",
            padx=18, pady=115, command=evaluate).grid(row=3, column=4, rowspan=5)

# ----------------------------------------------------------------------
# Final UI tweaks
# ----------------------------------------------------------------------
ui.resizable(False, False)
ui.mainloop()

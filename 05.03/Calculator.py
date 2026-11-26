import math
import tkinter as tk
from tkinter import *

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def multi(a, b): 
    return a * b
def div(a, b):
    if b == 0: 
        raise ValueError("деление на ноль невозможно")
    else:
        return a / b
def exponentiate(a, b):
    if a == 0 and b <= 0:
        raise ValueError("не определен")
    else:
        return a ** b
def square(num):
    if num < 0: 
        raise ValueError("не определен")
    else:
        return math.sqrt(num)
def factorial(num):
    if not isinstance(num, int) or num < 0:
        raise ValueError("некорректный факториал")
    else:
        return math.factorial(num)

memory = 0
def memory_save(num):
    global memory
    memory = num
def memory_read():
    return memory
def memory_add(num):
    global memory
    memory += num
def memory_clear():
    global memory
    memory = 0
    print(memory_clear)

wnd = tk.Tk()
wnd.title("Калькулятор")
wnd.geometry("285x430")
wnd.resizable(False, False)

wnd.configure(bg="#355A1C")

display = tk.Entry(wnd, font=("Arial", 20), justify="right",bg="#000000", fg="#FFFFFF")
display.pack(fill="x", padx=8, pady=8)
display.insert(0, "0")

first = {"value": None}
op = {"fn": None}

def current():
    try:
        return float(display.get())
    except ValueError:
        return 0.0

def setting(n):
    display.delete(0, tk.END)
    display.insert(0, str(n))

def press_digit(d):
    txt = display.get()
    if op.get("waiting"):
        setting(d)
        op["waiting"] = False
    elif txt == "0" or txt.startswith("ошибка"):
        setting(d)
    else:
        setting(txt + d)

def press_dot():
    if "." not in display.get():
        setting(display.get() + ".")

def negate():
    txt = display.get()
    if txt.startswith("-"):
        setting(txt[1:])
    else:
        setting("-" + txt)

def press_op(fn):
    first["value"] = current()
    op["fn"] = fn
    op["waiting"] = True

def press_eq():
    if op["fn"] is None:
        return
    a = first["value"]
    if not op.get("waiting"):
        b = current()
    else:
        b = 0
    try:
        setting(op["fn"](a, b))
    except Exception as e:
        setting(e)
    op["fn"] = None
    op["waiting"] = False

def unary(fn):
    try:
        setting(fn(current()))
    except Exception as e:
        setting(e)

def mem_op(fn):
    try:
        fn(current())
        setting(memory_read())
    except Exception as e:
        setting(e)

def clear_all():
    first["value"] = None
    op["fn"] = None
    setting("0")

layout = [("MA", lambda: mem_op(memory_add)),("MC", lambda: memory_clear()),("MR", lambda: setting(memory_read())),("MS", lambda: mem_op(memory_save)),
          ("x^y", lambda: press_op(exponentiate)),("√", lambda: unary(square)),("n!", lambda: unary(lambda x: factorial(int(x)))),("/", lambda: press_op(div)),
          ("7",  lambda: press_digit("7")),("8", lambda: press_digit("8")),("9", lambda: press_digit("9")),("*", lambda: press_op(multi)),
          ("4",  lambda: press_digit("4")),("5", lambda: press_digit("5")),("6", lambda: press_digit("6")),("-", lambda: press_op(sub)),
          ("1",  lambda: press_digit("1")),("2", lambda: press_digit("2")),("3", lambda: press_digit("3")),("+", lambda: press_op(add)),
          ("C",  clear_all),("0",  lambda: press_digit("0")),(".", press_dot),("+/-", negate)]

frame = tk.Frame(wnd, bg="#355A1C")
frame.pack(padx=6, pady=6, fill="both", expand=True)

for i, (text, cmd) in enumerate(layout):
    r, col = divmod(i, 4)
    tk.Button(frame, text=text, font=("Arial", 12), width=6, height=2,bg="#649757", fg="#000000",activebackground="#649757",command=cmd).grid(row=r, column=col, padx=2, pady=2)

tk.Button(wnd, text="=", font=("Arial", 14), height=2, bg="#649757", fg="#000000", activebackground="#649757",command=press_eq).pack(fill="x", padx=8, pady=(0, 8))

wnd.mainloop()
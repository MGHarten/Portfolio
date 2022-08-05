from tkinter import *

# create a calculator
window = Tk()
window.geometry("225x275")
window.title("Calculator")

//create buttons for calculator and assign them functions


def button_click(button):
    global Equation
    Equation = Equation + str(button)
    input_bar_text.set(Equation)


def button_clear():
    global Equation
    Equation = ""
    input_bar_text.set("")


def button_equals():
    global Equation
    result = str(eval(Equation))
    input_bar_text.set(result)
    Equation = ""


# create input box for calculator
Equation = ""
input_bar_text = StringVar()

# Input box setup

input_frame = Frame(window, width=225).pack(side=TOP)

input_box = Entry(input_frame, font=('arial', 18, 'bold'), text=input_bar_text)
input_box.pack()

# Buttons Frame

button_frame = Frame(window, width=225, height=245)
button_frame.pack()

# Numeric Button Grid

Button(button_frame, text="7", width=5, height=2, command=lambda: button_click(7)).grid(
    row=1, column=0, padx=1, pady=1)
Button(button_frame, text="8", width=5, height=2, command=lambda: button_click(8)).grid(
    row=1, column=1, padx=1, pady=1)
Button(button_frame, text="9", width=5, height=2, command=lambda: button_click(9)).grid(
    row=1, column=2, padx=1, pady=1)
Button(button_frame, text="*", width=5, height=2, command=lambda: button_click("*")).grid(
    row=1, column=3, padx=1, pady=1)

Button(button_frame, text="4", width=5, height=2, command=lambda: button_click(4)).grid(
    row=2, column=0, padx=1, pady=1)
Button(button_frame, text="5", width=5, height=2, command=lambda: button_click(5)).grid(
    row=2, column=1, padx=1, pady=1)
Button(button_frame, text="6", width=5, height=2, command=lambda: button_click(6)).grid(
    row=2, column=2, padx=1, pady=1)
Button(button_frame, text="-", width=5, height=2, command=lambda: button_click("-")).grid(
    row=2, column=3, padx=1, pady=1)

Button(button_frame, text="1", width=5, height=2, command=lambda: button_click(1)).grid(
    row=3, column=0, padx=1, pady=1)
Button(button_frame, text="2", width=5, height=2, command=lambda: button_click(2)).grid(
    row=3, column=1, padx=1, pady=1)
Button(button_frame, text="3", width=5, height=2, command=lambda: button_click(3)).grid(
    row=3, column=2, padx=1, pady=1)
Button(button_frame, text="+", width=5, height=2, command=lambda: button_click("+")).grid(
    row=3, column=3, padx=1, pady=1)

Button(button_frame, text="0", width=5, height=2, command=lambda: button_click(0)).grid(
    row=4, column=0, padx=1, pady=1)
Button(button_frame, text="C", width=5, height=2, command=button_clear).grid(
    row=4, column=1, padx=1, pady=1)

Button(button_frame, text="=", width=5, height=2, command=button_equals).grid(
    row=4, column=2, padx=1, pady=1)
Button(button_frame, text="/", width=5, height=2, command=lambda: button_click("/")).grid(
    row=4, column=3, padx=1, pady=1)

window.mainloop()

import tkinter as tk

calculation = ""


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)

    except:
        clear_field()
        text_result.delete(1.0, "Error")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root = tk.Tk()
root.geometry("235x350")
root.title("Calculator")

text_result = tk.Text(root, font=("Courier New", 12, 'bold'), width=22, height=2, bd=5)
text_result.grid(columnspan=9)
root.config(background='Black')


btn_1 = tk.Button(root, bd=4, bg='white', text="1", command=lambda: add_to_calculation(1),
                  width=4, height=2, font=("Arial", 14,))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, bd=4, bg='white', text="2", command=lambda: add_to_calculation(2),
                  width=4, height=2, font=("Arial", 14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, bd=4, bg='white', text="3", command=lambda: add_to_calculation(3),
                  width=4, height=2, font=("Arial", 14))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, bd=4, bg='white', text="4", command=lambda: add_to_calculation(4),
                  width=4, height=2, font=("Arial", 14))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, bd=4, bg='white', text="5", command=lambda: add_to_calculation(5),
                  width=4, height=2, font=("Arial", 14))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, bd=4, bg='white', text="6", command=lambda: add_to_calculation(6),
                  width=4, height=2, font=("Arial", 14))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, bd=4, bg='white', text="7", command=lambda: add_to_calculation(7),
                  width=4, height=2, font=("Arial", 14))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, bd=4, bg='white', text="8", command=lambda: add_to_calculation(8),
                  width=4, height=2, font=("Arial", 14))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, bd=4, bg='white', text="9", command=lambda: add_to_calculation(9),
                  width=4, height=2, font=("Arial", 14))
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, bd=4, bg='white', text="0", command=lambda: add_to_calculation(0),
                  width=4, height=2, font=("Arial", 14))
btn_0.grid(row=5, column=2)
btn_plus = tk.Button(root, bd=4, bg='white', text="+", command=lambda: add_to_calculation("+"),
                     width=4, height=2, font=("Arial", 14))
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(root, bd=4, bg='white', text="-", command=lambda: add_to_calculation("-"),
                      width=4, height=2, font=("Arial", 14))
btn_minus.grid(row=3, column=4)
btn_mult = tk.Button(root, bd=4, bg='white', text="*", command=lambda: add_to_calculation("*"),
                     width=4, height=2, font=("Arial", 14))
btn_mult.grid(row=4, column=4)
btn_div = tk.Button(root, bd=4, bg='white', text="/", command=lambda: add_to_calculation("/"),
                    width=4, height=2, font=("Arial", 14))
btn_div.grid(row=5, column=4)
btn_left = tk.Button(root, bd=4, bg='white', text="(", command=lambda: add_to_calculation("("),
                     width=4, height=2, font=("Arial", 14))
btn_left.grid(row=5, column=1)
btn_right = tk.Button(root, bd=4, bg='white', text=")", command=lambda: add_to_calculation(")"),
                      width=4, height=2, font=("Arial", 14))
btn_right.grid(row=5, column=3)
btn_clear = tk.Button(root, bd=4, text="Ce", command=clear_field, width=9, bg='#e01e3e',
                      font=("Arial", 14,))
btn_clear.grid(row=6, column=1, columnspan=2)
btn_equal = tk.Button(root, bd=4, bg='white', text="=", command=evaluate_calculation,
                      width=9, font=("Arial", 14))
btn_equal.grid(row=6, column=3, columnspan=2)
root.mainloop()


# E3RO-TECH-Inc

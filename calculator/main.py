import math
import tkinter as tk


class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.display = tk.Entry(master, width=20, font=("Arial", 20))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+",
            "sin", "cos", "tan", "log",
            "pi", "e", "(", ")",
            "sqrt", "^", "!", "abs"
        ]

        row = 1
        col = 0
        for button in buttons:
            tk.Button(master, text=button, width=5, height=2, font=("Arial", 15),
                      command=lambda x=button: self.button_click(x)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

        tk.Button(master, text="=", width=5, height=2, font=("Arial", 15),
                  command=self.calculate).grid(row=5, column=2, padx=5, pady=5)

    def button_click(self, symbol):
        current = self.display.get()
        if symbol == "C":
            self.display.delete(0, tk.END)
        elif symbol == ".":
            if "." not in current:
                self.display.insert(tk.END, symbol)
        elif symbol in ["sin", "cos", "tan", "log", "sqrt", "abs", "pi", "e", "(", ")"]:
            self.display.insert(tk.END, symbol)
        elif symbol == "^":
            self.display.insert(tk.END, "**")
        elif symbol == "!":
            if current and current[-1].isdigit():
                self.display.insert(tk.END, "*factorial(")
            else:
                self.display.insert(tk.END, "factorial(")
        else:
            self.display.insert(tk.END, symbol)

    def calculate(self):
        expression = self.display.get()
        try:
            expression = expression.replace("sin", "math.sin")
            expression = expression.replace("cos", "math.cos")
            expression = expression.replace("tan", "math.tan")
            expression = expression.replace("log", "math.log10")
            expression = expression.replace("sqrt", "math.sqrt")
            expression = expression.replace("abs", "math.fabs")
            expression = expression.replace("pi", "math.pi")
            expression = expression.replace("e", "math.e")
            expression = expression.replace("factorial", "math.factorial")
            result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except ZeroDivisionError:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error: Division by zero")
        except ValueError as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error: " + str(e))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error: " + str(e))


root = tk.Tk()
gui = CalculatorGUI(root)
root.mainloop()

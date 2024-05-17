import tkinter as tk

def gui():
    WIDTH = 172
    HEIGHT = 285
    root = tk.Tk()
    root.title("Calculator")
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.resizable(False, False) 

    label_frame = tk.Frame(root, bg="black")
    label_frame.grid(row=0, column=0, columnspan=4, sticky="ew")

    label = tk.Label(label_frame, text='', bg="black", fg="white", font=("Arial", 24), anchor='e')
    label.pack(fill="both")  

    button_frame = tk.Frame(root, bg="black")
    button_frame.grid(row=1, column=0, columnspan=4)

    button_C = tk.Button(button_frame, text="C", bg="gray", fg="white", font=("Arial", 18),
                         command=lambda: delete_all(label))
    button_C.grid(row=1, column=0, sticky="nsew", padx=1, pady=1)
    
    button_sign = tk.Button(button_frame, text="+/-", bg="gray", fg="white", font=("Arial", 18),
                            command=lambda: calc("+/-"))
    button_sign.grid(row=1, column=1, sticky="nsew", padx=1, pady=1)
    
    button_percent = tk.Button(button_frame, text="%", bg="gray", fg="white", font=("Arial", 18),
                               command=lambda: calc("%"))
    button_percent.grid(row=1, column=2, sticky="nsew", padx=1, pady=1)
    
    button_div = tk.Button(button_frame, text="/", bg="orange", fg="white", font=("Arial", 18),
                           command=lambda: (updatetext(label, "/"), calc("/")))
    button_div.grid(row=1, column=3, sticky="nsew", padx=1, pady=1)


    button_7 = tk.Button(button_frame, text="7", bg="dark gray", fg="white", font=("Arial", 18),
                         command=lambda: (updatetext(label, "7"), calc("7")))
    button_7.grid(row=2, column=0, sticky="nsew", padx=1, pady=1)

    button_8 = tk.Button(button_frame, text="8", bg="dark gray", fg="white", font=("Arial", 18),
                         command=lambda: (updatetext(label, "8"), calc("8")))
    button_8.grid(row=2, column=1, sticky="nsew", padx=1, pady=1)

    button_9 = tk.Button(button_frame, text="9", bg="dark gray", fg="white", font=("Arial", 18),
                         command=lambda: (updatetext(label, "9"), calc("9")))
    button_9.grid(row=2, column=2, sticky="nsew", padx=1, pady=1)

    button_mul = tk.Button(button_frame, text="*", bg="orange", fg="white", font=("Arial", 18),
                           command=lambda: (updatetext(label, "*"), calc("*")))
    button_mul.grid(row=2, column=3, sticky="nsew", padx=1, pady=1)

    button_4 = tk.Button(button_frame, text="4", bg="dark gray", fg="white", font=("Arial", 18),
                         command=lambda: (updatetext(label, "4"), calc("4")))
    button_4.grid(row=3, column=0, sticky="nsew", padx=1, pady=1)

    button_5 = tk.Button(button_frame, text="5", bg="dark gray", fg="white", font=("Arial", 18),
                         command=lambda: (updatetext(label, "5"), calc("5")))
    button_5.grid(row=3, column=1, sticky="nsew", padx=1, pady=1)

    button_6 = tk.Button(button_frame, text="6", bg="dark gray", fg="white", font=("Arial", 18),
                         command=lambda: (updatetext(label, "6"), calc("6")))
    button_6.grid(row=3, column=2, sticky="nsew", padx=1, pady=1)

    button_sub = tk.Button(button_frame, text="-", bg="orange", fg="white", font=("Arial", 18),
                           command=lambda: (updatetext(label, "-"), calc("-")))
    button_sub.grid(row=3, column=3, sticky="nsew", padx=1, pady=1)

    button_1 = tk.Button(button_frame, text="1", bg="dark gray", fg="white", font=("Arial", 18),
                         command=lambda: (updatetext(label, "1"), calc("1")))
    button_1.grid(row=4, column=0, sticky="nsew", padx=1, pady=1)

    button_2 = tk.Button(button_frame, text="2", bg="dark gray", fg="white", font=("Arial", 18),
                         command=lambda: (updatetext(label, "2"), calc("2")))
    button_2.grid(row=4, column=1, sticky="nsew", padx=1, pady=1)

    button_3 = tk.Button(button_frame, text="3", bg="dark gray", fg="white", font=("Arial", 18),
                         command=lambda: (updatetext(label, "3"), calc("3")))
    button_3.grid(row=4, column=2, sticky="nsew", padx=1, pady=1)

    button_add = tk.Button(button_frame, text="+", bg="orange", fg="white", font=("Arial", 18),
                           command=lambda: (updatetext(label, "+"), calc("+")))
    button_add.grid(row=4, column=3, sticky="nsew", padx=1, pady=1)

    button_0 = tk.Button(button_frame, text="0", bg="dark gray", fg="white", font=("Arial", 18),
                         command=lambda: (updatetext(label, "0"), calc("0")))
    button_0.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=1, pady=1)

    button_dot = tk.Button(button_frame, text=".", bg="dark gray", fg="white", font=("Arial", 18),
                           command=lambda: (updatetext(label, "."), calc(".")))
    button_dot.grid(row=5, column=2, sticky="nsew", padx=1, pady=1)

    button_eq = tk.Button(button_frame, text="=", bg="orange", fg="white", font=("Arial", 18),
                          command=lambda: evaluate(label))
    button_eq.grid(row=5, column=3, sticky="nsew", padx=1, pady=1)

    root.mainloop()

def updatetext(label, t):
    current_text = label.cget("text")
    new_text = current_text + t
    
    if len(new_text) <10:
         label.config(text=new_text)
    else:
         label.config(text="ERROR")



def calc(str):
    pass

def evaluate(label):
    try:
        expression = label.cget("text")
        result = eval(expression) 
        label.config(text=str(result))
    except Exception as e:
        label.config(text="Error")

def delete(label):
    current_text = label.cget("text")
    updated_text = current_text[:-1]
    label.config(text=updated_text)

def delete_all(label):
    label.config(text="")

gui()

import tkinter as tk

def gui():
    WIDTH = 340
    HEIGHT = 500
    root = tk.Tk()
    root.title("Calculator")
    root.geometry(f"{WIDTH}x{HEIGHT}")
    
    # Frame for the label
    label_frame = tk.Frame(root, bg="black")
    label_frame.grid(row=0, column=0, columnspan=4, sticky="ew")
    
    # Create the label inside the label frame
    label = tk.Label(label_frame, text='This is a label', bg="black", fg="white", width=40, height=10)
    label.pack(fill="both")  
    
    # Frame for the buttons
    button_frame = tk.Frame(root)
    button_frame.grid(row=1, column=0, columnspan=4)  # Removed sticky="nsew"
    
    # Disable expansion for all rows and columns
    for i in range(2):  # Two rows
        root.grid_rowconfigure(i, weight=0)
    for i in range(4):  # Four columns
        root.grid_columnconfigure(i, weight=0)
    
    # Define buttons
    buttons = [
        ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
        ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
        ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
        ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3)
    ]

    # Create and place buttons inside the button frame
    for text, row, column in buttons:
        button = tk.Button(button_frame, text=text, bg="light blue", height=7, width=11)
        button.grid(row=row, column=column, pady=0, padx=0)

    root.mainloop()

gui()

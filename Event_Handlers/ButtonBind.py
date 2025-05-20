import tkinter as tk

window = tk.Tk()

def handler_click(event):
    print("Button clicked!")

button = tk.Button(window, text="Click me.")
button.pack()

button.bind("<Button-1>", handler_click)

window.mainloop()

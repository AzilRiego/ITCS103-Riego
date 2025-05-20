import tkinter as tk

window = tk.Tk()
window.geometry('300x300')
window.title("Login")

label = tk.Label(master = window, text = "Login", font = "Calibary 10 bold")
label.pack()

entry = tk.Entry()
entry.pack()

entry = tk.Entry()
entry.pack()

button = tk.Button(master = window, text = "Login")
button.pack()

def handler_click(event):
    print("Someone tried to log in.")

button.bind("<Button-1>", handler_click)

button = tk.Button(master = window, text = "Create account")
button.pack()

window.mainloop()
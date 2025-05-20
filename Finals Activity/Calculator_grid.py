import tkinter as tk

window = tk.Tk()

window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,], minsize=20, weight=1)
window.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], minsize=20, weight=1)

entry = tk.Entry(master = window)
entry.grid(row=1, column=1, columnspan=8)

Label = tk.Label(master = window, text =" ")
Label.grid(row=2, column=1, columnspan=8)

entry = tk.Entry(master = window)
entry.grid(row=3, column=1, columnspan=8)

Label = tk.Label(master = window, text =" ")
Label.grid(row=4, column=1, columnspan=8)

button = tk.Button(master = window, text = "7")
button.grid(row=5, column=1)

button = tk.Button(master = window, text = "8")
button.grid(row=5, column=2)

button = tk.Button(master = window, text = "9")
button.grid(row=5, column=3)

button = tk.Button(master = window, text = "/")
button.grid(row=5, column=4)

button = tk.Button(master = window, text = "4")
button.grid(row=6, column=1)

button = tk.Button(master = window, text = "5")
button.grid(row=6, column=2)

button = tk.Button(master = window, text = "6")
button.grid(row=6, column=3)

button = tk.Button(master = window, text = "-")
button.grid(row=6, column=4)

button = tk.Button(master = window, text = "1")
button.grid(row=7, column=1)

button = tk.Button(master = window, text = "2")
button.grid(row=7, column=2)

button = tk.Button(master = window, text = "3")
button.grid(row=7, column=3)

button = tk.Button(master = window, text = "+")
button.grid(row=7, column=4)

button = tk.Button(master = window, text = "0")
button.grid(row=8, column=1)

button = tk.Button(master = window, text = "=")
button.grid(row=8, column=1, columnspan=9)

window.mainloop()

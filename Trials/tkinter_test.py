import tkinter as tk

window = tk.Tk()
window.geometry('300x300')
window.title("TEST")

#Label
Label = tk.Label(master = window, text = "Clicking the button does nothing.", font = "Calibary 30 bold")
Label.pack()

#Button
button = tk.Button(master = window, text = "Click")
button.pack()

#Label 2
Label = tk.Label(master = window, text = "Neither does typing something.", font = "Calibary 10 bold")
Label.pack()

#Type
entry = tk.Entry(master = window)
entry.pack()

window.mainloop()
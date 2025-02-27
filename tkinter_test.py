import tkinter as tk

window = tk.Tk()
window.geometry('300x300')
window.title("TEST")

#Label
Label = tk.Label(master = window, text = "Clicking the button does nothing.", font = "Calibary 10 bold")
Label.pack()

button = tk.Button(master = window, text = "Click")
button.pack()

Label = tk.Label(master = window, text = "Neither does typigng something.", font = "Calibary 5 bold")
Label.pack()

entry = tk.Entry(master = window)
entry.pack()

window.mainloop()
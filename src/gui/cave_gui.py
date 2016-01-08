import tkinter
from tkinter import Canvas


main = tkinter.Tk()

w = Canvas(main, width=200, height=100)
w.create_line(10,10, 200, 10, fill="#000000", width=1)
w.pack()


main.mainloop()

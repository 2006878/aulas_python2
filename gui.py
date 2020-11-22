from tkinter import Tk, Label, PhotoImage
root = Tk()
photo = PhotoImage(file='computer.gif')
hello = Label(master=root, image=photo, width=300, height=180)
hello.pack()
root.mainloop()
from tkinter import Tk, Label, PhotoImage, BOTTOM, LEFT, RIGHT, RIDGE
raiz = Tk()

texto = Label(raiz, font=('Helvetica', 16, 'bold italic'), foreground='white', background='black', padx=25, pady=10, text='A Paz começa com um sorriso.')
texto.pack(side=BOTTOM)
peace = PhotoImage(file='peace.gif')
peaceLabel = Label(raiz, borderwidth=3, relief=RIDGE, image = peace)
peaceLabel.pack(side=LEFT)

smilei = PhotoImage(file='smile.gif')
smileiLabel = Label(raiz, image=smilei)
smileiLabel.pack(side=RIGHT)

raiz.mainloop
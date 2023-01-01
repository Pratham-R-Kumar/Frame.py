from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images")

img = ImageTk.PhotoImage(Image.open("Sample.jpg"))
lab = Label(image=img)
lab.pack()


bt = Button(root, text="Exit", command=root.quit)
bt.pack()

root.mainloop()
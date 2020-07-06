from tkinter import *
from PIL import Image, ImageTk
root = Tk()
#GUI Logic here!
root.geometry("600x600") #WxH
root.minsize(200,200)
root.title("image")
# #-----------------For JPG FILES-------------------#
# image = Image.open("1.jpg")
# photo = ImageTk.PhotoImage(image)

photo = PhotoImage(file="1.png")

label = Label(text="SShameel",image=photo)
label.pack()


root.mainloop()

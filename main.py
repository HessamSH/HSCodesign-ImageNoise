from tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np

dir = "pic.jpg"

img = cv2.imread(dir)
noise = np.random.normal(0,1,img.size)
noise = noise.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')
img_noise = cv2.add(img,noise)
cv2.imwrite("noised.jpg", img_noise)

b,g,r = cv2.split(img_noise)
img_noise = cv2.merge((r,g,b))
# cv2.imshow('a',img_noise)
# cv2.waitKey(0)


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        load = Image.open(dir)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=20, y=20)

        im = Image.fromarray(img_noise)
        imgtk = ImageTk.PhotoImage(image=im)
        imgNoised = Label(self, image=imgtk)
        imgNoised.image = imgtk
        imgNoised.place(x=450, y=20)

root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.geometry("900x360")
root.mainloop()
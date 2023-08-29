from tkinter import *
import random, time

"""Code of the game"""


def throw():
    x = random.choice(['b1.png', 'b2.png', 'b3.png', 'b4.png', 'b5.png', 'b6.png'])
    return x


def img(event):
    global b1, b2
    for i in range(20):
        b1 = PhotoImage(file=throw())
        b2 = PhotoImage(file=throw())
        lab1['image'] = b1
        lab2['image'] = b2
        root.update()
        time.sleep(0.12)


"""Intrface of the game"""
root = Tk()
root.geometry('400x200')
root.title('Dice game) Make your throw')
root.resizable(height=False, width=False)  # block changing window shape
root.iconphoto(True, PhotoImage(file='G:\\Python\\PycharmProjects\\Dice_game\\ico.png'))
font = PhotoImage(file='G:\\Python\\PycharmProjects\\Dice_game\\background.png')
Label(root, image=font).pack()

lab1 = Label(root)  # pleasing buttons
lab1.place(relx=0.3, rely=0.5, anchor=CENTER)
lab2 = Label(root)  # pleasing buttons
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)

# Button(root, text='Throw', command=img).pack()

root.bind('<1>', img)
img('event')

root.mainloop()

5:55:36

#import module
from tkinter import *

# initialize window
root = Tk()
root.geometry('300x300')
root.title('Mad Libs Generator')
Label(root, text= 'Final Project - Mad Libs Generator \n Have Fun!' , font = 'arial 20 bold').pack()
Label(root, text = 'Click One!', font = 'arial 15 bold').place(x=40, y=80)

Button(root, text= 'The Photographer', font ='arial 15', command= madlib1, bg = 'ghost white').place(x=60, y=120)
Button(root, text= 'apple and apple', font ='arial 15', command = madlib3 , bg = 'ghost white').place(x=70, y=180)
Button(root, text= 'The Butterfly', font ='arial 15', command = madlib2, bg = 'ghost white').place(x=80, y=240)

root.mainloop()
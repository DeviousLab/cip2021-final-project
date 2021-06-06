#import module
from tkinter import *

# initialize window
root = Tk()
root.title('Mad Libs Generator')

# creates input fields for user to enter words
label1 = Label(root, text='Final Project Mad Libs Generator \n Enter your words below!', font=('helvetica', 20))
label1.pack()

frame = Frame(root)
frame.pack()

lst = ['Adverb', 'Noun', 'Liquid', 'Verb', 'Number', 'Noun(Plural)', 'Verb', 'Adjective', 'Noun', 'Verb', 'Adjective', 'Noun(Plural)', 'Illness','Occupation', 'Body part(plural)', 'Body part']

entries = []

for row, x in enumerate(lst):
    Label(frame, text=f'{x}:').grid(row=row, column=0)
    ent = Entry(frame)
    ent.grid(row=row, column=1)
    entries.append(ent)


# function that retrieves words and transfers them into the story
def generateMadLib():
    story = 'In order to wash your face {0}, you must wet your {1} in warm {2}.\n Then, {3}'\
'it across your face {4} times. This will wash off any remaining {5}.\n When you'\
'are done you should {6} the cloth in {7} water to clean it. \nYou should also wash'\
'your face with a {8} to keep it smooth and shiny.\n This will keep also keep away'\
'{9}. Don`t worry. \n It is normal to experience {10} the first time you try this.\n'\
'Consult your {11} if you break out in {12}. ' \
'This works well on your {13} too! '.format(*(x.get() for x in entries))

    label3 = Label(root, text='Here is your Mad Lib!', font='helvetica')
    label3.pack()

    label4 = Label(root, text=story)
    label4.pack()

# button that calls the function to generate the completed story
button1 = Button(root, text='Generate  Lib!', command=generateMadLib, bg='red', fg='white', font=('helvetica', 9, 'bold'))
button1.pack()

root.mainloop()
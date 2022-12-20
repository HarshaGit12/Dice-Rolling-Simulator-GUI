import tkinter
from PIL import Image, ImageTk
import random

root = tkinter.Tk()
root.geometry('500x500')
root.title('Dice Rolling Simulator - GUI')

BlankLine = tkinter.Label(root, text="")
BlankLine.pack()

HeadingLabel = tkinter.Label(root, text="Hello, Welcome to the Dice Rolling Simulator!",
   fg = "light blue",
     bg = "dark blue",
     font = "Helvetica 14 bold italic")
HeadingLabel.pack()
# images
dice = ['die1.png', 'die2.png', 'die3.png', 
    'die4.png', 'die5.png', 'die6.png']

DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage
 
ImageLabel.pack( expand=True)

def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    
    ImageLabel.configure(image=DiceImage)
    
    ImageLabel.image = DiceImage

button = tkinter.Button(root, text='Roll the Dice', fg='light green', bg = 'dark green', command=rolling_dice)

button.pack( expand=True)


root.mainloop()

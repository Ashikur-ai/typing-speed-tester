words = ['Grapes', 'Mango', 'Apple', 'gun', 'fan', 'door', 'tv', 'mobile','laptop']

def LabelSlider():
    global count, sliderWords
    text = 'Welcome to typing Speed Increaser'
    if count >= len(text):
        count = 0
        sliderWords = ''
    sliderWords += text[count]
    count += 1
    fontLabel.configure(text=sliderWords)
    fontLabel.after(150, LabelSlider)

def time():
    global timeleft, score, miss
    if timeleft >= 11:
        pass
    else:
        timerLabelCount.configure(fg='red')
        
    if timeleft > 0:
        timeleft -= 1
        timerLabelCount.configure(text=timeleft)
        timerLabelCount.after(1000,time)
    else:
        gamePlayDetailLabel.configure(text='Hit = {} | Miss = {} | Total Score = {}'.format(score, miss, score-miss))
        rr = messagebox.askretrycancel('Notification', 'For play again hit Retry')
        if rr == True:
            score = 0
            timeleft = 60
            miss = 0
            timerLabelCount.configure(text=timeleft)
            wordLabel.configure(text=words[0])
            scoreLabel_count.configure(text=score)


def startGame(event):
    global score, miss
    if timeleft == 60:
        time()

    gamePlayDetailLabel.configure(text='')
    if wordEntry.get() == wordLabel['text']:
        score += 1
        scoreLabel_count.configure(text=score)
    else:
        miss += 1

    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0, END)


from tkinter import *
import random
from tkinter import messagebox
################################# root method########
root = Tk()
root.geometry('800x600+400+100')
root.configure(bg='powder blue')
root.title('Typing Speed Increaser Game')
root.iconbitmap('icon.ico')

################### Variable ########
score = 0
timeleft = 60
count = 0
sliderWords = ''
miss = 0
#################### Label method #############
fontLabel = Label(root, text='', font=('Berlin Sans FB Demi', 30), bg = 'powder blue', width=30)
fontLabel.place(x=10, y=10)
LabelSlider()
random.shuffle(words)

wordLabel = Label(root, text=words[0], font=('Berlin Sans FB Demi',40), justify='center')
wordLabel.place(x=310, y=300)

scoreLabel = Label(root, text='Your Score:', font=('Berlin Sans FB Demi',40), bg='powder blue')
scoreLabel.place(x=10, y=140)

scoreLabel_count= Label(root, text=score, font=('Berlin Sans FB Demi', 40), bg='powder blue')
scoreLabel_count.place(x=300, y=140)

timerLabel = Label(root, text='Time left:', font=('Berlin Sans FB Demi', 40), bg='powder blue')
timerLabel.place(x=470, y=140)

timerLabelCount = Label(root, text=timeleft, font=('Berlin Sans FB Demi', 40), bg='powder blue')
timerLabelCount.place(x=700, y=140)

gamePlayDetailLabel = Label(root, text='Type word and hit enter button',
                            font=('Berlin Sans FB Demi', 30), bg='powder blue')
gamePlayDetailLabel.place(x=120, y=500)
################ Entry Method ##################
wordEntry = Entry(root, font=('Berlin Sans FB Demi', 40), justify='center')
wordEntry.place(x=70, y=400)
wordEntry.focus_set()
##################
root.bind('<Return>', startGame)


root.mainloop()
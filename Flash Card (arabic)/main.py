from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#C6EBC5"
current_card ={}

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("arabic_words.csv")
    arabic_words = data.to_dict(orient="records")
else:
    arabic_words = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(arabic_words)
    canvas.itemconfig(title_text,text="Arabic", fill="black")
    canvas.itemconfig(word_text,text=current_card["ARABIC"], fill="black")
    canvas.itemconfig(front_img,image=card_front_img)
    flip_timer = window.after(3000,func=flip_card)


def flip_card():
    canvas.itemconfig(front_img, image=card_back_img)
    canvas.itemconfig(title_text, text="English", font=("Arial",40,"italic"), fill="white")
    canvas.itemconfig(word_text, text=current_card["ENGLISH"], font=("Arial", 60, "bold"), fill="white")


def is_known():
    arabic_words.remove(current_card)
    data = pandas.DataFrame(arabic_words)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()



#-------------------------------------UI---------------------------------------#

window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width= 800, height= 526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file= "images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
front_img = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)
title_text= canvas.create_text(400,150,text="", font=("Arial",40,"italic"))
word_text = canvas.create_text(400,263,text="", font=("Arial",60,"bold"))
canvas.grid(column=0, row=0)

#-------------BUTTONS---------------#

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(column=1, row=1)


wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)


next_card()


window.mainloop()










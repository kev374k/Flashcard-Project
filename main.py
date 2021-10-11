from tkinter import *
from tkinter import Canvas
import pandas as pd
import random

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
HONEYDEW = "#F0FFF0"

# -------------------------------------------------
# Lists
new_data = pd.read_csv(
    "/Users/kevinwong/Python Projects/Small Python Games + Programs/Flash Card Capstone Project - Day 31/csv files/chinesewords100.csv"
)
chinese_pinyin = new_data["Chinese Pronunciation"]
english_meanings = new_data["English Definition"]
try:
    data = pd.read_csv(
        "/Users/kevinwong/Python Projects/Small Python Games + Programs/Flash Card Capstone Project - Day 31/csv files/words_to_learn.csv"
    )
except FileNotFoundError:
    data = pd.read_csv(
        "/Users/kevinwong/Python Projects/Small Python Games + Programs/Flash Card Capstone Project - Day 31/csv files/chinesewords100.csv"
    )
to_learn = data.to_dict(orient="records")
# ---------------------------------------------------
# Implementation of Pandas Data

# data = pd.read_csv('1000chinesewords.csv')
# Most common Chinese Words
# chinese_words = data['Chinese']
# Pinyin that relate to those words
# chinese_pinyin = data["Pinyin"]
# The meaning of those words in English
# english_meanings = data['Definition']

"""Created simpler data(.csv) to interpret into real data"""
# simple_data = {
#     "Chinese Words": chinese_words,
#     "Chinese Pronunication": chinese_pinyin,
#     "English Definition": english_meanings
# }
# frame = pd.DataFrame(simple_data)
# frame.to_csv('chinesewords.csv')

# words_known = {
#     "Words": []
# }
# frame = pd.DataFrame(words_known)
# frame.to_csv('/Users/kevinwong/Python Projects/Small Python Games + Programs/Flash Card Capstone Project - Day 31/csv files/known_words.csv')

# words_unknown = {
#     "Words": chinese_words
# }
# frame2 = pd.DataFrame(words_unknown)
# frame2.to_csv('/Users/kevinwong/Python Projects/Small Python Games + Programs/Flash Card Capstone Project - Day 31/csv files/unknown_words.csv')
# -------------------------------------------------
def change_words_right():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(
        card_word,
        text=current_card["Traditional"],
        fill="black",
        font=("Arial", 60, "bold"),
    )
    canvas.itemconfig(card_title, text="Chinese", fill="black")
    canvas.itemconfig(card_pinyin, text="", fill="black")
    flip_timer = window.after(3000, func=switch)
    to_learn.remove(current_card)
    data_to_learn = pd.DataFrame(to_learn)
    data_to_learn.to_csv(
        "/Users/kevinwong/Python Projects/Small Python Games + Programs/Flash Card Capstone Project - Day 31/csv files/words_to_learn.csv",
        index=False,
    )
    # dataframe_dict = {
    #     "Traditional": [current_card["Traditional"]],
    #     "Pinyin": [current_card['Chinese Pronunciation']],
    #     "Meaning": [current_card["English Definition"]]
    # }

    # dataframe = pd.DataFrame(dataframe_dict)
    # dataframe.to_csv('known_words.csv')


def change_words_wrong():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(
        card_word,
        text=current_card["Traditional"],
        fill="black",
        font=("Arial", 60, "bold"),
    )
    canvas.itemconfig(card_title, text="Chinese", fill="black")
    canvas.itemconfig(card_pinyin, text="", fill="black")
    flip_timer = window.after(3000, func=switch)
    # print(data_dict)
    # df = pd.DataFrame(data_dict)
    # df.to_csv('unknown_words1.csv')

    # df = pd.DataFrame({
    #     "Words": [current_word]
    # })

    # df.to_csv('/Users/kevinwong/Python Projects/Small Python Games + Programs/Flash Card Capstone Project - Day 31/csv files/known_words.csv', mode = 'a', index=False,header=False)


def switch():
    canvas.itemconfig(canvas_image, image=back_img)
    if len(current_card["English Definition"]) > 15:
        canvas.itemconfig(
            card_word,
            text=current_card["English Definition"],
            fill="white",
            font=("Arial", 35, "bold"),
        )
    canvas.itemconfig(card_word, text=current_card["English Definition"], fill="white")
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(
        card_pinyin, text=current_card["Chinese Pronunciation"], fill="white"
    )


# --------------------------------------------------
# Implementation of Buttons + Boxes

window = Tk()
window.title("Flashcard Project")
window.config(padx=50, pady=50, bg=HONEYDEW)
flip_timer = window.after(3000, switch)

# flashcard = Label(fg = HONEYDEW)
front_img = PhotoImage(
    file=r"/Users/kevinwong/Python Projects/Small Python Games + Programs/Flash Card Capstone Project - Day 31/images.png/card_front.png"
)
back_img = PhotoImage(
    file=r"/Users/kevinwong/Python Projects/Small Python Games + Programs/Flash Card Capstone Project - Day 31/images.png/card_back.png"
)
canvas = Canvas(width=800, height=526, bg=HONEYDEW, highlightbackground=HONEYDEW)
canvas_image = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(
    400, 150, fill="black", text="", font=("Ariel", 40, "italic")
)
card_word = canvas.create_text(
    400, 263, fill="black", text="", font=("Ariel", 60, "bold")
)
card_pinyin = canvas.create_text(
    400, 350, fill="black", text="", font=("Ariel", 40, "bold")
)
canvas.grid(row=0, column=0, columnspan=2)

# language = Label(text = "Chinese", font = ("Arial", 40, 'italic'))

check_mark = PhotoImage(
    file="/Users/kevinwong/Python Projects/Small Python Games + Programs/Flash Card Capstone Project - Day 31/images.png/right_one.png"
)
check_button = Button(
    image=check_mark,
    bd=0,
    highlightthickness=0,
    highlightbackground=HONEYDEW,
    command=change_words_right,
)
check_button.grid(row=1, column=1)

x_mark = PhotoImage(
    file="/Users/kevinwong/Python Projects/Small Python Games + Programs/Flash Card Capstone Project - Day 31/images.png/wrong_one.png"
)
x_button = Button(
    image=x_mark,
    highlightthickness=0,
    bd=0,
    highlightbackground=HONEYDEW,
    command=change_words_wrong,
)
x_button.grid(row=1, column=0)

change_words_wrong()

window.mainloop()

from tkinter import *
from PIL import ImageTk, Image
from random import *
from tkinter import messagebox


screen = Tk()
screen.title('screen')
screen.geometry('465x355')

def run():
    global black1_label, black3_label, black2_label, cat_label, door1_label, door2_label, door3_label
    global btn1, btn2, btn3, my_label, btn_change, btn_still, lbl
    global cat, cats, black, black1, door1, door, cat_place
    title = Label(screen, text='Find the cat', font='Times 20').grid(row=0, column=0)
    cat_place = randint(1, 3)

    def change(yn, notplace, escolha):
        global my_label, btn_change, btn_still, cat_place
        global door1_label, door3_label, door2_label
        final = 0
        if yn == True:
            if escolha == 1:
                if notplace == 2:
                    final = 3
                elif notplace == 3:
                    final = 2
            elif escolha == 2:
                if notplace == 1:
                    final = 3
                elif notplace == 3:
                    final = 1
            elif escolha == 3:
                if notplace == 1:
                    final = 2
                elif notplace == 2:
                    final = 1
        else:
            final = escolha
        my_label.grid_forget()
        btn_still.grid_forget()
        btn_change.grid_forget()
        if final == cat_place:
            word = 'won'
        else:
            word = 'lost'
        lbl = Label(screen, text=f"You've {word}.", font='Times 13')
        lbl.grid(row=3, column=1)
        door1_label.grid_forget()
        door2_label.grid_forget()
        door3_label.grid_forget()
        print(final)

    def choose(value):
        global cat_place, my_label, btn1, btn2, btn3, btn_still
        global door1_label, door3_label, door2_label, btn_change
        answ = 0
        print(value)
        print(cat_place)
        if value == 1:
            if cat_place == 1:
                a = [2, 3]
                answ = choice(a)
            elif cat_place == 2:
                answ = 3
            elif cat_place == 3:
                answ = 2
        elif value == 2:
            if cat_place == 1:
                answ = 3
            elif cat_place == 2:
                a = [1, 3]
                answ = choice(a)
            elif cat_place == 3:
                answ = 1
        elif value == 3:
            if cat_place == 1:
                answ = 2
            elif cat_place == 2:
                answ = 1
            elif cat_place == 3:
                a = [1, 2]
                answ = choice(a)
        if answ == 1:
            door1_label.grid_forget()
        elif answ == 2:
            door2_label.grid_forget()
        elif answ == 3:
            door3_label.grid_forget()
        my_label = Label(screen, text=f"The cat isn't in the door{answ}.\nYou can change.", font='Times 11')
        my_label.grid(row=3, column=1)
        btn1.grid_forget()
        btn2.grid_forget()
        btn3.grid_forget()
        btn_change = Button(screen, text='Change', bg='red', command=lambda: change(True, answ, value))
        btn_still = Button(screen, text='  Still  ', bg='blue', command=lambda: change(False, answ, value))
        btn_still.grid(row=4, column=0)
        btn_change.grid(row=4, column=2)
        print(answ)

    cat = Image.open('./tapi1.png')
    door = Image.open('./door.jpg')
    black = Image.open('./black.jpg')
    width, height = door.size
    black = black.resize((round(width), round(height)), Image.ANTIALIAS)
    black1 = ImageTk.PhotoImage(black)
    cats = ImageTk.PhotoImage(cat)
    door1 = ImageTk.PhotoImage(door)
    black1_label = Label(screen, image=black1)
    black2_label = Label(screen, image=black1)
    black3_label = Label(screen, image=black1)
    cat_label = Label(screen, image=cats, bg='black')
    door1_label = Label(screen, image=door1)
    door2_label = Label(screen, image=door1)
    door3_label = Label(screen, image=door1)
    black1_label.grid(row=1, column=0)
    black2_label.grid(row=1, column=1)
    black3_label.grid(row=1, column=2)
    cat_label.grid(row=1, column=cat_place - 1)
    door1_label.grid(row=1, column=0)
    door2_label.grid(row=1, column=1)
    door3_label.grid(row=1, column=2)
    s1 = Label(screen, text='                        ').grid(row=2, column=0)
    s2 = Label(screen, text='                        ').grid(row=2, column=1)
    s3 = Label(screen, text='                        ').grid(row=2, column=2)
    s4 = Label(screen, text='                        ').grid(row=3, column=1)
    s5 = Label(screen, text='                        ').grid(row=4, column=0)
    s6 = Label(screen, text='                           ').grid(row=4, column=2)
    s7 = Label(screen, text='                         ').grid(row=5, column=1)
    btn1 = Button(screen, text='Choose door 1', padx=30, bg='red', command=lambda: choose(1))
    btn1.grid(row=2, column=0)
    btn2 = Button(screen, text='Choose door 2', padx=30, bg='green', command=lambda: choose(2))
    btn2.grid(row=2, column=1)
    btn3 = Button(screen, text='Choose door 3', padx=30, bg='blue', command=lambda: choose(3))
    btn3.grid(row=2, column=2)

run()

def again():
    global black1_label, black3_label, black2_label, cat_label, door1_label, door2_label, door3_label
    global btn1, btn2, btn3, my_label, btn_change, btn_still, lbl
    global cat, cats, black, black1, door1, door
    black1_label.grid_forget()
    black2_label.grid_forget()
    black3_label.grid_forget()
    cat_label.grid_forget()
    door1_label.grid_forget()
    door2_label.grid_forget()
    door3_label.grid_forget()
    btn1.grid_forget()
    btn2.grid_forget()
    btn3.grid_forget()

    try:
        my_label.grid_forget()
    except:
        print('')
    try:
        lbl.grid_forget()
    except:
        print('')
    try:
        btn_still.grid_forget()
    except:
        print('')
    try:
        btn_change.grid_forget()
    except:
        print('')
    run()

btn_again = Button(screen, text='Try again', command=again)
btn_again.grid(row=6, column=0)

def exit():
    global screen
    popup = messagebox.askyesno('EXIT', 'Are you sure you want to nd the programm?')
    if popup == True:
        screen.quit()

btn_exit = Button(screen, text='   Exit   ',bg='purple', command= exit)
btn_exit.grid(row=6, column=2)

screen.mainloop()

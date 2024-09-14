from  tkinter import  *
import tkinter
from tkinter import messagebox  # For showing error popup
root=tkinter.Tk()
root.geometry("500x500")
root.title("Tic Tac Toe")

turn = "X"
win={   1:"",2:"",3:"",
        4:"",5:"",6:"",
        7:"",8:"",9:"",
    }


def checkforwin(player):



    # Row

    if win[1]==win[2] and win[2]==win[3] and win[3]==player:
        return True

    elif win[4]==win[5] and win[5]==win[6] and win[6]==player:
        return True

    elif win[7]==win[8] and win[8]==win[9] and win[9]==player:
        return True
    #  Column

    elif win[1]==win[4] and win[4]==win[7] and win[7]==player:
        return True

    elif win[2]==win[5] and win[5]==win[8] and win[8]==player:
        return True

    elif win[3]==win[6] and win[6]==win[9] and win[9]==player:
        return True

    # X side

    elif win[1]==win[5] and win[6]==win[9] and win[9]==player:
        return True

    elif win[3]==win[5] and win[5]==win[7] and win[7]==player:
        return True




def back_home():
    home()


def checkfordraw():
    for i in win.keys():
        if win[i] == "":
            return False
    return True


def game_start():

    f2=Frame(bg="orange")
    f2.place(x=0, width=500, height=500)

    #  Back Button
    back=Button(f2,text="<<<",bg="yellow",font=("comic sana ms",20),command=back_home)
    back.place(x=1,y=1)





    # Button frame
    button_frame= Frame(bg="yellow")
    button_frame.place(x=50,y=170)

    # Row One


    def run(event):
        global turn
        button=event.widget

        # Data stor ---------------------------------------
        button_text=str(button)
        clicked=button_text[-1]
        if clicked=="n":
            clicked=1
        else:
            clicked=int(clicked)
        print(clicked)



        # -------------------------------------
        if button["text"] == "":

            if turn=="X":
                button["text"]="X"
                win[clicked]=turn  # Data stor ------------
                if checkforwin(turn):
                    messagebox.showinfo("Winnnnnnnnn", "'X' You win")

                turn="O"
                if checkfordraw():
                    messagebox.showinfo("Opppps", "Match Draw")


            else:
                button["text"]="O"
                win[clicked] = turn  # Data stor ------------
                if checkforwin(turn):
                    messagebox.showinfo("Winnnnnnnnn", "'O' You win")
                turn="X"
            if checkfordraw():
                messagebox.showinfo("Opppps","Match Draw")

        print(win)


    b1=Button(button_frame,text="",bg="yellow",font=("comic sana ms",30),width=5,relief=RAISED,borderwidth=5)
    b1.grid(row=0,column=0)
    b1.bind("<Button-1>",run)
    b2=Button(button_frame,text="",bg="yellow",font=("comic sana ms",30),width=5,relief=RAISED,borderwidth=5)
    b2.grid(row=0, column=1)
    b2.bind("<Button-1>",run)
    b3=Button(button_frame,text="",bg="yellow",font=("comic sana ms",30),width=5,relief=RAISED,borderwidth=5)
    b3.grid(row=0, column=2)
    b3.bind("<Button-1>",run)


    # Row Two

    b4=Button(button_frame,text="",bg="yellow",font=("comic sana ms",30),width=5,relief=RAISED,borderwidth=5)
    b4.grid(row=1, column=0)
    b4.bind("<Button-1>",run)
    b5=Button(button_frame,text="",bg="yellow",font=("comic sana ms",30),width=5,relief=RAISED,borderwidth=5)
    b5.grid(row=1, column=1)
    b5.bind("<Button-1>",run)
    b6=Button(button_frame,text="",bg="yellow",font=("comic sana ms",30),width=5,relief=RAISED,borderwidth=5)
    b6.grid(row=1, column=2)
    b6.bind("<Button-1>",run)

    # Row Three

    b7=Button(button_frame,text="",bg="yellow",font=("comic sana ms",30),width=5,relief=RAISED,borderwidth=5)
    b7.grid(row=3, column=0)
    b7.bind("<Button-1>",run)
    b8=Button(button_frame,text="",bg="yellow",font=("comic sana ms",30),width=5,relief=RAISED,borderwidth=5)
    b8.grid(row=3, column=1)
    b8.bind("<Button-1>",run)
    b9=Button(button_frame,text="",bg="yellow",font=("comic sana ms",30),width=5,relief=RAISED,borderwidth=5)
    b9.grid(row=3, column=2)
    b9.bind("<Button-1>",run)

    tic_lab=Label(f2,text="Tic Tac Toe ッ",bg="yellow",font=("Comic sana ms",25))
    tic_lab.place(x=150,y=100)
    def for_refresh():
        for i in buttons:
            i["text"]=""
        for y in win.keys():
            win[y]=""
        game_start()


    b = Button(f2, text="Refresh", bg="yellow", font=("Comic Sans MS", 15), relief=RAISED,cursor="hand2", borderwidth=5,command=for_refresh)
    b.place(x=340, y=430)

    buttons=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
def home():
    f1 = Frame(bg="yellow")
    f1.place(x=0, width=500, height=500)

    b=Button(f1,text="Start Game",bg="orange",font=("Comic Sans MS",30),cursor="hand2",relief=RAISED,borderwidth=5,command=game_start)
    b.place(x=120,y=150)


home()
root.mainloop()
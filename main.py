import random
from tkinter import *
from  tkinter import messagebox
card_number_user = [11,2,3,4,5,6,7,8,9,10,10,10,10]
card_number_comp = [11,2,3,4,5,6,7,8,9,10,10,10,10]

user_card = []
computer_card =[]
drow = 0
def check():
    if (11 in user_card or 11 in computer_card) and ( sum(user_card) >21 or sum(computer_card)>21):
        if sum(user_card)>21 and 11 in user_card:
            user_card[user_card.index(11)]=1
        elif sum(computer_card) > 21 and 11 in computer_card:
            computer_card[computer_card.index(11)]=1
    else:
        pass

def comp_card_place(x):
    global xyc, g
    if drow ==0:
        if x == 1 or x == 11:
            pp = random.choice(all_card)
            g = canver.create_image(xyc, 90, image=pp[0])
            xyc += 40
        elif x == 10:
            a10 = [9, 10, 11, 12]
            pp = random.choice(all_card)
            g = canver.create_image(xyc, 90, image=pp[random.choice(a10)])
            xyc += 40
        else:
            pp = random.choice(all_card)
            g = canver.create_image(xyc, 90, image=pp[card_number_user.index(x)])
            xyc += 40
    else:
        g = canver.create_image(xyc, 90, image=blank)
        xyc += 40
def reveil():
    xyc = 254
    for x in range(1,len(computer_card)):
        if computer_card[x] == 1 or x == 11:
            pp = random.choice(all_card)
            g = canver.create_image(xyc, 90, image=pp[0])
            xyc += 40
        elif computer_card[x] == 10:
            a10 = [9, 10, 11, 12]
            pp = random.choice(all_card)
            g = canver.create_image(xyc, 90, image=pp[random.choice(a10)])
            xyc += 40
        else:
            pp = random.choice(all_card)
            g = canver.create_image(xyc, 90, image=pp[card_number_user.index(computer_card[x])])
            xyc += 40
def start_deal():
    """this is the start deal function which will assign 2 cards for the user and the computer"""
    global drow
    for i in range(2):
        div = random.choice(card_number_user)
        user_card.append(div)
        card_place(div)
        check()
    for i in range(2):

        div = random.choice(card_number_comp)
        computer_card.append(div)
        check()
        comp_card_place(div)
        drow = 1

def card_place(x):
    global xy,g
    if x == 1 or x == 11:
        pp = random.choice(all_card)
        g =canver.create_image(xy, 200, image=pp[0])
        xy += 40
    elif x == 10:
        a10 =[9,10,11,12]
        pp = random.choice(all_card)
        g =canver.create_image(xy, 200, image=pp[random.choice(a10)])
        xy += 40
    else:
        pp = random.choice(all_card)
        g = canver.create_image(xy, 200, image=pp[card_number_user.index(x)])
        xy +=40

def deal():
    """the request for an additional card"""
    if drow <= 0:
        start_deal()

    elif drow >= 1:
        if( sum(user_card) < 21 and sum(user_card) != 21):
            div = random.choice(card_number_user)
            user_card.append(div)
            card_place(div)
        else:
            messagebox.showinfo("Card", "Your card sum is greater the '21'")
        comp_dl = [0, 1]
        if (random.choice(comp_dl) == 0 and sum(computer_card) < 21) and sum(computer_card) != 21:
            div = random.choice(card_number_comp)
            computer_card.append(div)
            comp_card_place(div)

        else:
            pass
        check()

def result_of_game():

   def end():
       global tx_user, tx_computer, drow, xy, user_money, computer_money, play_deal, bet, xyc

       user = sum(user_card)
       comp = sum(computer_card)
       if user > comp and user <= 21:
           # user win
           user_money += play_deal
           messagebox.showinfo("Result","YOU WIN")
       elif comp > user and comp <= 21:
           # compuer win
           computer_money += play_deal
           messagebox.showinfo("Result","COMPUTER WIN")
       elif user > 21 and comp <= 21:
           computer_money += play_deal
           messagebox.showinfo("Result","COMPUTER WIN")
       elif comp > 21 and user <= 21:
           messagebox.showinfo("Result","YOU WIN")
           user_money += play_deal
       elif user > 21 and comp > 21:
           messagebox.showinfo("Result","YOU BOTH LOSE")
       elif user == comp and user <= 21:
           # you draw
           computer_money += play_deal / 2
           user_money += play_deal / 2
           messagebox.showinfo("Result","YOU AND COMPUTER DRAM")
       if user_money == 0:
           messagebox.showinfo("Result","GAME OVER")
       elif computer_money <= 0:
           messagebox.showinfo("Result","YOU ARE THE WINNER")
       elif user_money <= 0 and computer_money <= 0:
           messagebox.showinfo("Result","GAME OVER")
       else:
           pass

       user_card.clear()
       computer_card.clear()
       canver.delete("all")
       drow = 0
       xy = 215
       xyc = 215
       canver.create_image(254, 143, image=game_play_bd)
       tx_user = canver.create_text(55, 34, text=f"UXP:{user_money}", font=("Arial Rounded MT Bold", 12), fill="white")
       tx_computer = canver.create_text(450, 34, text=f"CXP:{computer_money}", font=("Arial Rounded MT Bold", 12),
           fill="white")
       play_deal = 0
       bet = canver.create_text(70, 74, text=f"Reword:{play_deal}", font=("Arial Rounded MT Bold", 12), fill="white")
   reveil()
   canver.after(3000, end)

##############################################################################
# TODO 1: GUI
def xp5000():
    global user_money,play_deal, computer_money
    user_money = user_money-5000
    computer_money= computer_money-5000
    play_deal += 10000
    canver.itemconfigure(tx_user, text=f"UXP:{user_money}")
    canver.itemconfigure(tx_computer, text=f"CXP:{computer_money}")
    canver.itemconfigure(bet, text=f"Reword:{play_deal}")

def xp1000():
    global user_money, play_deal, computer_money
    user_money = user_money - 1000
    computer_money = computer_money - 1000
    play_deal += 2000
    canver.itemconfigure(tx_user, text=f"UXP:{user_money}")
    canver.itemconfigure(tx_computer, text=f"CXP:{computer_money}")
    canver.itemconfigure(bet, text=f"Reword:{play_deal}")


def xp500():
    global user_money, play_deal, computer_money
    user_money = user_money - 500
    computer_money = computer_money - 500
    play_deal += 1000
    canver.itemconfigure(tx_user, text=f"UXP:{user_money}")
    canver.itemconfigure(tx_computer, text=f"CXP:{computer_money}")
    canver.itemconfigure(bet, text=f"Reword:{play_deal}")

def xp100():
    global user_money, play_deal, computer_money
    user_money = user_money - 100
    computer_money = computer_money - 100
    play_deal += 200
    canver.itemconfigure(tx_user, text=f"UXP:{user_money}")
    canver.itemconfigure(tx_computer, text=f"CXP:{computer_money}")
    canver.itemconfigure(bet, text=f"Reword:{play_deal}")

def animation(text):

    def all():
        global tx_user, tx_computer,bet
        def ghy(e):
            unveil["image"] = unv_off
        def hjy(e):
            unveil["image"] = unv_no

        canver.delete("all")
        canver.create_image(254, 143, image=game_play_bd)
        tx_user = canver.create_text(55, 34, text=f"UXP:{user_money}", font=("Arial Rounded MT Bold",12), fill="white")
        tx_computer = canver.create_text(450, 34, text=f"CXP:{computer_money}", font=("Arial Rounded MT Bold",12), fill="white")
        bet = canver.create_text(70, 74, text=f"Reword:{play_deal}", font=("Arial Rounded MT Bold", 12),
            fill="white")
        ac = Button(image=deal_card, border=0, bg="#ae272d", command=deal)
        ac.place(x=340, y=120)
        x5000 = Button(image=c5000, border=0, bg="#ae272d",command=xp5000)
        x5000.place(x=300, y=115)
        x1000 = Button(image=c1000, border=0, bg="#ae272d",command=xp1000)
        x1000.place(x=250, y=123)
        x500 = Button(image=c500, border=0, bg="#9d2228",command=xp500)
        x500.place(x=200, y=123)
        x100 = Button(image=c100, border=0, bg="#931e25",command=xp100)
        x100.place(x=150, y=123)
        unveil = Button(image=unv_no, border=0, bg="#372913", command=result_of_game)
        unveil.place(x=430,y=200)
        unveil.bind("<Enter>", ghy)
        unveil.bind("<Leave>", hjy)
    coler = ["red", "white", "yellow", "brown","green","orange"]
    t=canver.create_text(243,130, text="",  fill="red", justify=CENTER, font=("Algerian", 20,"bold"))
    delay = 0
    abt = 100
    for x in range(len(text)+1):
        s = text[:x]
        new_text = lambda s=s: canver.itemconfigure(t, text=s, fill=random.choice(coler))
        canver.after(delay, new_text)
        delay += abt
    canver.after(delay+3000, all)

def play_game():
    canver.delete("all")
    play_B.destroy()

    map_l = canver.create_image(254,145, image=mp)
    text = 'Welcome to BlackJack\n Game'
    animation(text)









def pl(e):
    play_B["image"] = play_h
def pl_b(e):
    play_B["image"] = play
home = Tk()
home.title("Black Jack Game")
xy = 215
xyc= 215
play_deal = 0
user_money = 10000
computer_money = 10000
h1 = PhotoImage(file="image/1h.png")
h2 = PhotoImage(file="image/2h.png")
h3 = PhotoImage(file="image/3h.png")
h4 = PhotoImage(file="image/4h.png")
h5 = PhotoImage(file="image/5h.png")
h6 = PhotoImage(file="image/6h.png")
h7 = PhotoImage(file="image/7h.png")
h8 = PhotoImage(file="image/8h.png")
h9 = PhotoImage(file="image/9h.png")
h10 = PhotoImage(file="image/10h.png")
hj = PhotoImage(file="image/jh.png")
hq = PhotoImage(file="image/qh.png")
hk = PhotoImage(file="image/kh.png")
h_list = [h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,hj,hq,hk]
d1 = PhotoImage(file="image/1d.png")
d2 = PhotoImage(file="image/2d.png")
d3 = PhotoImage(file="image/3d.png")
d4 = PhotoImage(file="image/4d.png")
d5 = PhotoImage(file="image/5d.png")
d6 = PhotoImage(file="image/6d.png")
d7 = PhotoImage(file="image/7d.png")
d8 = PhotoImage(file="image/8d.png")
d9 = PhotoImage(file="image/9d.png")
d10 = PhotoImage(file="image/10d.png")
dj = PhotoImage(file="image/jd.png")
dq = PhotoImage(file="image/qd.png")
dk = PhotoImage(file="image/kd.png")
d_list = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,dj,dq,dk]

bh1 = PhotoImage(file="image/1bh.png")
bh2 = PhotoImage(file="image/2bh.png")
bh3 = PhotoImage(file="image/3bh.png")
bh4 = PhotoImage(file="image/4bh.png")
bh5 = PhotoImage(file="image/5bh.png")
bh6 = PhotoImage(file="image/6bh.png")
bh7 = PhotoImage(file="image/7bh.png")
bh8 = PhotoImage(file="image/8bh.png")
bh9 = PhotoImage(file="image/9bh.png")
bh10 = PhotoImage(file="image/10bh.png")
bhj = PhotoImage(file="image/jbh.png")
bhq = PhotoImage(file="image/qbh.png")
bhk = PhotoImage(file="image/kbh.png")
bh_list = [bh1,bh2,bh3,bh4,bh5,bh6,bh7,bh8,bh9,bh10,bhj,bhq,bhk]

l1 = PhotoImage(file="image/1l.png")
l2 = PhotoImage(file="image/2l.png")
l3 = PhotoImage(file="image/3l.png")
l4 = PhotoImage(file="image/4l.png")
l5 = PhotoImage(file="image/5l.png")
l6 = PhotoImage(file="image/6l.png")
l7 = PhotoImage(file="image/7l.png")
l8 = PhotoImage(file="image/8l.png")
l9 = PhotoImage(file="image/9l.png")
l10 = PhotoImage(file="image/10l.png")
lj = PhotoImage(file="image/jl.png")
lq = PhotoImage(file="image/ql.png")
lk = PhotoImage(file="image/kl.png")
l_list = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,lj,lq,lk]
blank = PhotoImage(file="image/blank_card.png")
all_card = [l_list,bh_list,d_list,h_list]
home.geometry("503x287")

mp = PhotoImage(file="image/pro_start.png")
stat_up = PhotoImage(file="image/setup.png")
play = PhotoImage(file="image/play.png")
play_h = PhotoImage(file="image/play_d.png")
game_play_bd = PhotoImage(file="image/game_1.png")
deal_card = PhotoImage(file="image/add_card.png")
c1000 = PhotoImage(file="image/1000.png")
c5000 = PhotoImage(file="image/5000.png")
c500 = PhotoImage(file="image/500.png")
c100 = PhotoImage(file="image/100.png")
unv_no = PhotoImage(file="image/unveil_no.png")
unv_off = PhotoImage(file="image/unveil_off.png")
canver = Canvas(width=503, height=289)
canver.create_image(252.5,141.5, image=stat_up)
play_B = Button(canver, bg="black", image=play, border=0, command=play_game)
play_B.place(x=57,y=180)
play_B.bind("<Enter>", pl)
play_B.bind("<Leave>", pl_b)
canver.place(x=-2,y=0)
home.mainloop()
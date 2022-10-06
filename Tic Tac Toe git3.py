#The TicTacToe game by Gnanesh : ) done on 06/10/2022 at 11:34
def checkwin(brd,sym1,sym2,chance):  #checking win or draw
    if win(brd, sym1):
        print(f"{chance[:-2]} {int(chance[-1])-1} ({sym1}) won the game")
        return True
    if win(brd, sym2):
        print(f"{chance[:-2]} {int(chance[-1])+1} ({sym2}) won the game")
        return True
    if check_space(brd):
        print("Draw!!!")
        return True
def check_space(brd):      #checking all filled or not
    for i in range(1, 10):
        if brd[i] == ' ':
            return False
    return True
def check(brd,p1):          #checking empty or not
    Flag=False
    if brd[p1]==" ":
        Flag=True
    return Flag
def win(l,symbol):          #source to check win
    if (    (l[1]== symbol and l[2]== symbol and l[3] == symbol) or
            (l[4]== symbol and l[5]== symbol and l[6] == symbol) or
            (l[7]== symbol and l[8]== symbol and l[9] == symbol) or
            (l[1]== symbol and l[4]== symbol and l[7] == symbol) or
            (l[2]== symbol and l[5]== symbol and l[8] == symbol) or
            (l[3]== symbol and l[6]== symbol and l[9] == symbol) or
            (l[1]== symbol and l[5]== symbol and l[9] == symbol) or
            (l[7]== symbol and l[5]== symbol and l[3] == symbol)):
        return True
    return False
def pb(brd):                                               #the board to represent
    print(f" {brd[1]} | {brd[2]} | {brd[3]} ")
    print("-----------")
    print(f" {brd[4]} | {brd[5]} | {brd[6]} ")
    print("-----------")
    print(f" {brd[7]} | {brd[8]} | {brd[9]} ")
l=['1','2','3','4','5','6','7','8','9']                   #list of nums to check user i/p in numaric or not
def tictactoe():
    print("Welcome to the game : )")
    brd = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    pb(brd)                                                     #print board
    sym1 = input("enter symbol(X or O) for player 1: ").upper()
    sym2="X"
    if sym1=="X":
        sym2="O"
    else:
        sym1="O"                             #even though user i/p is wrong in symbol just taing X or O
    chance="Player_1"
    while True:
        if checkwin(brd,sym1,sym2,chance):
            break
        #user one i/p process
        if chance=="Player_1":
            p1=input("player 1 enter position: ")
            while p1 not in l:
                p1 = input("player 1 enter position in Numerical only : ")  #asking user to i/p only numaric only
            p1=int(p1)
            if check(brd,p1) :
                brd[p1]=sym1                     #if it's empty replacing with symbol
                pb(brd)
                chance="Player_2"
            else:
                print("place is filled")
                chance="Player_1"
        if checkwin(brd,sym1,sym2,chance):
            break
        #user two i/p process
        if chance=="Player_2":
            p2=input("player 2 enter position: ")
            while p2 not in l:
                p2 = input("player 2 enter position in Numerical only : ")#asking user to i/p only numaric only
            p2 = int(p2)
            if check(brd,p2):
                brd[p2]=sym2
                pb(brd)
                chance="Player_1"
            else:
                print("place is filled")
                chance="Player_2"
    ans = input("want to play again (y/n): ").upper()   #asking user to play again
    if ans == "Y":
        tictactoe()                    #if user wants to play again calling func by recurssion
tictactoe()                            #the key of game !!! : )
#this is my 3nd project in python by using modules 
#the above all code done by my own until what I learned



def clearlist():
    list=['','','','','','','','','']
    return list

list=clearlist()


def startscreen():
    print('Welcome to Tik Tak Toe!')
    p1choice= 'wrong'
    while p1choice not in ['X','O']:
        p1choice=input('Player 1: Your charecter is X. Press X to start, O to exit (X or O): ')
        if p1choice not in ['X']:
            print('Please input a correct choice!')
        elif p1choice=='O':
            exit(1)

    
    return p1choice
    
    
#add function 

    
def startgame(p1choice):
    if p1choice=='X':
        print(f'The player 1 has selected {p1choice} so player 1 starts first.')
    else:
        print(f'The player 1 has selected {p1choice} so player 2 starts first.')
    print()

def display():
    print(f' {list[0]} || {list [1]} || {list[2]}')
    print('------------')
    print(f' {list[3]} || {list [4]} || {list[5]}')
    print('------------')
    print(f' {list[6]} || {list [7]} || {list[8]}')


def gameloop1(p1choice):
    print('Player 1: Enter the index of placing your charecter.')
    replace=int(input("Enter position:"))
    if list[replace] in ['X','O']:
        print('This position is already occupied please enter a different position.')
        gameloop1(p1choice)
    else:
        list[replace]=p1choice

def gameloop2(p1choice):
    print('Player 2: Enter the index of placing your charecter.')
    replace=int(input("Enter position:"))
    if p1choice =='O':
        if list[replace] in ['X','O']:
            print('This position is already occupied please enter a different position.')
            gameloop2(p1choice)
        else:
            list[replace]='X'

        
        
    elif p1choice=='X':
        if list[replace] in ['X','O']:
            print('This position is already occupied please enter a different position.')
            gameloop2(p1choice)
        else:
            list[replace]='O'

    else:
        pass

def statcheck():
    win=False
    playerwin='none'
    #p2win
    if list[0]== 'O' and list[1]=='O' and list[2]=='O':
        win=True
        playerwin='p2'
    elif list[3]== 'O' and list[4]=='O' and list[5]=='O':
        win=True
        playerwin='p2'
    elif list[6]== 'O' and list[7]=='O' and list[8]=='O':
        win=True
        playerwin='p2'
    if list[0]== 'O' and list[3]=='O' and list[6]=='O':
        win=True
        playerwin='p2'
    elif list[1]== 'O' and list[4]=='O' and list[7]=='O':
        win=True
        playerwin='p2'
    elif list[2]== 'O' and list[5]=='O' and list[8]=='O':
        win=True
        playerwin='p2'
    elif list[0]== 'O' and list[4]=='O' and list[8]=='O':
        win=True
        playerwin='p2'
    elif list[2]== 'O' and list[4]=='O' and list[6]=='O':
        win=True
        playerwin='p2'
        

    #p1win
    elif list[0]== 'X' and list[1]=='X' and list[2]=='X':
        win=True
        playerwin='p1'
    elif list[3]== 'X' and list[4]=='X' and list[5]=='X':
        win=True
        playerwin='p1'
    elif list[6]== 'X' and list[7]=='X' and list[8]=='X':
        win=True
        playerwin='p1'
    elif list[0]== 'X' and list[3]=='X' and list[6]=='X':
        win=True
        playerwin='p1'
    elif list[1]== 'X' and list[4]=='X' and list[7]=='X':
        win=True
        playerwin='p1'
    elif list[2]== 'X' and list[5]=='X' and list[8]=='X':
        win=True
        playerwin='p1'
    elif list[0]== 'X' and list[4]=='X' and list[8]=='X':
        win=True
        playerwin='p1'
    elif list[2]== 'X' and list[4]=='X' and list[6]=='X':
        win=True
        playerwin='p1'

    #tie
    elif list[0] in ['X', 'O'] and list[1] in ['X', 'O'] and list[2] in ['X', 'O']  and list[3] in ['X', 'O'] and list[4] in ['X', 'O'] and list[5] in ['X', 'O'] and list[6] in ['X', 'O'] and list[7] in ['X', 'O'] and list[8] in ['X', 'O'] and win==False:
        print("Game is a tie")
    
    else:
        pass

    list1=["",""]
    list1[0]=win
    list1[1]=playerwin

    return list1

def continueplay():
    conti='Wrong'
    while conti not in ['Y', 'N']:
        conti=input(('Do you want to continue playing? (Y or N)'))
    if conti=='Y':
        gameloop()
    else:
        exiting()

def exiting():
    exit(1)


def gameloop():
    win=False
    playerwin='none'

    p1choice= startscreen()
    startgame(p1choice)
    display()
    while win==False:
        gameloop1(p1choice)
        display()
        chk=statcheck()
        win=chk[0]
        playerwin=chk[1]
        if win==True:
            break
        else:
            pass
        print(win)
        gameloop2(p1choice)
        display()
        chk=statcheck()
        win=chk[0]
        playerwin=chk[1]
        print(win)
    if playerwin=='p1':
        print('Player 1 is the winner.')
    if playerwin=='p2':
        print('Player 2 is the winner.')
    
    
    



gameloop()
list=clearlist()
continueplay()

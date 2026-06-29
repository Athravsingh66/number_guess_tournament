import random

modes=["Easy","Medium","Hard"]

def rules():
    print("\n============ TOURNAMENT RULES ==============")
    print("Easy   : Number between 1-10,  Max Attempts = 3")
    print("Medium : Number between 1-50,  Max Attempts = 5")
    print("Hard   : Number between 1-100, Max Attempts = 7")
    print("Guess history is shown at the end of each round.\n")

    

def play_game():
    print("Select the Level of Games from the given level as below  ")
    print('''1. Easy
2. Medium
3. Hard
''')
    try:
        choice = int(input("Select your Level: "))
        print("")
    except ValueError:
        print("Invalid input!")
        return
    if choice==1:
        level=modes[0]
        num=10
        attempt=3
    elif choice==2:
        level=modes[1]
        num=50
        attempt=5
    elif choice==3:
        level=modes[2]
        num=100
        attempt=7
    else:
        print("Invalid Entry")
        return
        
    guess_history_player=[]  
    print(f"{level} Level Selected") 
    print(f"Gueses the number in between 1 to {num}\n")  
    computer=random.randint(1,num)
    for i in range(1,attempt+1):
        print(f"Round:{i}")
        try:
            player = int(input("Enter your number: "))
        except ValueError:
            print("Invalid input!")
            continue                                                                               
        if player<1 or player>num:
            guess_history_player.append(player)
            print("You Guessed the number Out of Range")
            continue
        if player==computer:
            guess_history_player.append(player)
            print("---You Guessed the Right Number---")
            break
        
        elif player>computer:
            print("Your Guessed Too High ")
        elif player<computer:
            print("You Guessed Too Low ")
        else:
            print("Inavlid Entry \n")
        guess_history_player.append(player)
    else:
        print("\n!!!!!!!!!!! You Lost the Game !!!!!!!!!!!!!!!! ")
        print(f"The Correct Number was {computer}.")
            
    print("")
    print("---------------------Finally--------------------")         
    print(f"Your all Previous Guess History:{guess_history_player}")
    print("================TOURNAMENT IS OVER NOW AGAIN PLAY NEW TOUENAMENT======================\n")
    
    
    
while True:
    print("-------------Number Guess Tournament----------------")
    print("==============Tournament Menu======================")
    print('''1. Play New Tournament Round
2. View Tournament Rules
3. Exit Game''')
    try:
        menu_choice = int(input("Enter Your Menu Choice: "))
    except ValueError:
        print("Invalid input!")
        continue 
    print("")
    if menu_choice==1:
        play_game()
    elif menu_choice==2:
        rules() 
    elif menu_choice==3:
        print("Thanks for Playing Game\n")
        break  
    else:
        print("Inavlid Entry Something Went Wrong!!!!!!!!")
        
    
        
        
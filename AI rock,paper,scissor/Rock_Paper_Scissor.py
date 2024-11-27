import random

print("Hello welcome to Rock, Paper, scissor with AI")
print("Please enter ur name: ")
user = input()
ai = "AI"
userlist = []
AIlist = []
probabilities = [0,0,0]

def get_ai_choice():
    if len(userlist) <= 3:
        items_list = ["rock", "paper", "scissor"]
        return random.choice(items_list)
    
    else:
        for choice in userlist:
            if choice == "rock":
                probabilities[0]+=1
            if choice == "paper":
                probabilities[1]+=1
            if choice == "scissor":
                probabilities[2]+=1
        
        moves = len(userlist)
        probabilities[0]/= moves 
        probabilities[1]/= moves 
        probabilities[2]/= moves

        best_choice = max(probabilities)

        if best_choice == probabilities[0]:
            return "paper"
        elif best_choice == probabilities[1]:
            return "scissor"
        elif best_choice == probabilities[2]:
            return "rock"
        

def check_winner(user_choice, ai_choice):
    winner = user
    if user_choice == ai_choice:
        return "Tie!"
    elif(user_choice == "rock" and ai_choice == "scissor") or (user_choice == "scissor" and ai_choice == "paper") or (user_choice == "paper" and ai_choice == "rock"):
        return (f"{winner} is the winner!")
    else:
        winner = ai
        return (f"{ai} is the winner!")

running = True
while(running):
    print("Do you want to play?")
    answer = input().lower()
    if answer == "yes" or answer == "y":
        #run the game here
        print("Play between rock, paper, scissor")
        user_choice = input()

        while user_choice not in ["rock", "paper", "scissor"]:
            print("Invalid choice. Please play between rock, paper, scissor")
            user_choice = input()

        userlist.append(user_choice)
        ai_choice = get_ai_choice()

        AIlist.append(ai_choice)
        result = check_winner(user_choice,ai_choice)

        print(f"You chose {user_choice}, AI chose {ai_choice}, {result}")
    
    elif answer== "no" or answer == "n" :
        running = False
    
    else:
        print("Please enter appropriate answer (yes or no)")

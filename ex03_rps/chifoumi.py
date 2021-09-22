import random

def generate_bot_pick():
    bot_pick = random.choice(['Rock', 'Paper', 'Cissors'])
    print("Bot pick : "+str(bot_pick))

    return bot_pick

def check_validity(user_pick, bot_pick):

    if user_pick == "Rock" and bot_pick == "Cissors" or user_pick == "Cissors" and bot_pick == "Paper" or user_pick == "Paper" and bot_pick == "Rock":
        print("You won !")
        winner = "user"

    elif bot_pick == "Rock" and user_pick == "Cissors" or bot_pick == "Cissors" and user_pick == "Paper" or bot_pick == "Paper" and user_pick == "Rock":
        print("You lost !")
        winner = "bot"

    else:
        winner = None

    return winner



def play():

    print("Here are the picks : \n -- Rock -- \n -- Paper -- \n -- Cissors --\n")

    user_pick = input("Choose your pick !\n")

    if(user_pick == "Rock" or user_pick == "Paper" or user_pick == "Cissors"):
        bot_pick = generate_bot_pick()
        winner = check_validity(user_pick, bot_pick)

        while winner == None:
            user_pick = input("Draw ! Try a another pick !\n")
            if(user_pick == "Rock" or user_pick == "Paper" or user_pick == "Cissors"):
                bot_pick = generate_bot_pick()
                winner = check_validity(user_pick, bot_pick)

    else:
        while user_pick != "Rock" or user_pick != "Paper" or user_pick != "Cissors":
            user_pick = input("Bad ! Try a another pick !\n")
            if(user_pick == "Rock" or user_pick == "Paper" or user_pick == "Cissors"):
                bot_pick = generate_bot_pick()
                winner = check_validity(user_pick, bot_pick)

if __name__ == "__main__":

    play()
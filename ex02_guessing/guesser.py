import random

def randomizer(min_range, max_range):

    rand = random.randint(min_range, max_range)
    print(rand)

    user_guess = input("What's your guess ?\n")
    user_guess = int(user_guess)

    if user_guess == rand:
        print("Bravo !")

    else:
        while user_guess != rand:
            
            user_guess = int(user_guess)

            if user_guess < rand:
                user_guess = input("More !\n")

            elif user_guess > rand:
                user_guess = input("Less !\n")

            elif user_guess == rand:
                print("Bravo !")
                break

if __name__ == "__main__":

    min = input("Type in the minimum range : ")
    max = input("Type in the maximum range : ")

    randomizer(int(min), int(max))
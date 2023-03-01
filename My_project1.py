import random
def rock_paper_scissors():
    user1 = input("enter rock,paper,scissors: ")
    user2 = input("enter rock,paper,scissors: ")
    if user1 == "paper" and user2 == "scissors":
        return "user1 lose"
    elif user1 == "paper" and user2 == "rock":
        return "user1 wins"
    elif user1 == "paper" and user2 == "paper":
        return "drawn"
    elif user1 == "scissors" and user2 == "scissors":
        return "drawn"
    elif user1 == "scissors" and user2 == "rock":
        return "user2 wins"
    elif user1 == "scissors" and user2 == "paper":
        return "user1 win"
    elif user1 == "rock" and user2 == "scissors":
        return "user1 win"
    elif user1 == "rock" and user2 == "rock":
        return "drawn"
    elif user1 == "rock" and user2 == "paper":
        return "user2 win"


def guess_the_number():
    number1 = random.randrange(1, 10)

    user3 = None
    while user3 != number1:
        user3 = int(input('enter number: '))
    return 'You win'


def mainmenu():
    users = input("choose your game: rock paper or guess the number? ")
    if users == 'rock':
        print(rock_paper_scissors())
    elif users == 'guess':
        print(guess_the_number())

mainmenu()
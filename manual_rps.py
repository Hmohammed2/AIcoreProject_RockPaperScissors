import random as rd


class Game:

    def __init__(self):
        # instantiate list for possible choices in game
        self.possible_actions = ["rock", "paper", "scissors"]
        self.user_choice = input("Enter a choice (rock, paper, scissors): ")

    def get_computer_choice(self):
        # method simulates a computer choosing between rock, paper and scissors
        computer_action = rd.choice(self.possible_actions)
        return computer_action

    def get_user_choice(self):
        # Method gets user choice
        if self.user_choice in self.possible_actions:
            print(f"You picked {self.user_choice}")
        else:
            print("You can only pick between Rock, Paper, Scissors")
            raise KeyError
        return self.user_choice

    def get_winner(self):
        computer_choice = self.get_computer_choice()
        user_choice = self.user_choice

        print(f"Computer picks {computer_choice}")

        if user_choice == computer_choice:
            print(f"You picked {user_choice} and computer picked {computer_choice}. Its a tie!")
        elif user_choice == "rock":
            if computer_choice == "paper":
                print("Too bad you lose! Paper beats rock!")
            else:
                print("Well done you win! Rock smashes scissors")
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("Well done you win! Paper beats rock!")
            else:
                print("Too bad you lose! Scissors cuts paper!")
        elif user_choice == "scissors":
            if computer_choice == "rock":
                print("Too bad you lose! Rock smashes scissors!")
            else:
                print("Well done you win! Scissors cuts paper!")


def play():
    while True:
        init = Game()
        init.get_winner()

        play_again = input("Play again (y/n)")
        if play_again.lower() != "y":
            break


if __name__ == '__main__':
    play()

"""In the game Rock Paper Scissors, two players simultaneously choose one of three
options: rock, paper, or scissors. If both players choose the same option, then the
result is a tie. However, if they choose differently, the winner is determined as
follows:
l
Rock beats scissors, because a rock can break a pair of scissors.
l
Scissors beats paper, because scissors can cut paper.
l
Paper beats rock, because a piece of paper can cover a rock.
Create a game in which the computer randomly chooses rock, paper, or scissors.
Let the user enter a number 1, 2, or 3, each representing one of the three choices.
Then, determine the winner. Save the application as RockPaperScissors.java.
(In the chapter Characters, Strings, and the StringBuilder, you will modify the
game so that the user enters a string for rock, paper, and scissors, rather than just
entering a number.)"""

from random import choice


class RPS:
    def __init__(self):
        self.choices = [1, 2, 3]
        self.computer_count = 0
        self.human_count = 0

    def computer_play(self, cc):
        self.cc = cc

    def human_play(self, hc):
        self.hc = hc

    def check_winner(self):
        if self.cc == self.hc:
            print("It is a tie")
        elif self.cc == 1 and self.hc == 2:
            print("Human wins because paper can cover a rock")
            self.human_count += 1
        elif self.cc == 2 and self.hc == 1:
            print("Computer wins because paper can cover a rock")
            self.computer_count += 1
        elif self.cc == 1 and self.hc == 3:
            print("Computer wins because rock can break scissors")
            self.computer_count += 1
        elif self.cc == 3 and self.hc == 1:
            print("Human wins because rock can break scissors")
            self.human_count += 1
        elif self.cc == 2 and self.hc == 3:
            print("Human wins because scissors can cut paper")
            self.human_count += 1
        elif self.cc == 3 and self.hc == 2:
            print("Computer wins because scissors can cut paper")
            self.computer_count += 1

    def count_wins(self):
        s = "Computer won {0} times and human won {1} times".format(self.computer_count, self.human_count)
        print(s)


def game_play():
    game = RPS()
    for i in range(5):
        human_choice = int(input("Enter your choice 1 for rock, 2 for paper and 3 for scissors: "))
        game.human_play(human_choice)
        print("Human has played", human_choice)

        computer_choice = choice([1, 2, 3])
        game.computer_play(computer_choice)
        print("Computer has played", computer_choice)

        game.check_winner()
    game.count_wins()

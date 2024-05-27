import random
from colorama import init, Fore, Style

init()

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RockPlayer(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        self.their_last_move = None

    def move(self):
        if self.their_last_move is None:
            return random.choice(moves)
        else:
            return self.their_last_move

    def learn(self, my_move, their_move):
        self.their_last_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.move_index = 0

    def move(self):
        move = moves[self.move_index]
        self.move_index = (self.move_index + 1) % len(moves)
        return move


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Enter your move (rock, paper, or scissors): ").lower()
            if move in moves:
                return move
            else:
                print("Invalid move! Please enter rock, paper, or scissors.")


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = 0
        self.player2_score = 0

    def play_round(self):
        move1 = self.player1.move()
        move2 = self.player2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            print(f"{Fore.GREEN}Player 1 WINS!{Style.RESET_ALL}")
            self.player1_score += 1
        elif beats(move2, move1):
            print(f"{Fore.GREEN}Player 2 WINS!{Style.RESET_ALL}")
            self.player2_score += 1
        else:
            print(f"{Fore.YELLOW}It's a tie!{Style.RESET_ALL}")
        print(f"Score: Player 1 - {self.player1_score}, Player 2 - {self.player2_score}")

    def play_game(self):
        print("Game start!")
        round_count = 0
        while True:
            self.play_round()
            round_count += 1
            if self.player1_score == 3:
                print(f"{Fore.GREEN}Player 1 WINS THE GAME!{Style.RESET_ALL}")
                break
            elif self.player2_score == 3:
                print(f"{Fore.GREEN}Player 2 WINS THE GAME!{Style.RESET_ALL}")
                break
            if round_count == 5:
                continue_playing = input(
                    "Do you want to continue playing? (yes or no): ").lower()
                if continue_playing != 'yes':
                    break
                else:
                    round_count = 0
        print(f"Final Score: Player 1 - {self.player1_score}, Player 2 - {self.player2_score}")
        if self.player1_score > self.player2_score:
            print(f"{Fore.GREEN}Player 1 is the overall winner!{Style.RESET_ALL}")
        elif self.player2_score > self.player1_score:
            print(f"{Fore.GREEN}Player 2 is the overall winner!{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}The game is a tie!{Style.RESET_ALL}")


if __name__ == '__main__':
    players = {
        '1': RockPlayer,
        '2': RandomPlayer,
        '3': ReflectPlayer,
        '4': CyclePlayer,
        '5': HumanPlayer
    }
    print("Player list:")
    for number, player in players.items():
        print(f"{number}. {player.__name__}")

    while (player1_choice := input("Choose player 1: ")) not in players.keys():
        print("Invalid choice, please select player 1 from the list.")

    while (player2_choice := input("Choose player 2: ")) not in players.keys():
        print("Invalid choice, please select player 2 from the list.")

    game = Game(players[player1_choice](), players[player2_choice]())
    game.play_game()

    while True:
        start_new_game = input("Do you want to start a new game? (yes or no): ").lower()
        if start_new_game == 'yes':
            while (player1_choice := input("Choose player 1: ")) not in players.keys():
                print("Invalid choice, please select player 1 from the list.")
            while (player2_choice := input("Choose player 2: ")) not in players.keys():
                print("Invalid choice, please select player 2 from the list.")
            game = Game(players[player1_choice](), players[player2_choice]())
            game.play_game()
        else:
            print("Bye!")
            break

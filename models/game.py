import time
import random


class Game:
    def __init__(self):
        self._player_turn = ""
        self._opponent_turn = ""
        self._result = ""
    
    
    def play(self):
        print("Rock")
        time.sleep(1)
        print("Paper")
        time.sleep(1)
        print("Scissors")
        time.sleep(1)
        print("Shoot!")
        self._player_turn = input("Make your move: ")
        if self._player_turn.lower() == "rock":
            print("You have chosen rock.")
        elif self._player_turn.lower() == "paper":
            print("You have chosen paper.")
        elif self._player_turn.lower() == "scissors":
            print("You have chosen scissors.")
        else:
            print("❌ ERROR : Please type exactly 'rock', 'paper' or 'scissors'.")

        options = ["rock", "paper", "scissors"]
        self._opponent_turn = random.choice(options)
        print(f"The opponent has chosen { self._opponent_turn}.")

        wins = 0
        defeat = 0
        draw = 0

        if self._player_turn.lower() == "rock" and  self._opponent_turn.lower() == "scissors":
            wins += 1
            print("Victory!")
        elif self._player_turn.lower() == "rock" and  self._opponent_turn.lower() == "paper":
            defeat += 1
            print("Defeat...")
        elif self._player_turn.lower() == "rock" and  self._opponent_turn.lower() == "rock":
            draw += 1
            print("Draw.")
        elif self._player_turn.lower() == "paper" and  self._opponent_turn.lower() == "rock":
            wins += 1
            print("Victory!")
        elif self._player_turn.lower() == "paper" and  self._opponent_turn.lower() == "scissors":
            defeat += 1
            print("Defeat...")
        elif self._player_turn.lower() == "paper" and  self._opponent_turn.lower() == "paper":
            draw += 1
            print("Draw...")      
        elif self._player_turn.lower() == "scissors" and  self._opponent_turn.lower() == "paper":
            wins += 1
            print("Victory!")
        elif self._player_turn.lower() == "scissors" and  self._opponent_turn.lower() == "rock":
            defeat += 1
            print("Defeat...")
        elif self._player_turn.lower() == "scissors" and  self._opponent_turn.lower() == "scissors":
            draw += 1
            print("Draw...")

game1 = Game()
game1.play()
    

    

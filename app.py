#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "Player wins"
    else:
        return "Computer wins"

def main():
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("Choose rock, paper, or scissors: ").lower()

        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(f"Result: {result}")

        if result == "Player wins":
            player_score += 1
        elif result == "Computer wins":
            computer_score += 1

        print(f"Player Score: {player_score}")
        print(f"Computer Score: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Game over!")
    print(f"Final Score - Player: {player_score}, Computer: {computer_score}")

if __name__ == "__main__":
    main()
  

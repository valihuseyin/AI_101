# Pseudo-code:
# 1. Loop to allow replaying the game.
# 2. Ask Player 1 for their move (rock, paper, or scissors).
# 3. Ask Player 2 for their move (rock, paper, or scissors).
# 4. Validate both moves.
# 5. Compare moves:
#    - If moves are the same, it's a tie.
#    - Else, determine the winner based on the rules.
# 6. Print a congratulations message to the winner.
# 7. Ask if players want to play again.
# 8. If yes, repeat; if no, exit.

# Implementation:
def get_move(player):
    move = input(f"{player}, enter your move (rock, paper, scissors): ").strip().lower()
    while move not in ['rock', 'paper', 'scissors']:
        print("Invalid move. Please choose rock, paper, or scissors.")
        move = input(f"{player}, enter your move (rock, paper, scissors): ").strip().lower()
    return move

def determine_winner(move1, move2):
    if move1 == move2:
        return None
    if (move1 == 'rock' and move2 == 'scissors') or \
       (move1 == 'scissors' and move2 == 'paper') or \
       (move1 == 'paper' and move2 == 'rock'):
        return 1
    else:
        return 2

def main():
    while True:
        move1 = get_move("Player 1")
        move2 = get_move("Player 2")
        winner = determine_winner(move1, move2)
        if winner is None:
            print("It's a tie!")
        else:
            print(f"Congratulations Player {winner}, you win!")
        again = input("Would you like to play again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
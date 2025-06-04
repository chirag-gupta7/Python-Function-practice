import random

options = ['🍒',' 🍇', '🍉', '7️⃣']

play_option = input("Do you want to play? (Y/N): ").lower()
while play_option == 'y':
    def play():
        results = random.choices(options, k=3)
        
        print(f"{results[0]} | {results[1]} | {results[2]}")
        
        if all(symbol == '7️⃣' for symbol in results):
            print("Jackpot! 💰")
            print("You are the hero of this game!")
        else:
            print("HAHA you got fucked hahahahaha")
            print("You lose! 😢")
            print("Thanks for playing!")
            print("Better luck next time!")
    
    play()
    play_option = input("Do you want to play again? (Y/N): ").lower()
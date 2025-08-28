import random  # Step 1: Import module

# Game settings
MIN_NUM = 1
MAX_NUM = 10
MAX_ATTEMPTS = 5

def play_game():
    random_number = random.randint(MIN_NUM, MAX_NUM)
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        try:
            guess = int(input(f"Guess a number between {MIN_NUM} and {MAX_NUM}: "))
        except ValueError:
            print("❌ Please enter numbers only!")
            continue

        if not (MIN_NUM <= guess <= MAX_NUM):
            print(f"⚠️ Please enter a number between {MIN_NUM} and {MAX_NUM}!")
            continue

        attempts += 1

        if guess == random_number:
            print("🎉 You WIN!")
            return True
        elif abs(guess - random_number) == 1:
            print("🔥 Very close!")
        elif guess > random_number:
            print("📈 Too high!")
        else:
            print("📉 Too low!")

    print(f"💀 You LOSE! The number was {random_number}")
    return False


# Game loop
wins = 0
losses = 0

while True:
    if play_game():
        wins += 1
    else:
        losses += 1

    print(f"📊 Score: {wins} Wins - {losses} Losses")

    play_again = input("Play again? (y/n): ").strip().lower()
    if play_again != "y":
        print("👋 Thanks for playing!")
        break


import random  # Step 1: Import module

# Game setting 
MIN_NUM = 1
MAX_NUM = 10
MAX_ATTEMPT = 5

def play_game():

    # Create random number
    # Step 2: Pick number between 1 and 10
    random_number = random.randint(1, 10)
    attempts = 0

    while attempts < MAX_ATTEMPT:

        # Add Exception Handling
        try:
            # Step 3: Get user input
            guess = int(input(f"guess number between {MIN_NUM} to {MAX_NUM}:"))
        except ValueError:
            print("please enter number only!")
            continue    # Skip the rest and ask again

        if not (MIN_NUM <= guess <= MAX_NUM):
            print(f"❌ Please enter a number between {MIN_NUM} and {MAX_NUM}!")
            continue

        attempts += 1
        if guess == random_number:
            print("🎉You WIN!")
            return True
        elif abs(guess - random_number) == 1:
            print("🔥Very close!")
        elif guess > random_number:
            print("📈 Too high!")
        else:
            print("📉 Too low!")

    print("💀 You LOSE! The number was {}".format(random_number))
    return False

# Game loop
wins = 0
losses = 0

while True:
    if play_game():
        wins += 1
    else:
        losses += 1

    print(f"Score:{wins} Wins - {losses} losses")   # f - is shor cut of .format()

    play_again = input("Play again? (y/n)").strip().lower() #.strip() - It’s useful when you want to clean up user input, because people often accidentally type extra spaces before or after what they enter.
    if play_again != "y":
        print("Thanks for playing! 👋")
        break

# You’ve already got:

# 1.Random number generation

# 2.Input validation

# 3.Attempt limit

# 4.Win/lose messages

# 5.Replay loop

# 6.Score tracking    

import random

num = random.randint(1, 100)
difficulty = input("Type 'Easy' or 'Hard': ")
if difficulty == "Easy":
    attempts = 10
else:
    attempts = 5
print(f"You have {attempts} attempts of guessing a number")

while attempts != 0:
    guess = int(input("guess a number :"))
    if guess > num:
        print("Too High \nguess again")
        attempts -= 1
        print(f"you have {attempts} attempts left")
    elif guess < num:
        print("Too Low \nguess again")
        attempts -= 1
        print(f"you have {attempts} attempts left")
    if guess == num:
        print("you won")

if attempts == 0:
    print("you lost")


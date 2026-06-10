num = 57
round = 0
while round <= 2:
    guess = int(input("Guess the number between 0 and 100"))
    if guess == num:
        print("CORRECT")
        break
    else:
        round += 1

print(f"Correct number is {num}")

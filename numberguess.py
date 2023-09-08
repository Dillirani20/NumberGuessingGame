import math
import random

start = int(input("Enter starting number: "))
end = int(input("Enter finishing number: "))

x = random.randint(start, end)
print("You have ", round(math.log(end-start+1, 2)), "chances to guess the number")
count = 0

while count < math.log(end-start+1,2):
    count += 1
    guess = int(input("Enter number to guess: "))

    if x == guess:
        print("You have guessed the right number in", count, "turn")
        break
    elif x > guess:
        print("You guessed the number which is too small")
    elif x < guess:
        print("You guessed the number which is too high")

if count >= math.log(end-start+1, 2):
    print("You have reached your guess limit \n")
    print("Better luck next time!")
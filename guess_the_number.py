import random

print("You'll have to guess a random number between 0 and 100. You have 5 tries")

number_to_guess = random.randint(0, 101)

for tries in range(5):

  guess = int(input())

  if guess < number_to_guess:
    print("Your guess is too low, what about " + str(guess+1))
  elif guess > number_to_guess:
    print("Your guess is too high, what about " + str(guess-1))
  else:
    break
    

if guess == number_to_guess:
  print("Yes!!! " + str(guess) + " is the number. You rock!")
else:
  print("You loose, the number was " + str(number_to_guess))

  



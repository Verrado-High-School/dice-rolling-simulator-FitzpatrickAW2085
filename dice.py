# Alan Fitzpatrick
#Period 4

import random


rollNumber = 0
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0


print()


print ("Welcome to the Dice Rolling Simulator!")


print()


playerChoice = int(input("Enter how many times would you like to roll the dice: "))

print()


while True:
	rollNumber = rollNumber + 1
	randomNum = random.randint(1,6)
	print ("Roll number: " + str(rollNumber) + "  " + "Dice landed on: " + str(randomNum))
	if rollNumber >= playerChoice:
		if randomNum == 1:
			ones = ones + 1
		elif randomNum == 2:
			twos = twos + 1
		elif randomNum == 3:
			threes = threes + 1
		elif randomNum == 4:
			fours = fours + 1
		elif randomNum == 5:
			fives = fives + 1
		elif randomNum == 6:
			sixes = sixes + 1
		break

	elif randomNum == 1:
		ones = ones + 1
	elif randomNum == 2:
		twos = twos + 1
	elif randomNum == 3:
		threes = threes + 1
	elif randomNum == 4:
		fours = fours + 1
	elif randomNum == 5:
		fives = fives + 1
	elif randomNum == 6:
		sixes = sixes + 1


print()


print ("Results after rolling the dice " + str(playerChoice) + " times: ")


print()


print ("The amount of times the dice landed on one: " + str(ones))
print ("The amount of times the dice landed on two: " + str(twos))
print ("The amount of times the dice landed on three: " + str(threes))
print ("The amount of times the dice landed on four: " + str(fours))
print ("The amount of times the dice landed on five: " + str(fives))
print ("The amount of times the dice landed on six: " + str(sixes))


print()


print ("Probability of One rolled: " + str(((ones) / (rollNumber))*100) + " " + "%")
print ("Probability of Two rolled: " + str(((twos) / (rollNumber))*100) + " " + "%")
print ("Probability of Three rolled: " + str(((threes) / (rollNumber))*100) + " " + "%")
print ("Probability of Four rolled: " + str(((fours) / (rollNumber))*100) + " " + "%")
print ("Probability of Five rolled: " + str(((fives) / (rollNumber))*100) + " " + "%")
print ("Probability of Six rolled: " + str(((sixes) / (rollNumber))*100) + " " + "%")

print()
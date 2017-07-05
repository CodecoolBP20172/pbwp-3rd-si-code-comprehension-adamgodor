import random  # import the module called 'random'

guessesTaken = 0  # create a global variable, set its value to zero

print('Hello! What is your name?')  # print the following string to console
myName = input()  # ask the user for an input, this input will the value of the 'myName' var

number = random.randint(1, 20)  # pick a random int between 1 and 20, this int will be under the name 'number'
# print 'myName' var between two pieces of string
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:  # initialize a while loop
    print('Take a guess.')  # print the following str to console
    guess = input()  # ask the user for input, this input will be the value of the 'guess' var
    guess = int(guess)  # convert the 'guess' string into integer

    guessesTaken += 1  # add 1 to the 'guessesTaken' value

    if guess < number:  # initialize an if statment
        # if the statement ('guess' var is smaller than 'number' var) true, print the following str
        print('Your guess is too low.')

    if guess > number:  # initialize an if statment
        # if the statement ('guess' var is bigger than 'number' var) true, print the following str
        print('Your guess is too high.')

    if guess == number:  # initialize an if statment
        break  # if the statement is true, stop the while loop

if guess == number:  # initialize an if statment
    guessesTaken = str(guessesTaken)  # convert the guessesTaken var into a string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
    # print 'myName'and 'guessesTaken' var between two pieces of string

if guess != number:  # initialize an if statment
    number = str(number)  # convert the 'number' var into a string
    print('Nope. The number I was thinking of was ' + number)
    # print the following statement to console

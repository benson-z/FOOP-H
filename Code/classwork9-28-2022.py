import random

#an example of a loop that continually asks for input from the user until a specific result is given; in this case a number aggregator 
# answer = input("Please enter a number, type 'quit' to get the sum of all your numbers\n").lower()
# sum = 0
# #while true:
# #  run the indented code
# while (answer!='quit'):
#   sum = sum + int(answer)
#   answer = input("Please enter a number, type 'quit' to get the sum of all your numbers\n").lower()
# print("The sum is:", sum)

#FOR YOU TO DO:
#Write a program that stores a random, secret number in a variable (you decide the range of this secret number)
#The user has to guess the secret number, the program should loop until they get it right.
#Once the user has guessed correctly they get a congratulations message
#challenge - use conditionals to give the user higher/lower hints
a = random.randint(0, 100)
guess = None
while guess != a:
    guess = int(input("Guess a number\n"))
    if guess > a:
        print("Lower")
    elif guess < a:
        print("Higher")
print("You got the number!")


# Uncomment and fix this code
counter = 1
while counter < 5:
    print("Hello")
    counter += 1
print ("The loop has ended")

# #Figure out what sum will be at the end, uncomment, then check your answer
# sum=0
# num=1
# while(num<=4):
#   sum=sum+num
#   num = num + 1
# print(sum)
# Sum = 10

#Write a program that uses a loop to output the seven times table up to 12 x 7 ex.7, 14, 21, ... 
#Challenge - add user input so they choose the number, not necessarilly 7.
#Challenge - format the output better.  Example - '1 x 7 = 7'  '2 x 7 = 14'

interval = int(input("Choose a interval: "))
for a in range(1, 13):
    print(a, "x", interval, "=", a*interval)
import random
n= random.randint(1, 99)
print("This game is to guess number\n")
print("You have got 10 chances to guess a random number\n which will be between 1  to 100\n")
print("The game will suggest if your number is high or low compare to gussing number\n")
print("Good luck\n")
print("Enter number\n")
i=0
p=10

while(i<p):

    s = int(input())
    if(s>n):
        print("your number is greater than random number")


    elif(s<n):
        print("try again!!!!!")
        print("your number is smaller than random number")

    if(s==n):
        print("Congratulation!!!!!!\n YOU WON\n")
        print("The number is\n"+str(n))
        break

    i += 1
    z=p-i
    print("you left with {} chances".format(z))


    if (i >= p):
        print("you have exceed your chances\n\nBetter Luck next time")
        print("The random number is = {} ".format(n))
        break





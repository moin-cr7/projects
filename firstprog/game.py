import random
lst=["s","p","v"]
won=0
lost=0
tie=0
i=1
l=20

while i<=l :

    print("Enter your choice as \n\tSTONE=s\n\tPAPER=p\n\tSCISOR=v")
    g=random.choice(lst)
    print(g)
    x = input(str().lower())
    i+=1
    if (g=="s" and x=="p" or g=="p" and x=="v" or g=="v" and x=="s"):
        print("you won")
        won+=1
        print(won)
    elif(g=="p" and x=="s" or g=="v" and x=="p" or g=="s"and x=="v" )    :
        print("you lost")
        lost+=1
        print(lost)
    elif(g==lst and x=="s","p","v"):
        print("tie")
        tie=tie+1
def dec(result) :
    def op():
        print("===================")
        result()
        print("===================")
    return op
@dec
def resultt():
    if(won>lost):
        print(f"Lost={lost},\nWon={won},\nTie={tie}")
        print("you won the game by \n"+str(won)+"/"+str(lost+won+tie))
    elif(lost>won):
        print(f"Lost={lost},\nWon={won},\nTie={tie}")
        print("You lost game by \n "+str(lost)+"/"+str(won+lost+tie))

resultt()

import random
from hangman_parts import parts
from time import sleep
words=["rose","lotus","lily","poppy","hibiscus","snowdropsed"]
# words=["python","hangman"]
pick=random.choice(words)
print("the word has",len(pick),"letters")

right=["_"]*len(pick)
wrong=[]

def update():
    for i in right:
        print(i,end=" ")
    print()
print("Let me think")
def wait():
    for i in range(7):
        print(".",end="")
        sleep(.7)
    print()
wait()

update()
parts(len(wrong))

while True:
    
    print("==========================")
    
    guess=input("guess the letter:-")
    print("let me check")
    wait()
    
    if guess in pick:
        index=0
        for i in pick:
            if i==guess:
                right[index]=guess
            index+=1
        update()
    else:
        if guess not in wrong:
            wrong .append(guess)
            parts(len(wrong))
        else:
            print("you already guess that")
    if len(wrong)>=5:
        print("you lose")
        print("The correct wors is",pick)
        break
    if "_" not in right:
        print("you win")
        break

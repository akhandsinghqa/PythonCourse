# We all have played snake, water gun game in our childhood. If you haven’t, google the
# rules of this game and write a python program capable of playing this game with the
# user.
import random

inputDict = {"s": 1, "w": 0, "g": -1}

outDict = {1: "Snake", 0: "Water", -1: "Gun"}

com = random.choice([1, 0, -1])

you_str = input("Enter you choice (s : snake,w : water,g : gun) : ")
you = inputDict.get(you_str)

if you == None:
    print("Error : Valid input not entered like s,w,g.\nTry again........")
else:
    print(f"You choose {outDict.get(you)}.\nComputer choose {outDict.get(com)}")
    if you == com:
        print("Game is draw.")
    else:
        """
        if(you==1 and com==0): # 1
            print("You won !")
        elif(you==1 and com==-1): # 2
            print("You lose !")
        elif(you==0 and com==-1): # 1
            print("You won !")
        elif(you==0 and com==1): # -1
            print("You lose !")
        elif(you==-1 and com==1): # -2
            print("You won !")
        elif(you==-1 and com==0): # -1
            print("You lose !")
        """
        if (you - com) == 1 or (you - com) == -2:
            print("You won !")
        else:
            print("You lose !")

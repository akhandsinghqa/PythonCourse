# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hi-
# score whenever the game() function breaks the Hi-score.

fname = "Hi-score.txt"


# def create_file():
#     f = open(fname, "w")
#     f.close()


def read_file():
    with open(fname, "r") as rf:
        hiscore = rf.read()
        if hiscore != "":
            return int(hiscore)
        else:
            return 0


def game(score, hiscore):
    print("Your score is :", score)
    if score > hiscore:
        with open(fname, "w") as wf:
            wf.write(str(score))
            print("Your score is hi-score.")


# create_file()
hi_score = read_file()
game(101, hi_score)
print(f"The high score is : {read_file()}")

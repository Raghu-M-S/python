import random
def play():
    i = input("'r' for rock 'p' for paper 's' for scissor\n")
    choice = random.choice(['r','p','s'])
    if i==choice:
        return "match tie"
    if is_win(i,choice):
        return "you won"
    return 'you lost'

def is_win(computer,user):
    if (user=='r' and computer=='s')or(user=='s' and computer=='p')or(user=='p' and computer=='r'):
        return True

print(play())

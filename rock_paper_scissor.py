import random

def play():
    
        user = input("'r' for rock, 'p' for paper, 's' for scissor, 'e' to end: ")
        computer = random.choice(['r', 's', 'p'])

        if user == computer:
            return 'tie'
        
        # r>s , p>r, s>p 

        if is_win(user, computer):
            return 'you Won!'
        
        return 'you lost'



def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())
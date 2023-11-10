# import using import keyword
import random

random.randint(1,10)  # the value generated is between 1 and 9 but you can not get 10
heads_tally = 0
tails_tally = 0

def coin_flip():
    """Randomly return head or tail"""
    if(random.randint(0,1) == 0):
        return "head"
    else:
        return "tail"
for i in range(10_000):
    if coin_flip() == "head":
        heads_tally = heads_tally + 1
    else: 
        tails_tally = tails_tally + 1

# get_coin_flip = coin_flip()
# print(get_coin_flip)
ratio = heads_tally / tails_tally
print(f"The ratio of head {heads_tally} to tail {tails_tally} is {ratio}")
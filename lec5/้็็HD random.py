import random

head = 1
tail = 2
tosses = int(input("How many time tosscoin :"))

def toss_coin():
  for toss in range(tosses):
    if random.randint(head, tail) == head:
       print("Head")
    else:
       print("Tail")

toss_coin()
       

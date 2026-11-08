#) version 1 - random.choice()

import random

friends = ["Alice", "Bob", "Charlie", "Dana", "Ella"]

payer = random.choice(friends)

print(f"{payer} is paying the bill today!")


#) version 2 - random.randint() and indexing

num_friends = len(friends)

index = random.randint(0, num_friends - 1)

payer = friends[index]

print("\nVersion 2:")
print(f"{payer} is paying the bill today!")
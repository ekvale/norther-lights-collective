import random
from random import sample

valid_code = []
code = [0,1,2,3,4]

for x in range(len(code) ** len(code)):
    valid_code.append((sample(code, 5)))

valid_code = set(tuple(x) for x in valid_code)

for x in valid_code:
    if x[0] == x[1] / 2:
        if x[2] < x[4]:
            print(x)

print(len(valid_code))

scores = [random.randrange(1, 11, 1) for i in range(10)]

sorted_scores = sorted(scores)

print(sorted_scores)
print(sorted_scores[-2])



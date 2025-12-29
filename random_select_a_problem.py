import random

done = []

while True:
    res = random.randint(1, 101)
    if res not in done:
        print(res)
        quit()
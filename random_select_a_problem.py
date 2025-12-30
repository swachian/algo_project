import random

done = [8, 10, 14, 15, 17, 26, 40, 42, 45, 48, 52, 60, 86, 89, 91, 93, 97, 98, 72, 66, 
        33, 5, 55, 37, 62, 64, 69, 47, 32, 12, 78, 23]

while True:
    res = random.randint(1, 101)
    if res not in done:
        print(res)
        quit()
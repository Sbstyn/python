import random
num = 0
y = []
list2 = []
times = 1
while times <= 1000:
    while len(y) < 100:
        x = random.randint(1,100)
        y.append(x)
        y = list(dict.fromkeys(y))
        num = num + 1
        #print("\n", num)
        #print(y)
        """if len(y) < 25:
            print("-")
        elif len(y) < 50:
            print("--")
        elif len(y) < 75:
            print("---")
        else:
            print("----")"""

    times = times + 1
    list2.append(num)
    #print("av: ", sum(list2) / len(list2))
    num = 0
    y = []
print("av: ", sum(list2) / len(list2))
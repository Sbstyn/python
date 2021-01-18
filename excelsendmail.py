import sendemail
import random

importdata = []
data = []
players = []

f = open("C:\\Users\\sebes\\Desktop\\web\\chessleaguepy\\database.txt", "r")

for words in f:
    importdata.append(words)

for words in importdata:
    words = words.rstrip()
    data.append(words)
print(data)

x = 0

while x < len(data):
    if x % 2 == 0:
        players.append(data[x])
    x += 1
print(players)

def choosePairs():
    random.shuffle(players)
    opponent1 = random.choice(players)
    opponent2 = random.choice(players)
    if opponent1 == opponent2:
        choosePairs()
    else:
        print(opponent1, opponent2)
        players.remove(opponent1)
        players.remove(opponent2)
        print(players)

        address = data[data.index(opponent1) + 1]
        print(address)
        subject = opponent1 + "! This round you are playing with: " + opponent2 + ", his/her gmail adress: " + data[data.index(opponent2) + 1]
        print(subject)
        #sendemail.sendGmail(adress, subject)

        address = data[data.index(opponent2) + 1]
        print(address)
        subject = opponent2 + "! This round you are playing with: " + opponent1 + ", his/her gmail adress: " + data[data.index(opponent1) + 1]
        print(subject)
        #sendemail.sendGmail(adress, subject)

        if len(players) - 2 < 0:
            if len(players) == 1:
                address = data[data.index(players[0]) + 1]
                print(address)
                subject = players[0] + "! You didn't get paired this round, instead you get 0,5 point."
                print(subject)
            print("Pairing Ended!")
        else:
            choosePairs()
choosePairs()
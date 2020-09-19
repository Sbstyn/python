import random

"""
by:
╔══╗░╔╗░░╔═╦╗░░░░░░░░╔═╦═╗░░░░╔╗░░░░░░
║══╬═╣╚╦═╣═╣╚╦╦╦═╦═╦╗║║║║╠═╗╔╦╣╚╦═╦═╦╗
╠══║╩╣╬║╩╬═║╔╣║║╩╣║║║║║║║║╬╚╣╔╣╔╣╬║║║║
╚══╩═╩═╩═╩═╩═╬╗╠═╩╩═╝╚╩═╩╩══╩╝╚═╩═╩╩═╝
░░░░░░░░░░░░░╚═╝░░░░░░░░░░░░░░░░░░░░░░



╬╬╬╬╬╬╬╬╬╬
╬╬╬╬╬╬╬╬╬╬
╬╬•╬╬╬╬╬╬╬
╬╬╬╬╬╬╬╬•╬
╬╬╬╬╬╬╬╬╬╬

Home: x:0 y:0
Player: x:6 y:-1
(Optimal path takes 7 decision)
"""

x = 6
y = -1

dec = 0

fail = False

while x != 0 or y != 0 and fail != True:
    c = random.choice(["N","S","W","E"])
    if c == "N":
        y += 1
    elif c == "S":
        y += -1
    elif c == "W":
        x += -1
    elif c == "E":
        x += 1
    dec += 1
    #print("x: ", x ," y: ", y ,"   Choice: ", c ,"   Decisions: ", dec ,sep="")

    if -1000 >= x or x >= 1000 or -1000 >= y or y >= 1000:
        fail = True
        print("Fail...")
        break
print("x: ", x ," y: ", y ,"   Choice: ", c ,"   Decisions: ", dec ,sep="")
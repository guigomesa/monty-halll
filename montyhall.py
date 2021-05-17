import random

class door():
    def __init__(self, prize):
        self.prize = prize

class event:
    def __init__(self, doorChoice):
        
        self.doors = list()
        self.doors.append(door("Ferrari"))
        self.doors.append(door("Goat"))
        self.doors.append(door("Donkey"))

        random.shuffle(self.doors)
        self.choice = doorChoice

    def montyHall(self):

        if(self.doors[self.choice].prize=="Ferrari"):
            self.doors = filter(lambda door: "Goat"!= door.prize,self.doors)
        elif(self.doors[self.choice].prize=="Goat"):
            self.doors = filter(lambda door: "Donkey" != door.prize,self.doors)
        else:
            self.doors = filter(lambda door: "Goat" != door.prize,self.doors)
        
        self.doors = list(self.doors)

    def changeChoice(self):
        if(self.choice == 0):            
            self.choice = 1
        else:
            self.choice = 0


    def win(self):
     
        try:
            return "Ferrari" in self.doors[self.choice].prize
        except:
            return False

    

win = list()
defeat = list()


for x in range(0,1000):
    doorChoosed = random.randint(0,2)

    ev = event(doorChoosed)

    ev.montyHall()

    ev.changeChoice()

    result = ev.win()

    if(result):
        win.append(result)
    else:
        defeat.append(result)
    

totalWin = len(win)
totalDefeat = len(defeat)

print("Total win "+str(totalWin))
print("Total defeat "+str(totalDefeat))

percentVictory = ((totalWin*100) / (totalWin+totalDefeat))
percentDefeat = ((totalDefeat*100) / (totalWin+totalDefeat))

print(str(percentVictory)+"% victory")
print(str(percentDefeat)+"% defeat")

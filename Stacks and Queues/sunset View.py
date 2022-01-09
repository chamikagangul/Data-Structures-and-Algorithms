
import random


class Stack:


    def __init__(self):
        self.array = []

    def __init__(self,array):
        self.array = array

    def __str__(self) -> str:
        return str(self.array)

    def empty(self):
        return len(self.array)==0

    def pop(self):
        if not self.empty():
            return self.array.pop()
        else:
            return 0

    def push(self,e):
        self.array.append(e)

    def len(self):
        return len(self.array)

def getBuildingsWithSunsetView(buildings):
    buildingsWithSunsetView = Stack([])
    while(not buildings.empty()):
        lastBuilding = buildings.pop()
        # print(lastBuilding)
        lastbuildingwithSunsetView = -float('inf')
        while(lastBuilding>=lastbuildingwithSunsetView and not buildingsWithSunsetView.empty()):
            lastbuildingwithSunsetView = buildingsWithSunsetView.pop()
        
        if(lastbuildingwithSunsetView>0):
            buildingsWithSunsetView.push(lastbuildingwithSunsetView)
        buildingsWithSunsetView.push(lastBuilding)
    return buildingsWithSunsetView


buildings = Stack([random.randrange(0,100) for _  in range(10)])

print(buildings)
x = getBuildingsWithSunsetView(buildings)

print(x)
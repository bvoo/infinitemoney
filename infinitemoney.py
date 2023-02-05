# This generates infinite money :3

from random import shuffle, randint, choice

class Letter():
    def __init__(self):
        return

    def giveValue(self,value):
        self.value = value
       
        self.letterM = 'M'
        self.lettero = 'o'
        self.lettern = 'n'
        self.lettere = 'e'
        self.lettery = 'y'
        
        if (value == self.letterM):
            self.value = self.letterM
        elif (value == self.lettero):
            self.value = self.lettero
        elif (value == self.lettern):
            self.value = self.lettern
        elif (value == self.lettere):
            self.value = self.lettere
        elif (value == self.lettery):
            self.value = self.lettery
        
        return self.value

class Generator():
    def __init__(self, resources) -> None:
        while True:
            self.resources = resources.copy()
            self.money = self.generateMoney(self.resources)
            self.printMoney(self.money)
        return

    def generateMoney(self, resources):

        money = ['a', 'a', 'a', 'a', 'a']
        self.allowedLetters = resources
        self.allowedOrder = [0, 1, 2, 3, 4]
        while (len(self.allowedOrder) > 0 and self.allowedLetters[0] not in money):
            place = choice(self.allowedOrder)
            money[place] = self.allowedLetters[0]
            self.allowedLetters.pop(0)
            self.allowedOrder.pop(self.allowedOrder.index(place))

        while (not self.testMoney(money)):
            shuffle(money)

        return money

    def testMoney(self, money):
        self.result = ""
        self.result += money[0]
        self.result += money[1]
        self.result += money[2]
        self.result += money[3]
        self.result += money[4]

        if self.result == "Money":
            return True

    def printMoney(self, money):
        print(money[0], end='')
        print(money[1], end='')
        print(money[2], end='')
        print(money[3], end='')
        print(money[4], end='\n')
        return

let = Letter()
allowedLetters = [let.giveValue('M'), let.giveValue('o'), let.giveValue('n'), let.giveValue('e'), let.giveValue('y')]
gen = Generator(allowedLetters)

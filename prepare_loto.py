import random

class Bag:

    def __init__(self):
        self.samples = [i for i in range(1, 91)]
    #достаем бочонок с номером из мешочка
    def select_sample(self):
        return self.samples.pop(random.randrange(len(self.samples)))



#карточка игрока,заполнена цифрами в три  строки по пять в каждой
#цифры в карточке не повторяются,и расположены по возрастанию в строке

class Ticket:
    def __init__(self):
        self.numbers = []
        while len(self.numbers) < 15:
            i = random.randrange(1, 91)
            if i not in self.numbers:
                self.numbers.append(i)
        self.strings = {}
        for i in range(3):
            self.strings[i] = self.numbers[i*5:i*5 + 5]
            self.strings[i].sort()

#Изображение карточки
    def show_ticket(self, num):
        print('Номер на карточке игрока: ', num)
        print("-"*30)
        for i in range(3):
            for num in self.strings[i]:
                print(num, " ", end=" ")
            print("\n")
        print("-" * 30)

class Gamer:
    def __init__(self):
        self.card = Ticket()

    def is_victory(self):
        for i in range(3):
            if self.card.strings[i].count("-") < 5:
                return False
        return True

class Dropout(Gamer):
    def act(self, num):
        pass
class Person(Gamer):
    def act(self, num):
        self.card.show_ticket(num)
        replay = None
        while replay not in ['yes', 'no']:
            replay = input("Зачеркнуть номер? (yes/no) ")
        if replay == "yes":
            if num not in self.card.numbers:
                print("Такого номера  на Вашей карточке нет ! ")
                return False
            else:
                for i in range(3):
                    if num in self.card.strings[i]:
                        self.card.strings[i][self.card.strings[i].index(num)] = '-'
                        self.card.numbers.pop(self.card.numbers.index(num))
                        return True
        else:
            if num in self.card.numbers:
                print("Такой номер  есть на Вашей карточке есть! ")
                return False
            return True
class Computer(Gamer):
    def act(self, num):
        self.card.show_ticket(num)
        if num in self.card.numbers:
            for i in range(3):
                if num in self.card.strings[i]:
                    self.card.strings[i][self.card.strings[i].index(num)] = '-'
                    self.card.numbers.pop(self.card.numbers.index(num))
        return True
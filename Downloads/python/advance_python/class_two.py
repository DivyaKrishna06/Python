class Player:
    membership=True
    def __init__(self,name='anonymus',age=0):
        try:
            if (age>18):
                self.name=name
                self.age=age
        except:
            print('Age error exception')
        
    def shout(self):
        print(f'{self.name} is {self.age} years old')
        return 'done'

name=input('Enter the name: ')
age=int(input('Enter the age: '))
player1=Player(name,age)
player1.shout()
# player2=PlayerCharacter('Hermaini',20,'Magic')
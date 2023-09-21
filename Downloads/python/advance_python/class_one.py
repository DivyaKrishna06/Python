class PlayerCharacter:
    def __init__(self,name,age,weapon):
        self.name=name
        self.age=age
        self.weapon=weapon

    def run(self):
        print(f'{self.name} is running')
        return 'done'
    
player1=PlayerCharacter('HarryPotter',23,'Wand')
player2=PlayerCharacter('Hermaini',20,'Magic')
player1.run()
player2.attack=20

print(f'The player {player2.name} attacked {player2.attack} times')
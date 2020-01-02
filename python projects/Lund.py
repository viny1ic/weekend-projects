class Team:
    def __init__(self):
        self.dict = {}
        self.team1 = input('Enter the name of team 1 :  ')
        self.team2 = input('Enter the name of team 2 :  ')
    def Addplayers(self):
        self.dict = dict.fromkeys([input(f'Enter Team {self.team1} ,  player {i+1}  :  ')for i in range(0,11)], self.team1)
        self.dict.update(dict.fromkeys([input(f'Enter Team {self.team2} ,  player {i+1}  :  ')for i in range(0,11)], self.team2))
    def Showplayers(self):
        return self.dict 

p1 = Team()
p1.Addplayers()
print(p1.Showplayers())
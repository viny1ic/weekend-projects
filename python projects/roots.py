team1,team2 = input('Enter team1 and team2 comma seperated :  ')
dict1 = dict.fromkeys([input(f'Enter Team {team1} ,  player {i+1}  :  ') for i in range(0,11)],team1)))
dict1.update(dict.fromkeys([input(f'Enter Team {self.team2} ,  player {i+1}  :  ')for i in range(0,11)],team2))
print(dict1)

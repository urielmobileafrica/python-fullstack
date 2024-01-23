#updating constructor to accept infomation rather than individual attributes
class Player:
    cls_players = []
    max_index = 0
    @classmethod
    def get_team(cls, team_list):
        cls.team_list = team_list
        cls.max_index = len(team_list) - 1
        i = 0
        while i <= cls.max_index:
            cls.cls_players.append(team_list[i])
            print(cls.cls_players[i])
            i += 1
        return cls
        


    def __init__(self, player):
        #self.name = name
        #self.age = age
        #self.position = position
        #self.team = team
        self.player = player
        

#creating instanes using the following dictionarires

kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}

player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

#create a new list with Player Instances from the list of Players

#My List of Dictionaries
players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]

player_max_index = len(players) - 1
#This is a list of all "players"
player_n = []
new_team = []
#create new player instances
i = 0
while i <= player_max_index:
    # creating new player instances as a list of instances
    player_n.append(Player(players[i]))
    # on creation adding that instance list index to a new team by appending to an initially empty "team list"
    new_team.append(player_n[i])
    i += 1
i = 0
print(new_team)
#print(f'player_n has {len(player_n)} Instances')

#Using get_team to return a list of player objects given a list of disctionarie
Player.get_team(players)

print("done")










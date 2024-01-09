class User:
    
    def __init__(self, first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        #default attributes
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        for attrib, value in self.__dict__.items():
            print(f'{attrib}: {value}')
        print('---------------------')
        pass

    def enroll(self):
        if (self.is_rewards_member == False):
            self.is_rewards_member=True
            self.gold_card_points=200
        pass

    def spend_points(self,amount):
        if (self.gold_card_points < amount):
            if (self.gold_card_points == 0):
                print(f'{self.first_name} has no points to spend!')
            elif(self.gold_card_points > 0):
                print(f'{self.first_name} only has {self.gold_card_points} points to spend')
                #print(f'Using all {self.gold_card_points} points NOW...')
                print('-----------------------')
                #Use all available Points
                #self.gold_card_points -= self.gold_card_points
        else:
            self.gold_card_points -= amount

        return self.gold_card_points
        pass


user_john=User('John','Doe','john@doe.com',25)
user_john.display_info()
user_john.enroll()


user_jane=User('Jane','Doe','jane@doe.com',27)
user_gene=User('Gene','Doe','gene@doe.com',23)



user_john.spend_points(50)#spend 50 points as John
user_jane.enroll()
user_jane.spend_points(80)


user_john.display_info()
user_jane.display_info()
user_gene.display_info()

user_john.enroll()
user_john.display_info()

#implementing and testing ovespend logic
#user_gene.gold_card_points=30
user_gene.display_info()
user_gene.spend_points(40)
user_gene.display_info()


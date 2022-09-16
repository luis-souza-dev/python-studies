class Robot:
    population = 0
    
    def __init__(self, name):
        self.name = name
        print('(Initializing {})'.format(self.name))
        
        
        Robot.population += 1
    
    def die(self):
        print('{} is being destroyed'.format(self.name))
        
        Robot.population -= 1
        
        if (Robot.population == 0):
            print('{} was the last one'.format(self.name))
        else:
            print('There are {} robots remaining'.format(Robot.population))
            
    def say_hi(self):
        print('Greetings I\'m {} the super robot'.format(self.name))
        
    @classmethod
    def how_many(cls):
        print('We have {:d} robots'.format(cls.population))
        
droid1 = Robot('Luis')
droid1.say_hi()
Robot.how_many()

droid2 = Robot('Michele')
droid2.say_hi()
Robot.how_many()

print('\n Robots working here\n')

print('Robots finished working, disposing of them.')
droid1.die()
Robot.how_many()
droid2.die()
Robot.how_many()
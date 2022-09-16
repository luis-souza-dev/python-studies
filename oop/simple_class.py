class Person:
    def __init__(self,name):
        self.name = name
    def say_hello(self):
        print('Hello {}, how are you?'.format(self.name))
        
p = Person('Luis')
p.say_hello()
def say_hello():
    print('Hello there!')
    
say_hello()
say_hello()


# functions with params
def say_hello_to_user(userName):
    print('Hello there, ',userName)
    
say_hello_to_user('Luis')
    
    
# function with keyword argument
def say_user_name_age(userName, userAge):
    print('Hello there', userName)
    print('You are {} year old!'.format(userAge))
    
say_user_name_age(userAge=23,userName='Luis')


#function with variable number of arguments
def total(a=5, *numbers, **phonebook):
    print('a',a)
    
    for single_item in numbers:
        print('single_item', single_item)
    
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)
        
total(10,1,2,3,4,5,6,Jack=123, L=23, fsdfsdfsdf= 32)
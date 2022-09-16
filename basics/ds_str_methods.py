name = 'Luis'

if name.startswith('Lu'):
    print('Yes the name starts with Lu')
if 'u' in name:
    print('Yes there is a u in the name')
if name.find('is') != -1:
    print('Yes it contains the string \'is\'')

delimiter = '_*_'
myList = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(myList))
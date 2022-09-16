print('Simple assignment')
shopList = ['apple', 'egg', 'cucumber', 'beer']

# myList is just another name poiting to the same object!
myList = shopList

del shopList[0]

print('shopList is ', shopList)
print('myList is ', myList)

print('Copy making a full slice')

myList = shopList[:]

del myList[0]

print('shopLIst', shopList)
print('myList', myList)
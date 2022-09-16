shopList = ['apples', 'bananas', 'oranges', 'egg']

print('I have ', len(shopList), ' items in my shoplist')

print('these items are:', end=' ')
for item in shopList:
    print(item,end=' ')
    
print('\ni also need to buy rice')
shopList.append('rice')

print('my shoplist is now', shopList)

print('Sorting shop list')
shopList.sort()
print('Sorted shopping list', shopList)

print('The first item i\'ll buy will be', shopList[0])
oldItem = shopList[0]
del shopList[0]
print('I bought the first item', oldItem)
print('Updated shoppping list', shopList)
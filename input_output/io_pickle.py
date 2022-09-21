import pickle

shoplistfile = 'shoplist.data'

shoplist = ['apple', 'cheese', 'bread', 'peanut butter']

# Write to the file
f = open(shoplistfile,'wb')

# Dump the object to the file
pickle.dump(shoplist,f)
f.close()

# Delete the shoplist variable
del shoplist

# Read back from the storage
f = open(shoplistfile, 'rb')
# Load the object from the file
storedList = pickle.load(f)
print(storedList)
f.close()
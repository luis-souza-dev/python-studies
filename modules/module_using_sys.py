import sys
import module_using_name

print('The command line arguments are: ')
for i in sys.argv:
    print(i)

print('\n\nThe python path is', sys.path, '\n')
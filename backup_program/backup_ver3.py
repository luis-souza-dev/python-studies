import os
import time

source = ['/home/luis/Desktop/backup_test']

target_dir = '/home/luis/Desktop/backup_destination'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    
today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = input('Enter a comment ---> ')

if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ','_') + '.zip'
    
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created the directory ', today)
    
zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(source))

print('Zip command is: ')
print(zip_command)
print('Running')
if os.system(zip_command) == 0:
    print('Backup was successfull')
else:
    print('Backiup failed')
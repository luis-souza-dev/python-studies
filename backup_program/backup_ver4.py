import os, time,zipfile



source = ['/home/luis/Desktop/backup_test']

target_dir = '/home/luis/Desktop/backup_destination'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')


comment = input('Enter a comment --> ')

if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'
        
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)
    
zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(source))

print('Zip command is:')
print(zip_command)
print('Running:')

with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(source[0]):
        print('root', root)
        print('dirs', dirs)
        print('files', files)
        for file in files:
            zipf.write(os.path.join(root, file), 
                        os.path.relpath(os.path.join(root, file), 
                                        os.path.join(source[0], '..')))



print('Successful backup to', target)
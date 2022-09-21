import sys, time

f = None

try:
    f = open('poem.txt')
    # Our visual file-reading idiom
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()
        print('Press ctrl + c now')
        # To make sure it runs for a while
        time.sleep(2)
except IOError:
    print('Could not find the file poem.txt')
except KeyboardInterrupt:
    print('You cancelled the operation.')
finally:
    if f:
        f.close()
        print('(Cleaning up: closed the file)')
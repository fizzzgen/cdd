import os
import sys

PATH_HISTORY = '/Users/fizzzgen/.cd/history.txt'
find_path = sys.argv[1]
with open('cd.txt', 'w') as f:
    f.write(find_path)

current_path = os.path.abspath(os.getcwd())
if os.path.exists(os.path.join(current_path, find_path)):
    print(os.path.join(current_path, find_path))
else:
    with open(PATH_HISTORY, 'r') as f:
        paths = list(f.read().split('\n'))[:-1]
        paths.reverse()
    for item in paths:
        if item.endswith('/') and find_path in item:
            print item
            break
        elif item.endswith(find_path):
            print item
            break
    print(find_path)

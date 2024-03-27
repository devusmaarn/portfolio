import os
import time

while True:
    print('adding changes to commit....')
    os.system('git add .')

    message = input('enter commit message: ')
    print('commiting changes....')
    os.system(f'git commit -m "{message}"')

    print('pushing changes to remote ...')
    os.system('git push')
    print("new changes pushed.")

    time.sleep(10)
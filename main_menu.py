from colorama import init
from termcolor import colored
import time
import playmaths

#fcn for timedelay messages
def time_msg(s,clr='cyan'):
    for i in s:
        print(colored(i,clr),end='',flush=True)
        time.sleep(0.01)

init()
 
print(colored(
    
''' 
                                  ██████    █████  █████ █████ ███████████    █████   ███   █████ █████ ███████████   █████████   ███████████   ██████████  
                                ███░░░░███ ░░███  ░░███ ░░███ ░█░░░░░░███    ░░███   ░███  ░░███ ░░███ ░█░░░░░░███   ███░░░░░███ ░░███░░░░░███ ░░███░░░░███ 
                               ███    ░░███ ░███   ░███  ░███ ░     ███░      ░███   ░███   ░███  ░███ ░     ███░   ░███    ░███  ░███    ░███  ░███   ░░███
                              ░███     ░███ ░███   ░███  ░███      ███        ░███   ░███   ░███  ░███      ███     ░███████████  ░██████████   ░███    ░███
                              ░███   ██░███ ░███   ░███  ░███     ███         ░░███  █████  ███   ░███     ███      ░███░░░░░███  ░███░░░░░███  ░███    ░███
                              ░░███ ░░████  ░███   ░███  ░███   ████     █     ░░░█████░█████░    ░███   ████     █ ░███    ░███  ░███    ░███  ░███    ███ 
                               ░░░██████░██ ░░████████   █████ ███████████       ░░███ ░░███      █████ ███████████ █████   █████ █████   █████ ██████████  
                                 ░░░░░░ ░░   ░░░░░░░░   ░░░░░ ░░░░░░░░░░░         ░░░   ░░░      ░░░░░ ░░░░░░░░░░░ ░░░░░   ░░░░░ ░░░░░   ░░░░░ ░░░░░░░░░░   
              ''', 'green'))

time_msg(''' 
Welcome users, this is a python program that lets  you create and play Quizzes
Press[1] for creating a quiz                     Press[2] for attending a quiz                   
''')
print()
g = int(input(''))


if g==2:
    print()
    time_msg('Enter the subject:    [0] Maths          [1] Physics          [2] 2Chemistry')
    print()

    sub=int(input(''))
    print()
    if sub==0:
        quiz=playmaths.get_quiz()

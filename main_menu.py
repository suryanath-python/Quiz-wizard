from colorama import init
from termcolor import colored
import time
import playmaths
import scores
init()

global g
#fcn for timedelay messages
def time_msg(s,clr='cyan'):
    for i in s:
        print(colored(i,clr),end='',flush=True)
        time.sleep(0.01)
    return ' '

 
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


name=input(time_msg('Enter your name :'))

time_msg(''' 
Welcome users, this is a python program that lets  you create and play Quizzes
Press[1] for attending a quiz                     Press[2] Scoreboard                   
''')
print()
g = int(input(''))


if g==1:
    time_msg('''
  For every correct answer you will be awarded +1 mark
  For every wrong answers -1 will be deducted

    ''')
    print()
    time_msg('Enter the subject:    [0] Maths          [1] Physics          [2] Chemistry')
    print()

    sub=int(input(''))
    print()
    if sub==0:
        score=playmaths.play_quiz()

    scores.enter_name(name,score)

if g==2:
    scores.show()

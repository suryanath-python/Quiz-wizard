from colorama import init
from mysql import connector as msql
from termcolor import colored
import time

init()

def time_msg(s,clr='cyan'):
    for i in s:
        print(colored(i,clr),end='',flush=True)
        time.sleep(0.01)

    return ''    

def tabulize(record, clr='light_cyan'): #To tabulize and make data segsy
    l=[]
    for i in record:
        l.append(i[0])    

    s=len(l)
    lines=s*16

    print(colored('+'+'-'*lines+'+',clr))
    for i in range(s):
        print(colored('|'+ str(i).center(15),clr),end='')
    print(colored('|',clr))

    print(colored('+'+'-'*lines+'+',clr))

    for i in range(s):
        p=l[i].capitalize()
        print(colored('|'+ p.center(15),clr),end='')
    print(colored('|',clr))    

    print(colored('+'+'-'*lines+'+',clr))

def get_quiz():          #To display all the tables in the database and also gets the question to answer
    con = msql.connect(
    host="localhost",
    user="root",
    password="surya@2006",
    database="maths"
    )
    cursor=con.cursor()
    cursor.execute('SHOW TABLES')
    records=cursor.fetchall()

    tabulize(records,'magenta')        

    print()
    p=int(input(colored("Enter the quiz_id of the quiz you want to answer: ",'magenta')))

    cursor.close()
    con.close()    
    return p

def convert_sql_list(record):
    l=[]
    for i in record:
        l.append(i[0])

    return l
   

def play_quiz():
    score=0
    con = msql.connect(
    host="localhost",
    user="root",
    password="surya@2006",
    database="maths"
    )
    cursor=con.cursor()
    cursor.execute('SHOW TABLES')
    record=cursor.fetchall()
    
    l=convert_sql_list(record)

    g=get_quiz()
    cursor.execute(
      '''SELECT Q_ID 
          FROM {} '''.format(l[g]))

    q_id=cursor.fetchall()
    q_id=convert_sql_list(q_id)

    cursor.execute(
      '''SELECT QUESTIONS 
          FROM {} '''.format(l[g]))    

    questions=cursor.fetchall()
    questions=convert_sql_list(questions)

    cursor.execute(
      '''SELECT A 
          FROM {} '''.format(l[g])) 
    
    option_A=cursor.fetchall()
    option_A=convert_sql_list(option_A)

    cursor.execute(
      '''SELECT B 
          FROM {} '''.format(l[g]))

    option_B=cursor.fetchall()
    option_B=convert_sql_list(option_B)
    
    cursor.execute(
      '''SELECT C 
          FROM {} '''.format(l[g]))
    
    option_C=cursor.fetchall()
    option_C=convert_sql_list(option_C)

    cursor.execute(
      '''SELECT D 
          FROM {} '''.format(l[g]))
    
    option_D=cursor.fetchall()
    option_D=convert_sql_list(option_D)
    
    cursor.execute(
      '''SELECT ANSWER 
          FROM {} '''.format(l[g]))
    
    answer=cursor.fetchall()
    answer=convert_sql_list(answer)

    cursor.close()
    con.close()

    # print(q_id)
    # print(questions)
    # print(option_A)
    # print(option_B)
    # print(option_C)
    # print(option_D)
    #print(answer[1])
    print()
    useless=input(time_msg('Press any key when you are ready: '))
    print()

    for i in range(len(q_id)):
      s1='\033[1m({})'.format(q_id[i]), '\033[1m{}'.format(questions[i])
      s2='(A) {}'.format(option_A[i]), ' (B) {}'.format(option_B[i]),' (C) {}'.format(option_C[i]),' (D) {}'.format(option_D[i])
      
    
      time_msg(s1,'blue')
      print()
      time_msg(s2,'blue')
      ans=input(' ')

      if ans == answer[i]:
        time_msg("Your answer was right", 'green')
        score+=1
      
      else:
        time_msg("Your answer was wrong", 'red')
        score-=1
      print('\n')
      
    print('\n')  
    time_msg('Your score is: '+str(score), 'green')
    
      
    return score


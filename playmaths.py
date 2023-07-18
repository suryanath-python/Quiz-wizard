from mysql import connector as msql
from termcolor import colored

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

  tabulize(records,'red')        

  print()
  p=int(input(colored("Enter the quiz_id of the quiz you want to answer: ",'magenta')))

  cursor.close()
  con.close()    
  return p

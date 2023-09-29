from mysql import connector as msql
from termcolor import colored

def tabulize_scores(record, clr='light_cyan'): #To tabulize and make data segsy
    record.sort(key=lambda x:x[1],reverse=True)
    l=[]
    l1=[]
    for i in record:
        l.append(i[0])  
    for i in record:
        l1.append(i[1])


    s=len(l)
    lines=4*8

    print(colored('+'+'-'*lines+'+',clr))
    print(colored('\033[1m           HIGH SCORES !!\033[0m','magenta'))
    print(colored('+'+'-'*lines+'+',clr))
    for i in range(s):
        p=l[i].capitalize()
        q=str(l1[i])
        print(colored('|'+ str(i+1).center(5)+'|'+ p.center(15)+'|'+q.center(10)+'|',clr))
        print(colored('+'+'-'*lines+'+',clr))

def show():
    con = msql.connect(
    host="localhost",
    user="root",
    password="surya@2006",
    database="score"
    )

    cursor=con.cursor()
    cursor.execute('SELECT * FROM SCORES;')
    records=cursor.fetchall()
    tabulize_scores(records)
    cursor.close()
    con.close()

def enter_name(name,score):
    con = msql.connect(
    host="localhost",
    user="root",
    password="surya@2006",
    database="score"
    )
    
    names=[]

    cursor=con.cursor()
    cursor.execute('SELECT * FROM SCORES;')
    records=cursor.fetchall()
    # print(records)    

    for i in records:
        names.append(i[0])

    # print(names)



    if name not in names:
        cursor.execute(
        '''INSERT INTO SCORES 
        VALUES ('{}',{});'''.format(name,score)
        )
        
    con.commit()
    cursor.close()
    con.close()


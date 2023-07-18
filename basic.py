import mysql.connector as msql

con = msql.connect(
    host = "localhost",
    user = "root",
    passwd = "admin",
    database = "test"
)
print(con.is_connected())
cur = con.cursor()

#Creates quiz tables
def create_quiz():
    qname = input("Enter quiz name: ")

    create = "CREATE TABLE "+qname+"\
    (Q_ID INT NOT NULL AUTO_INCREMENT,\
    Questions VARCHAR(50),\
    A VARCHAR(25),\
    B VARCHAR(25),\
    C VARCHAR(25),\
    D VARCHAR(25),\
    Answer CHAR(1),\
    PRIMARY KEY(Q_ID))"
    
    cur.execute(create)
    print("quiz created successfully.")
    con.commit()

#Add questions to an existing quiz table
def add_questions():
    qname = input("Enter name of an existing quiz: ")

    q = input("Enter the question: ")
    a = input("Enter Option A: ")
    b = input("Enter Option B: ")
    c = input("Enter Option C: ")
    d = input("Enter Option D: ")
    ans = input("Set the correct answer(A/B/C/D): ") 

    add = "INSERT INTO "+qname+"\
        (Questions,A,B,C,D,Answer)\
        VALUES('{}','{}','{}','{}','{}','{}')\
        ".format(q,a,b,c,d,ans)

    cur.execute(add)
    print("Question added successfully.")
    con.commit()

#Delete an existing quiz
def delete_quiz():
    qname = input("Enter name of an existing quiz: ")

    drop = "DROP TABLE "+qname+""

    cur.execute(drop)
    print("quiz deleted successfully.")
    con.commit()

#Delete a question from an existing quiz
def delete_questions():
    qname = input("Enter name of an existing quiz: ")
    q_id = input("Enter id of question you want to delete: ")

    delete = "DELETE FROM "+qname+" WHERE Q_ID = {}".format(q_id) 

    cur.execute(delete)
    print("question deleted successfully.")
    con.commit()

c = int(input("MENU:\n1)Create a quiz\n2)Add questions to existing quiz\n3)Delete a quiz\n4)Delete questions from an existing quiz\nChoose option: "))   

if c == 1: 
    create_quiz()
if c == 2:
    add_questions()
if c == 3:
    delete_quiz()
if c == 4:
    delete_questions()

con.close()

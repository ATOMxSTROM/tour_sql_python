import mysql.connector
from pyfiglet import Figlet
from tabulate import tabulate

mydb=mysql.connector.connect(host="localhost",user="root",passwd="29@2004@sriram")
c=mydb.cursor()
c.execute('drop database if exists tournament')
def fun():
    c.execute("CREATE DATABASE IF NOT EXISTS tournament")
    c.execute('use tournament')

    c.execute('create table if not exists tour(S_NO int primary key,\
              team_name varchar(30),\
              represented_school varchar(30),\
              location varchar(20),\
              player_1 varchar(20),\
              player_2 varchar(20),\
              player_3 varchar(20),\
              player_4 varchar(20),\
              player_5 varchar(20),\
              age varchar(10),\
              score int)')

    c.execute('create table if not exists duplicate(S_NO int primary key,\
    team_name varchar(30),\
    represented_school varchar(30),\
    location varchar(20),\
    player_1 varchar(20),\
    player_2 varchar(20),\
    player_3 varchar(20),\
    player_4 varchar(20),\
    player_5 varchar(20),\
    age varchar(10),\
    score int)')

def start():

    c.execute('use tournament')
    m=input('''enter 'm' if you want to access management part
enter 'v' if you want to access viewer mode : ''')
    print('')
    if m.lower()=='m':
        pw=input('enter the password to confrim that you are from managent : ')
        print('')
        if pw=='123':
            n=int(input('enter the number of teams participating : '))
            print('')
            list1=[]

            for i in range(1,n+1):
                team=input('enter the team name : ')
                represented_school=input('enter the school name which the team is representing : ')
                location=input('enter the location of the school : ')
                player_1=input('enter the player 1 name : ')
                player_2=input('enter the player 2 name : ')
                player_3=input('enter the player 3 name : ')
                player_4=input('enter the player 4 name : ')
                player_5=input('enter the player 5 name : ')
                age=input('enter the age category of the team : ')
                score_val=int(input('enter the score of each teams : '))
                print('')
                c.execute("insert into tour values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(i,team,represented_school,location,player_1,player_2,player_3,player_4,player_5,age,score_val))

            mydb.commit()
            def fun():
                s=int(input('''enter 1 for displaying the content
enter 2 for altering the table
enter 3 to update the values in table
enter 4 to delete the row in the table : '''))
                if s==1:
                    c.execute('select*from tour')
                    for i in c:
                            print(i)
                elif s==2:

                    n2=input("enter in which attribute , the change need to be done:\nteam_name\nrepresented_school\nlocation : ")

                    if n2=='team_name':

                        q=int(input("enter 1 to increase the range\nenter 2 to change the name of the table : "))

                        if q==1:
                            c.execute('alter table tour modify team_name varchar(40)')

                        elif q==2:
                            nf=input('enter the new name of the table : ')

                            print('nf in q2 of team name : ')

                            c.execute(f'alter table tour rename column team_name to {nf}')

                            print('comment executed on team')


                    elif n2=='represented_school':
                        q=int(input('enter 1 to increase the range\nenter 2 to change the name of the table : '))

                        if q==1:
                            c.execute('alter table tour modify represented_school varchar(40)')

                        elif q==2:
                            nf=input('enter the new name of the table : ')
                            c.execute(f'alter table tour rename column "represented_school" to {nf}')

                    elif n2=='location':
                        print('entered the location : ')

                        q=int(input('enter 1 to increase the range\nenter 2 to change the name of the table : '))

                        if q==1:
                            c.execute('alter table tour modify team_name varchar(30)')


                        elif q==2:
                            nf=input('enter the new name of the table : ')
                            c.execute(f'alter table tour rename column "location" to {nf}')

                elif s==3:
                    Recid = int(input("Enter the Record's S_No : "))
                    colname = input('''enter the column name , in which the updade need to be done :
column name:player_1
            player_2
            player_3
            player_4
            player_5 : ''')

                    dict = {"player1" : ("player_1" ,"1" ,"player 1" ,"pla 1") ,
                     "player2" :("player_2","2" ,"player 2" ,"pla 2") ,
                     'player3' : ('player_3','3','player 3','pla 3') ,
                      "player4" :("player_4" ,"4" ,"player 4" ,"pla 4") ,
                      'player5' : ('player_5','5','player 5','pla 5'),
                      'score_val':('score','val','scr')}

                    for i in list(dict.values()) :
                        if colname in i:
                            change = input('Enter the value to be changed : ')
                            c.execute("update tour set " + i[0] + " = %s where S_NO = %s" ,(change ,Recid))

                            break

                elif  s==4:
                    deleted_row=int(input('enter the row number to delete the team from the list : '))


                    c.execute("delete from tour where S_NO= '{}'".format(deleted_row))


                    print('job done')

                else:
                    print('the enterd value is wrong!Please check the value you have entered')
            fun()
    elif m.lower()=='v':
        def viewer():
            c.execute('use tournament')
            c.execute('select*from tour')
            for i in c:
                print(i)

    else:
        print("not a valid value , please check the variable you have entered")
        v=input('press yes if you want to continue : ')
        if v.lower()=='yes' or v.lower()=='y':
            start()
    mydb.commit()

    while True:
        w=input('enter "yes" or "y" to continue to managent or press "no" or "n" to pass to next : ')
        if w.lower() in 'yes':
            fun()
        else:
            print('you will be in next phase')
            break
    p=input('enter "v" to get into viewer mode or "n" to get to next phase : ')
    if p=='v':
        viewer()
def managment():

    c.execute('select max(score) from tour')


    for i in c:
        print('the maximum score is : ',i[0])

    mydb.commit()

fun()
start()
managment()
l=input('enter "yes" if you want to view main table : ')
print('')
if l.lower()=='yes' or l.lower()=='y':
    c.execute('select*from tour')
    for i in c:
        print(i)
    print('')
    c.execute('select*from duplicate')
    for i in c:
        print(i)
    print('')
l=input('enter "completed" or "comp" to delete the tables in the database : ')
if l.lower() in 'completed':
    c.execute('delete from tour')
    c.execute('delete from duplicate')
mydb.commit()

figlet=Figlet(font='slant')
print(figlet.renderText('THANKS  FOR  JOINING  THE  TOURNAMENT '))

import mysql.connector
from pyfiglet import Figlet
mydb=mysql.connector.connect(host="localhost",user="root",passwd="29@2004@sriram")
c=mydb.cursor()
def fun():
    c.execute("CREATE DATABASE IF NOT EXISTS tournament")
    c.execute('use tournament')

    c.execute('create table if not exists tour(S_NO int primary key,\
              team_name varchar(10),\
              represented_school varchar(20),\
              location varchar(20),player_1 varchar(20),player_2 varchar(20),player_3 varchar(20),player_4 varchar(20),player_5 varchar(20),age varchar(10))')

    c.execute('create table if not exists duplicate(S_NO int primary key,team_name varchar(10),represented_school varchar(20),location varchar(20),player_1 varchar(20),player_2 varchar(20),player_3 varchar(20),player_4 varchar(20),player_5 varchar(20),age varchar(10))')
    c.close()
def start():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="29@2004@sriram")
    c=mydb.cursor()
    c.execute('use tournament')
    m=input('''enter 'm' if you want to access management part
enter 'v' if you want to access viewer mode''')
    if m.lower()=='m':
        pw=input('enter the password to confrim that you are from managent')
        if pw=='123':
            n=int(input('enter the number of teams participating'))
            #list to be inserted
            list1=[]
            #add="insert into tour(S_NO,team_name,represented_school,location,player_1,player_2,player_3,player_4,player_5,age) values(%s)"
            for i in range(n):
                team=input('enter the team name')
                represented_school=input('enter the school name which the team is representing')
                location=input('enter the location of the school')
                player_1=input('enter the player 1 name ')
                player_2=input('enter the player 2 name')
                player_3=input('enter the player 3 name')
                player_4=input('enter the player 4 name')
                player_5=input('enter the player 5 name')
                age=input('enter the age category of the team')
                c.execute("insert into tour values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(i,team,represented_school,location,player_1,player_2,player_3,player_4,player_5,age))
                #t7= [i,team,represented_school,location,player_1,player_2,player_3,player_4,player_5,age]
                #list1.insert(i,t7)

            #c.execute(add,list1)
                #duplicate
            #c.execute(add,list1)
            mydb.commit()
            s=int(input('''enter 1 for displaying the content
enter 2 for altering the table
enter 3 to update the values in table
enter 4 to delete the row in the table
enter 5 to see the structure of the table'''))
            print(s)
            if s==1:
                c.execute('select*from tour')
                for i in c:
                        print(i)
            if s==2:
                #print("i am inside s2")
                n2=input("enter in which attribute , the change need to be done:\nteam_name\nrepresented_school\nlocation")

                if n2=='team_name':

                    q=int(input("enter 1 to increase the range\nenter 2 to change the name of the table"))

                    if q==1:
                        c.execute('alter table tour modify team_name varchar(20)')
                        c.execute('alter table duplicate modify team_name varchar(20)')
                    elif q==2:
                        nf=input('enter the new name of the table')

                        print('nf in q2 of team name')

                        c.execute(f'alter table tour rename column team_name to {nf}')
                        c.execute(f'alter table duplicate rename column team_name to {nf}')

                        print('comment executed on team')
                    print("n2:" ,n2)

                elif n2=='represented_school':
                    q=int(input('enter 1 to increase the range\nenter 2 to change the name of the table'))
                    print('get int')
                    if q==1:
                        c.execute('alter table tour modify represented_school varchar(30)')

                        c.execute('alter table duplicate modify represented_school varchar(30)')

                        print('q is equal to 1  in  represented_school')
                    elif q==2:
                        nf=input('enter the new name of the table')

                        print('q is equal to 2 in represented_school')

                        c.execute(f'alter table tour rename column "represented_school" to {nf}')
                        c.execute(f'alter table duplicate rename column "represented_school" to {nf}')

                        print('comment done in represented_school')
                elif n2=='location':
                    print('entered the location')

                    q=int(input('enter 1 to increase the range\nenter 2 to change the name of the table'))

                    if q==1:
                        c.execute('alter table tour modify team_name varchar(30)')
                        c.execute('alter table duplicate modify team_name varchar(30)')

                        print('the has be altered in location')
                    elif q==2:
                        nf=input('enter the new name of the table')
                        c.execute(f'alter table tour rename column "location" to {nf}')
                        c.execute(f'alter table duplicate rename column "location" to {nf}')

            if s==3:
                Recid = int(input("Enter the Record's S_No: "))
                colname = input('''enter the column name , in which the updade need to be done :
                            column name:player_1
                                        player_2
                                        player_3
                                        player_4
                                        player_5
                                        ''')

                dict = {"player1" : ("player_1" ,"1" ,"player 1" ,"pla 1") ,
                 "player2" :("player_2","2" ,"player 2" ,"pla 2") ,
                 'player3' : ('player_3','3','player 3','pla 3') ,
                  "player4" :("player_4" ,"4" ,"player 4" ,"pla 4") ,
                  'player5' : ('player_5','5','player 5','pla 5')}

                for i in list(dict.values()) :
                    if colname in i:
                        change = input('Enter the name to be changed ')
                        c.execute("update tour set " + i[0] + " = %s where S_NO = %s" ,(change ,Recid))
                        c.execute("update duplicate set " + i[0] + " = %s where S_NO = %s" ,(change ,Recid))

                        print('job done')
                        break

            if  s==4:
                n0=int(input('enter the row number to delete the team from the list'))
                c.execute('delete from tour where S.NO==n0')

            #duplicate db
                n0=int(input('enter the row number to delete the team from the list'))
                c.execute('delete from duplicate where S.NO==n0')
            if s==5:
                print(c.execute('desc tour'))
            c.close()


    elif m.lower()=='v':
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="29@2004@sriram")
        c=mydb.cursor()
        c.execute('use tournament')
        c.execute('select*from tour')
        for i in c:
            print(i)
    else:
        print("not a valid value , please check the variable you have entered")
        v=input('press yes if you want to continue')
        if v.lower()=='yes' or v.lower()=='y':
            start()
    mydb.commit()
    c.close()
def managment():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="29@2004@sriram")
    c=mydb.cursor()
    c.execute('use tournament')
    c.execute('select*from tour')
    y=c.fetchall()
    r=c.rowcount()
    m=r%2
    while m==0:
        if m%2==0:
            f=int(input('enter the first team'))
            f1=int(input('enter the second team'))
            print('Team 1 going to participate',f)
            print('Team 2 going ot participate',f1)
            k=int(input('winning team'))
            k1=int(input('losing team'))
            c.excute('delete from duplicate where S.NO==k1')
            m=m%2
        else:
            f=int(input('enter the first team'))
            f1=int(input('enter the second team'))
            f3=int(input('enter the thrid team'))
            print('Team 1',f,'vs Team 2',f1)
            k=int(input('winning team'))
            k1=int(input('losing team'))
            c.excute('delete from duplicate where S.NO==k1')
            print('Winning team',k,'vs Team 3',f2)
            k=int(input('winning team in second round'))
            k1=int(input('losing team in second round'))
            c.excute('delete from duplicate where S.NO==k1')
            m=(m%2)-1
    c.execute('select*from duplicate')
    for i in c:
        print(i)
    mydb.commit()
fun()
start()
#managment()
l=input('enter "yes" if you want to view table and the winner team')
if l.lower()=='yes' or l.lower()=='y':
    c.execute('select*from tour')
    for i in c:
        print(i)
    c.execute('select*from duplicate')
    for i in c:
        print(i)
c.execute('drop database tournament')
figlet=Figlet(font='Standard')
print(figlet.renderText('THANKS FOR JOINING THE TOURNAMENT '))

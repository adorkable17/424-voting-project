import mysql.connector
from mysql.connector import errorcode
from mysql.connector import MySQLConnection, Error


def call_winner_count(cnx, cursor,*args):
    cursor.callproc('winner_count')

def call_insert_votes(cnx, cursor, args):
    cursor.callproc('insert_votes', args)

def call_vote_count(cnx, cursor, args):
    cursor.callproc('vote_count', args)
def invalid():
    return "Not a valid function"



#func int to choose the procedure
#1 to get the full tallied list of votes
#2 to check if voter has already voted
#3 to insert a vote

#args is an argument list for each procedure
def databaseAccess(func,args)
    try:
        #user,password,host should change depending on who's hosting the database and the accounts on it
        #no i don't use these credentials for anything else don't even try it
        cnx = mysql.connector.connect(user='av591', password='databases336',
                                host='localhost',
                                    database='voter')
        cursor = cnx.cursor()

        #switch to select function
        functions = {
            1:call_winner_count,
            2:call_vote_count,
            3:call_insert_votes
        }
        
        if(func in functions):
            func = functions[1]
            func(cnx,cursor,args)
        else:
            return invalid()
        

        results = []
        #Return array of results
        for result in cursor.stored_results():
            result.append(result)
        
        return results
        
            
            
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
            
    else:
        cursor.close()
        cnx.close()


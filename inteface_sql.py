import sqlite3
import datetime
import calendar

connection = None
chitRuleTableNumber = 0


def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)


def initDataBase():
    """to initialize data base"""
    retVar = False
    global connection

    try:
        # connecting to the database
        connection = sqlite3.connect("LpChitDb.db")
        retVar = True
    except:
        print("Cannot access database file")
    return retVar


def createRuleTable(chitRuleTableDetail):
    """to create the group table"""
    global connection
    global chitRuleTableNumber

    retVar = False
    # cursor
    crsr = connection.cursor()

    # getting table name
    chitRuleTableName = "LPCHIT_RT" + chitRuleTableDetail.get('groupType')

    # SQL command
    sql_command = "CREATE TABLE " + chitRuleTableName + \
                  "(s_no INTEGER,dueAmount INTEGER, interestAmount INTEGER,DisposeAmount INTEGER);"
    print(sql_command)

    # execute the statement
    crsr.execute(sql_command)

    print(type(chitRuleTableDetail.get('rowCount')))

    for index in range(chitRuleTableDetail.get('rowCount')):
        # SQL command to JRRRTTNTN5HB5BH5BBHB5 the data in the table
        # Sample Command
        # sql_command = "INSERT INTO TableName VALUES (1, 5000, 0, 0,\"NILL\" ,\"2021-08-13\");"
        sql_command = "INSERT INTO " + chitRuleTableName + \
                      " VALUES (" + str(index + 1) + ", " + \
                      str(chitRuleTableDetail.get('dueAmount')[index]) + ", " + \
                      str(chitRuleTableDetail.get('interest')[index]) + ", " + \
                      str(chitRuleTableDetail.get('disposeAmount')[index]) + ");"
        print(sql_command)
        crsr.execute(sql_command)
    # To save the changes in the files. Never skip this.
    # If we skip this, nothing will be saved in the database.
    connection.commit()
    return retVar

def setvendorLotReq(LPCHIT_DTBB1, uname):
    crsr = connection.execute("SELECT * from LPCHIT_DTBB1;")
    #insert = """INSERT INTO chitRuleTableName(vendorLotReq) VALUES (%d);"""
    #print(insert)
    #vendorLotReq = """VALUES=[0,0,0,0,0,0,0,0,0,0];"""
    #print(vendorLotReq)
    sql_command = crsr.execute("SELECT vendorLotReq,uname FROM LPCHIT_DTBB1;")
    print(sql_command)
    sql_command = connection.execute("UPDATE LPCHIT_DTBB1 set vendorLotReq = 1 where uname = 'UID4';")
    rows = crsr.fetchall()
    for row in rows:
        print(row)
    # execute your query
    print(sql_command)
def resetvendorLotReq(LPCHIT_DTBB1 , uname):
    crsr = connection.execute("SELECT * FROM LPCHIT_DTBB1;")
    crsr.execute("SELECT vendorLotReq FROM LPCHIT_DTBB1;")
    sql_command = connection.execute("UPDATE LPCHIT_DTBB1 set vendorLotReq = 0 ;")
    print(sql_command)
'''def UpdateLastColumnInDerivedTable():
    retValue = False
    print('UpdateLastColumnInDerivedTable')
    updatechitRuleDetail = {'TableName': 'LPCHIT_DTBB1','uname':['UID1',"\"NILL\"","\"NILL\"","\"NILL\"","\"NILL\"","\"NILL\"","\"NILL\"","\"NILL\"","\"NILL\"","\"NILL\"","\"NILL\""]}
    # sql_command = "INSERT INTO TableName VALUES (1, 5000, 0, 0,\"NILL\" ,\"2021-08-13\");"
    sql_command = "INSERT INTO " + chitRuleTableName + " VALUES (1, 5000, 0, 0,\"NILL\" ,\"2021-08-13\");"
'''


def getRuleTableAmountDetails(groupType):
    """To get Due and Interest amount from the Rule Table"""
    # cursor
    crsr = connection.cursor()
    # getting table name
    chitRuleTableName = "LPCHIT_RT" + groupType
    sql_command = "SELECT dueAmount, interestAmount FROM "+chitRuleTableName+";"

    crsr.execute(sql_command)
    AmountDetail = crsr.fetchall()
    print(AmountDetail)
    return AmountDetail


def createDeriveVendorTable(chitDerivedTableDetail):
    """used to create Derived Table"""
    global connection
    global chitRuleTableNumber
    monthCat = ''

    retVar = False
    # cursor
    crsr = connection.cursor()

    chitRuleTableNumber = chitRuleTableNumber + 1
    chitRuleTableName = "LPCHIT_DT" + chitDerivedTableDetail.get('groupType') + str(chitRuleTableNumber)
    for index in range(chitDerivedTableDetail.get('monthCount')):
        monthCat = monthCat+"month" + str(index+1) + " DATE,"
    for index in range(10):
        vendorLotReq =0

    # SQL command to create a table in the database
    sql_command = "CREATE TABLE " + chitRuleTableName + \
                  "(sNo INTEGER,uname VARCHAR(30)," + monthCat + \
                  " lotteryDate DATE,dueDate DATE,lastPaidDate DATE" + \
                  "penality INTEGER,totalAmountPaid INTEGER," + \
                  "userLotReq BIT", "vendorLotReq);"
    print(sql_command)
    crsr.execute("SELECT * FROM LPCHIT_DTBB1")

    crsr.execute(sql_command)

    #Getting Amount details from Rule Table
    AmountDetails = getRuleTableAmountDetails(chitDerivedTableDetail.get('groupType'))
    #Convert Date String in to Object
    date_time_obj = datetime.datetime.strptime(chitDerivedTableDetail.get('startDate'), '%Y-%m-%d')


    for index in range(len(AmountDetails)):
        sql_command = "INSERT INTO " + chitRuleTableName + \
                      " (sNo,uname,dueDate) VALUES (" + str(index+1) + ", '" + \
                      chitDerivedTableDetail.get('uname')[index] + "', " + \
                       add_months(date_time_obj, index).strftime('%Y-%m-%d')+");"
        print(sql_command)
        # execute the statement
        crsr.execute(sql_command)

    # To save the changes in the files. Never skip this.
    # If we skip this, nothing will be saved in the database.
    connection.commit()
    return retVar
def closeDataBase():
    # close the connection
    connection.close()


    return


def listAllRuleChitName():
    # connecting to the database
    global connection
    # connection = sqlite3.connect("LpChitDb.db")
    # cursor
    if connection == None:
        initDataBase()
    crsr = connection.cursor()
    # crsr.execute("SELECT name FROM sqlite_master WHERE type='table';") #for example
    crsr.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'LPCHIT_%';")
    print(crsr.fetchall())

def dispTable(tableName):
    # connecting to the database
    global connection
    crsr = connection.cursor()
    sql_command = "SELECT * from "+tableName
    crsr.execute(sql_command)
    print(crsr.fetchall())


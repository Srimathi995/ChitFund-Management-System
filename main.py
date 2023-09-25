import sys
import inteface_sql
import random



def createNewRuleChit():
    """Create New Chit is used to create the Chit table using SQL"""
    print('createNewChit')
    # to Initialize Sql
    inteface_sql.initDataBase()

    chitRuleTableDetail = {'groupType': 'BB', 'rowCount': 10,
                           'dueAmount': [5000, 4000, 4000, 4250, 4250, 4500, 4500, 4800, 4900, 4950],
                           'interest': [0, 1000, 1000, 750, 750, 500, 500, 200, 100, 50],
                           'disposeAmount': [0, 37500, 37500, 40000, 40000, 42500, 42500, 45500, 46500, 47000]}
    inteface_sql.createRuleTable(chitRuleTableDetail)
    inteface_sql.closeDataBase()

def createNewDerivedChit():
    """Derived chit is used to get all the detailed information about the chit"""
    print('createNewChit')
    # to Initialize Sql
    chitDerivedTableDetail = {'groupType': 'BB', 'monthCount': 10,
                              'uname': ['UID1', 'UID2', 'UID3', 'UID4', 'UID5', 'UID6', 'UID7', 'UID8', 'UID9',
                                        'UID10'],
                              'startDate': '2021-08-15'}
    inteface_sql.initDataBase()
    inteface_sql.createDeriveVendorTable(chitDerivedTableDetail)
    inteface_sql.closeDataBase()



def editChit():
    """edit is used to Edit the Chit table using SQL"""
    print('EditChit')


def displayChit():
    """display Chit is used to list the Chit table using SQL"""
    print('displayChit')
    # display LPCHITBB001 table
    inteface_sql.initDataBase()
    inteface_sql.listAllRuleChitName()
    inteface_sql.closeDataBase()


def displayTableContent(tableName):
    "To display table content "
    inteface_sql.initDataBase()
    inteface_sql.dispTable(tableName)
    inteface_sql.closeDataBase()


def pickAllChit():
    """pick a lottery for all the chit"""
    print('pickAllChit')
    inteface_sql.initDataBase()
    inteface_sql.setvendorLotReq("LPCHIT_DTBB1", "uname")
    inteface_sql.resetvendorLotReq("LPCHIT_DTBB1", "uname")
    inteface_sql.closeDataBase()

def pickSpecificChit():
    """pick a lottery for specific chit"""
    print('pickSpecificChit')


    # using list comprehension + randrange()
    # to generate random number list between 1-20
    #res1 = [random.randrange(1,20,1) for i in range(7)]
    res1 = [random.randrange(1,20,1)]

    # printing result
    print("Random number list is : " + str(res1))
    # using list comprehension + randrange()
    # to generate random number list between 1-10
    # initializing list
    test_list = [1, 4, 5, 2, 7]

    # printing original list
    print("Original list is : " + str(test_list))

    # using random.choice() to
    # get a random number
    random_num = random.choice(test_list)

    # printing random number
    print("Random selected number is : " + str(random_num))


def main():
    """Main function"""
    print('main')
    # create while(1) function
    while True:
        print("Enter the below to proceed:")
        print("1. Create base rule chit table")
        print("2. Create derived chit table ")
        print("3. Display all Chit ")
        print("4. Display Specific table content")
        print("5. pick a lot from all the chit")
        print("6. Pick a lot from the specific chit ")
        print("7. Exit program")

        try:
            user_input = int(input())
        except:
            print("please enter integer input")
            continue

        if (user_input >= 1 and user_input <= 6):
            print("User Selected: " + str(user_input))
            if user_input == 1:
                createNewRuleChit()
            elif user_input == 2:
                createNewDerivedChit()
            elif user_input == 3:
                displayChit()
            elif user_input == 4:
                displayTableContent('LPCHIT_DTBB1')
            elif user_input == 5:
                pickAllChit()
            elif user_input == 6:
                pickSpecificChit()
            elif user_input == 7:
                sys.exit()
            else:
                print("Invalid Selection Please try valid Selection")
        else:
            print("Invalid Selection Please try valid Selection")


if __name__ == '__main__':
    main()

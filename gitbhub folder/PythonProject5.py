import sqlite3


def displayTickets(cur):
    sql = "SELECT * FROM tickets"
    cur.execute(sql)
    results = cur.fetchall()

    if results:
        print("%-6s %-15s %-8s %-5s %-7s" % ('TID', 'Posted Speed', 'Mph Over', 'Age', 'Violator Sex'))
        for row in results:
            tid, a_s, p_s, age, sex = row
            a_s = int(a_s)
            p_s = int(p_s)
            over = a_s - p_s
            print('%-6s %-21s %2s %3s %14s' % (tid, p_s, over, age, sex))

        print()
    else:
        print('No Data Found')


def addTicket(cur, con):
    a_s = int(input('What speed were they going: '))
    while True:
        if a_s >= 0:
            break
        else:
            print('Please enter a valid integer.')

    p_s = int(input('What was the posted speed: '))
    while True:
        if p_s >= 0:
            break
        else:
            print('Please enter a valid integer.')
    age = int(input('What age where they: '))
    while True:
        if age >= 0:
            break
        else:
            print('Please enter a valid integer.')
    while True:
        sex = input('What gender where they (Male or Female): ').capitalize()
        if sex == 'Male':
            break
        elif sex == 'Female':
            break
        else:
            print('''
Please enter Male or Female.
            ''')

    data = (None, a_s, p_s, age, sex)
    sql = "INSERT INTO tickets VALUES (?, ?, ?, ?, ?)"

    cur.execute(sql, data)
    print('''
record has been added
    ''')
    con.commit()


def filterBySex(cur):
    while True:
        opt = input('Which sex(Male or Female): ').capitalize()
        if opt == 'Male' or opt == 'Female':
            break
        else:
            print('''
please enter Male or Female.
            ''')

    try:
        sql = "SELECT * FROM tickets WHERE violator_sex = ?"
        cur.execute(sql, (opt,))
        results = cur.fetchall()
        if results:
            print("%-6s %-15s %-8s %-5s %-7s" % ('TID', 'Posted Speed', 'Mph Over', 'Age', 'Violator Sex'))
            for row in results:
                tid, a_s, p_s, age, sex = row
                a_s = int(a_s)
                p_s = int(p_s)
                over = a_s - p_s
                print('%-6s %-21s %-2s %3s %14s' % (tid, p_s, over, age, sex))

            print()
    except sqlite3.Error as error:
        print(str(error), 'Error occurred')
        print("No data found.")


def main():
    con = sqlite3.connect('tickets5.db')
    cur = con.cursor()

    while True:

        print('''
Menu Options:
    1: Display data
    2: Add
    3: Filter by Sex
    4: Save and Exit
        ''')
        opt = input('''
Enter your choice: ''')
        if opt == '1':
            displayTickets(cur)
        elif opt == '2':
            addTicket(cur, con)
        elif opt == '3':
            filterBySex(cur)
        elif opt == '4':
            con.close()
            print('Data saved.')
            print('Goodbye.')
            break
        else:
            print('''
please enter a valid option. 1, 2, 3, or 4.
            ''')


main()

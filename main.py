import os




def cls():
    os.system('clear')
    print('------------------ Orangery Database ------------------')

#ALL, N, N-LAST
def show_rec():
    cls()
    answer = input('\n Show all records - <a>\n Show 1 record by using id - <i>\n Show n-last records - <n>\n\n - ')
    if answer == 'a':
        showall()
    elif answer == 'i':
        show_id()
    elif answer == 'n':
        show_n()
    else:
        cls()
        runmain()
    
#WHERE plant_id = id
def show_id():
    cls()
    id = input('\nEnter the record id: ')
    print('showing ... \n')
    os.system(f'''ssh -i key.pem ubuntu@18.196.165.162 "python3 /home/ubuntu/orangery/get_1record.py {id}"''')
    answer = input('continue? <y / no - any key>  ')
    if answer == 'y':
        cls()
        runmain()
    
#N - last
def show_n():
    cls()
    n = input('\nEnter n-last records you want to get: ')
    print('showing ...')
    os.system(f'''ssh -i key.pem ubuntu@18.196.165.162 "python3 /home/ubuntu/orangery/get_n_last_records.py {n}"''')
    answer = input('continue? <y / no - any key>  ')
    if answer == 'y':
        cls()
        runmain()


#SELECT * FROM plamts;
def showall():
    cls()
    print('\nDatabase output * * * ...\n')
    os.system("ssh -i key.pem ubuntu@18.196.165.162 'python3 /home/ubuntu/orangery/get_all.py'")
    answer = input('continue? <y / no - any key>  ')
    if answer == 'y':
        cls()
        runmain()

#UPDATE & INSERT
def changging():
    cls()
    answer = input('\n Edit record - <e>\n Create a new one - <c>\n\n - ')
    if answer == 'e':
        editing()
    elif answer == 'c':
        creating()
    else:
        cls()
        runmain()

#UPDATE
def editing():
    cls()
    id = input('Enter the record ID which you want to edit: ')
    name = input('Enter a new record name: ')
    desc = input('Enter a new decription: ')
    number = input('Enter a new number of items: ')
    price = input('Enter a new price for one item: ')
    rare = input('Is the new item rare ? <Y/N> : ')
    print('Editing ...')
    os.system(f'''ssh -i key.pem ubuntu@18.196.165.162 "python3 /home/ubuntu/orangery/edit.py {id} {name} {desc} {number} {price} {rare}"''')
    answer = input('continue? <y / no - any key>  ')
    if answer == 'y':
        cls()
        runmain()


#INSERT
def creating():
    cls()
    name = input('Enter a record name: ')
    desc = input('Enter a decription: ')
    number = input('Enter the number of items: ')
    price = input('Enter the price for one item: ')
    rare = input('Is the item rare ? <Y/N> : ')
    print('Creating ...')
    os.system(f'''ssh -i key.pem ubuntu@18.196.165.162 "python3 /home/ubuntu/orangery/create.py {name} {desc} {number} {price} {rare}"''')
    answer = input('continue? <y / no - any key>  ')
    if answer == 'y':
        cls()
        runmain()

#DELETE
def deleting():
    cls()
    id = input('\nEnter the record id which you want to delete: ')
    print('Deleting  ... \n')
    os.system(f'''ssh -i key.pem ubuntu@18.196.165.162 "python3 /home/ubuntu/orangery/delete.py {id}"''')
    answer = input('continue? <y / no - any key>  ')
    if answer == 'y':
        cls()
        runmain()


#Main MENU: 

def runmain():
    while True:
        answer = input("""\n    to see what we have - enter '1'
    to change something - enter '2'
    to delete something - enter '3'
    \nto quit - enter 'q'
    \nyour answer is - """)
        if answer == 'q':
            cls()
            break
        elif answer == '1':
            show_rec()
            cls()
            break
        elif answer == '2':
            changging()
            cls()
            break
        elif answer == '3':
            deleting()
            cls()
            break
        else:
            cls()



#Starting program >>>>>>>>>>>>>>>>>>>>>>>>.
answer = ''
cls()
print ("\n\tWellcome to our Orangery^!")
runmain()





os.system('clear')

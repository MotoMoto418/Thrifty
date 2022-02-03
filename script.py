from utils import Utils
from firebaseinit import Firebase


fire = Firebase()
utils = Utils()

user_info = {'isLoggedIn': False}

Flag0 = True
while Flag0:
    choice0 = input("\nWhat would you like to do today? Enter -\nsignup - To sign up\nsignin - To sign in\nquit - To quit\n")

    if choice0.lower() == 'signup':
        Flag1 = True
        while Flag1:
            name = input("\nEnter your full name: ")
            email = input("\nEnter your email address: ")
            password = input("\nEnter the password: ")
            c_password = input("\nPlease confirm the password: ")

            if password == c_password:
                try:
                    data = utils.signup(name, email, password)
                    user_info.update(data['info'])
                    UID = data['UID']
                    fire.db.child('users').child(UID).child('user-data').update(user_info)

                    choice1 = input("\nWould you like to sign in? (Y/N)\n")

                    if choice1.lower() == 'y':
                        try:
                            UID = utils.signin(email, password)
                            fire.db.child('users').child(UID).child('user-data').update({'isLoggedIn': True})
                            user_info['isLoggedIn'] = True

                            user_name = fire.db.child('users').child(UID).child('user-data').child('name').get().val()
                            
                            Flag1 = False

                        except:
                            print("\nError.\n")
                            Flag1 = False

                    elif choice1.lower() == 'n':
                        Flag1 = False

                    else:
                        print("\nInvalid input. Exiting.\n")
                        Flag1 = False

                except:
                    print("\nUnknown error.\n")

            else:
                print("\nPasswords do not match. Please try again.\n")
                continue

    elif choice0.lower() == 'signin':
        Flag2 = True
        while Flag2:
            email = input("\nEnter your email address: ")
            password = input("\nEnter your password: ")

            try:
                UID = utils.signin(email, password)
                fire.db.child('users').child(UID).child('user-data').update({'isLoggedIn': True})
                user_info['isLoggedIn'] = True

                user_name = fire.db.child('users').child(UID).child('user-data').child('name').get().val()

                Flag0 = False
                Flag2 = False

            except:
                print("Please try again.\n")
                continue

    elif choice0.lower() == 'quit':
        print("\nThank you for using our program.\n")
        Flag0 = False

try:
    isLoggedIn = fire.db.child('users').child(UID).child('user-data').child('isLoggedIn').get().val()
    while isLoggedIn:
        print(f"\nHello {user_name}, what would you like to do today?")
        choice0 = input("\nEnter -\nupdate - To update tracking list\nview - To view tracking info\nquit - To quit\n")

        if choice0.lower() == 'update':
            innerFlag = True
            while innerFlag:
                inner_choice = input("\nEnter - \nadd - To add links to track\ndel - To stop tracking a link\nback - To go back")

                if inner_choice.lower() == 'add':
                    items = dict(fire.db.child('users').child(UID).child('tracking-data').get().val())
                    keys = [key for key in items]

                elif inner_choice.lower() == 'del':
                    pass

                elif inner_choice.lower() == 'back':
                    innerFlag = False

                else:
                    print("\nInvalid input.\n")
                    continue

        elif choice0.lower() == 'view':
            beauty, websites = utils.show(UID)
            print(beauty)

            Flag1 = True
            while Flag1:
                choice1 = int(input("\nEnter serial number of the item to view the URL. To exit, type 0.\n"))

                if choice1 == 0:
                    Flag1 = False

                else:
                    print(f"URL - {websites[choice1 - 1]}")

        elif choice0.lower() == 'quit':
            fire.db.child('users').child(UID).child('user-data').update({'isLoggedIn': False})
            break

except:
    pass

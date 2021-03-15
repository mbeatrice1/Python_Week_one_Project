
#!/usr/bin/env python3.6
from user import User 
from credential import Credential

'''
****User account methods****
'''

def create_user_account(fname, lname, password, confirmPassword):
    '''
    Method to create application user account
    '''
    new_user_account = User(fname, lname, password, confirmPassword)
    return new_user_account

def save_user_account(user_account):
    '''
    Method to save user account
    '''
    user_account.save_user()

def check_user(user_name):
    '''
    Method to check if a user of a given name exists
    '''

    return User.is_user_exists(user_name)

def get_user(user_name):
    '''
    Method to get a user by user's first name
    '''

    return User.find_by_name(user_name)


'''
 ****Credential methods****
'''

def create_credential(account_name, password):
    '''
    Method to create a new credential
    '''

    new_credential = Credential(account_name, password)
    return new_credential

def save_credential(new_credential):
    '''
    Method to save new credential into the credential_list
    '''

    new_credential.save_credential()

def delete_credential(credential_to_delete):
    '''
    Method to delete credential
    '''
    credential_to_delete.delete_credential()

def get_credential_by_accound_name(account_name):
    '''
    Method to find a credential by account name
    '''

    return Credential.find_by_account_name(account_name)

def is_credential_exists(account_name):
    '''
    Method that check if a credential exists
    '''

    return Credential.is_credential_exists(account_name)

def get_all_credential():
    '''
    Method that display all saved credential
    '''

    return Credential.display_credentials()

def main():
    print("\nWelcome to Password Locker Application.")
    print("What is your name?")
    user_name = input()
    print(f"\nHello {user_name}. Welcome to our application")
    print("*"*35)
    print("You need to signup to use this application")
    print("\n")

    print("Signup")
    print("-"*7)
    print("\n")

    print("Enter your first name:")
    fname = input()
        
    print("Enter your last name:")
    lname = input()

    print("Enter new password:")
    password = input()

    print("Confirm your password:")
    confirmedPassword = input()

    if password == confirmedPassword: 
        save_user_account(create_user_account(fname, lname, password, confirmedPassword))
        print("\nYou have successfully created your account.")
        print("\n")

        while True:
            print("Make your choice : ")
            print("Press 1. to Login")
            print("Press 0. to Exit")

            choice = input()

            if choice == "1":

                print("\nLogin with your first name to start")
                print("*"*35)

                print("\nEnter your first name:")
                logged_first_name = input()

                print("\nEnter your password:")
                logged_password = input()

                # check if the user exists
                if check_user(logged_first_name):
                    logged_user = get_user(logged_first_name)
                    if logged_user.password == logged_password and logged_user.fname == logged_first_name:
                        print("\n***Successfully logged in***\n")
                        # Print the menu

                        print("Menu")
                        print("*"*5)
                        print("\n")

                        while True:
                            print("Use these short codes : nc - new credential, dc - display credentials, fc - find a credential, rm - remove credential, ex -exit password locker ")

                            short_code = input().lower()

                            if short_code == "nc":
                                print("\nNew credential")
                                print("-"*15)

                                print("\nEnter Account Name:")
                                account_name = input()

                                print("\nEnter credential password")
                                cred_pass = input()

                                save_credential(create_credential(account_name, cred_pass))
                                print(f"\nCredential {account_name} is successfully saved\n")

                            elif short_code == "dc":

                                print("\n***All Credentials***\n")

                                if get_all_credential():
                                   for credential in get_all_credential():
                                        print(f"Credential Name : -------------{credential.account_name}")
                                        print(f"Credential Password : ---------{credential.password}")
                                        print("\n")
                                else :
                                    print("------No credential saved yet-------\n")
                
                            elif short_code == "fc":

                                print("\nEnter credential name :  ")
                                credential_to_search = input()

                                if is_credential_exists(credential_to_search):
                                    found_credential = get_credential_by_accound_name(credential_to_search)
                                    print(f"\nCredential name: ----------- {found_credential.account_name}")
                                    print(f"Credential password: -------- {found_credential.password}")
                                    print("\n")
                                else:
                                    print(f"\nCredential {credential_to_search} does not exists\n")

                            elif short_code == "rm":

                                print("\nEnter credential name to delete : ")
                                credential_name_to_remove = input()

                                if is_credential_exists(credential_name_to_remove):
                                    credential_to_remove = get_credential_by_accound_name(credential_name_to_remove)
                                    delete_credential(credential_to_remove)
                                    print(f"\nCredential {credential_name_to_remove} successfully removed\n")
                                else:
                                    print(f"\nCredential {credential_name_to_remove} does not exists\n")

                            elif short_code == "ex":
                                print("\n.......Thank you for using Password Locker.......\n")
                                break
                            else:
                                print("\n!!!You entered a wrong short code. Try again")
                                print("\n")
                    else :
                        print("\n***Wrong username or password***\n")
                else:
                    print("\n***User not found.Check well your first name***\n")
            elif choice == "0":
                print("\n----GoodBye----\n")
                break
            else: 
                print("\nWrong choice.Enter 1 to Login or 0 to exit\n")

    else:
        print("\n***Your password doesn't match. Try again***\n")



if __name__ == "__main__":
    main()
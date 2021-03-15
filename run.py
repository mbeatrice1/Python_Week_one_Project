#!/usr/bin/env python3.6
 from user import User
 import getpass

def create_user(username,passcode)

new_user = User(username,passcode)new
return new_user














def main():
    print("Welcome to the Password Locker for Your Application")
    print("Create Your Account to Store Your Passwords Or Login if You have an account")
    user_name=input()
    passcode= getpass.getpass("Create Your Password")
    
    

    
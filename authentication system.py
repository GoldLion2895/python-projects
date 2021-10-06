import random
import uuid


def newuser():
    print("Hello! please enter your name age and a password.")
    name=input("Enter your name: ")
    age=input("Enter your age: ")
    username=name[0:3]+age
    password=input("Enter a secure password: ")
    userid = uuid.uuid1().int
    print(f"We have created the username {username} based on your name '{name}' and age '{age}'.\nHere is your UserID - '{userid}' || Make sure to save it for further usage")
    print("\nNow you can login to our website :)")
    with open('db.txt', 'a') as file:
        file.write(f"Name={name},UserID={userid},Age={age},Username={username},Password={password}\n")
    login()

def login():
    print("Hello! please enter your UserID and password.")
    userid=input("Enter your UserID: ").strip()
    password = input("Enter your password: ").strip()

    with open("db.txt",'r')as file:
        entries = file.readlines()
    
    for i in entries:
        credits = i.split(",")
        userID = credits[1].split("=")[1].strip()
        username = credits[3].split("=")[1]
        passWord = credits[4].split("=")[1].strip()
        if userID == userid and password == passWord:
            print(f"Logged in successfully\nWelcome back {username.title()} to our Website")
            return
        else:
            continue
        
    print("Incorrect credentials, Please try again or register")
    turn = input("Login/register, type l/r : ").lower()
    if turn == "l":
        login()
    else:
        newuser()

    



first_input = input("Welcome to the website. To get started, please Login/Register\nType l to login and r to register :").lower()
def statement(first_input):
    if first_input == "l":
        login()
    elif first_input == "r":
        newuser()
    else:
        print("\n**Incorrect Mode selected!**\n")
        first_input = input("Please Login/Register\nType l to login and r to register :").lower()
        statement(first_input)

statement(first_input)
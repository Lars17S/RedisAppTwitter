import redis

# Users : hash
# Following : List(users : string)
# Tweets : List(text)


# Funcionalidades
# - Users login
# - Create user


def login():
    for i in range(3):
        print("============ LOG IN ============")
        username = input("Enter your username:\n")
        password = input("Enter your password:\n")
        if r.hget("users", username) == password.encode('utf-8'):
            return True
        print("\nIncorrect password")
        print("================================\n")
    if "y" == input("\nYou have exceeded the number of attempts. Do you want to register? (y/n)\n").lower():
        return register()
    else:
        return False

def register():
    while True:
        print("=========== REGISTER ===========")
        username = input("Enter your username:\n")
        password = input("Enter your password:\n")
        if not r.hexists("users", username):
            r.hset("users", username, password)
            return True
        if "y" == input("\nThis username already exists!. Do you want to log in? (y/n)\n").lower():
            return login()
        print("================================\n")

def twitter():
    print("============ TWITTER ============")
    
def controller():
    print("============= MENU =============")
    print("Select option: "
          "\n\t1) Log In"
          "\n\t2) Register")
    option = int(input())
    validation = login() if option == 1 else register()
    print("================================\n")
    if validation:
        twitter()

r = redis.Redis(host='localhost', port=6379, db = 1)
controller()
import redis

# Users : hash
# Following : List(users : string)
# Tweets : List(text)


# Funcionalidades
# - Users login
# - Create user

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def login():
    print("\n============ LOG IN ============")
    for i in range(3):
        username = input("\nEnter your username:\n")
        password = input("Enter your password:\n")
        if r.hget("users", username) == password.encode('utf-8'):
            return True
        elif not r.hexists("users", username):
            if "y" == input(color.YELLOW+"\nThe username does not exist. Do you want to register? (y/n)\n"+color.END).lower():
                return register()
        else:
            print(color.RED+"\nIncorrect password!"+color.END)
    print(color.RED+"You have exceeded the number of allowed attempts. Exiting app..."+color.END)
    return False

def register():
    print("\n=========== REGISTER ===========")
    while True:
        username = input("\nEnter your username:\n")
        password = input("Enter your password:\n")
        if not r.hexists("users", username):
            r.hset("users", username, password)
            return True
        if "y" == input(color.YELLOW+"\nThis username already exists!. Do you want to log in? (y/n)\n"+color.END).lower():
            return login()

def twitter():
    print("\n============ TWITTER ============")
    
def controller():
    print("\n============= MENU =============")
    print("Select option: "
          "\n\t1) Log In"
          "\n\t2) Register")
    option = int(input())
    validation = login() if option == 1 else register()
    if validation:
        twitter()

r = redis.Redis(host='localhost', port=6379, db = 1)
# r.flushall()
controller()
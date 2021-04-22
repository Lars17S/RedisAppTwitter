import redis

# Users : hash
# Following : List(users : string)
# Tweets : List(text)


# Funcionalidades
# - Users login
# - Create user

r = redis.Redis(host='localhost', port=6379, db = 0)

# r.flushdb()



def login():
    for i in range(3):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if r.hget("users", username).decode("utf-8") == password:
            return True
        print("Incorrect password")
    if "y" == input("You have exceeded the number of attempts. Do you want to register? (y/n)").lower():
        register()
    else:
        return False

def register():
    while True:
        username = input("Enter your username: ")
        if not r.hexists("users", username):
            password = input("Enter your password: ")
            r.hset("users", username, password)
            return True
        print("This username already exists!")

def twitter():
    print()
    
def controller():
    print()
    # Validad login o registro
        # Si verdadero: Pasarlo a la app twitter
    # Si falso, salirse




# print("1: Login\n2: Create user")



# print(r.keys('*'))
# print(r.keys('*'))
# r.set('Hello', 'World')
# print(r.get('Hello').decode('utf-8'))
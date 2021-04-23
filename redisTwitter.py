import redis
import threading
import time
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
            return twitter(username)
        elif not r.hexists("users", username):
            if "y" == input(color.YELLOW+"\nThe username does not exist. Do you want to register? (y/n)\n"+color.END).lower():
                return register()
        else:
            print(color.RED+"\nIncorrect password!"+color.END)
    print(color.RED+"You have exceeded the number of allowed attempts. Exiting app..."+color.END)
    return

def register():
    print("\n=========== REGISTER ===========")
    while True:
        username = input("\nEnter your username:\n")
        password = input("Enter your password:\n")
        if not r.hexists("users", username):
            r.hset("users", username, password)
            return twitter(username)
        if "y" == input(color.YELLOW+"\nThis username already exists!. Do you want to log in? (y/n)\n"+color.END).lower():
            return login()
def tweet(username:str):
    tweet = input("What's happening?:\n")
    r.lpush(username+":Tweets",tweet)
    r.publish(username+':Channel', tweet)

def follow(username: str):
    followTo = input("Who do you want to follow?\n")
    if not r.hexists("users", followTo):
        print("This user does not exist")
    elif not r.sadd(username+":Subs", followTo):
        print("You already follow "+ followTo)
    else:
        r.sadd(followTo + ":Followers", username)
        print("Now you're following "+followTo)


def getFollowers(username: str):
    followers = r.smembers(username+":Followers")
    followers= [x.decode("utf-8") for x in followers]
    return followers

def getSubs(username:str):
    subs = r.smembers(username + ":Subs")
    subs= [x.decode("utf-8") for x in subs]
    return subs

def printFollowers(username:str):
    followers=getFollowers(username)
    print("\n======== Followers =========")
    for f in followers:
        print("-\t"+f)

def printSubs(username:str):
    subs=getSubs(username)
    print("\n======== Subscriptions =========")
    for s in subs:
        print("-\t"+s)

def checkSubsTweets(username:str):
    global stop_threads
    stop_threads = False
    subs = getSubs(username)
    subsChannel = [x+":Channel" for x in subs]
    rb = r.pubsub()
    rb.subscribe(subsChannel)

    for item in rb.listen():
        print(item)
        if stop_threads:
            print(color.RED + "Gina me matoooooo X|" + color.END)
            break
    print(color.RED+"Finished"+color.END)

def seeTimeline(username:str):
    print("\n======== Timeline =========")
    global stop_threads
    stop_threads = True
    t = threading.Thread(target=checkSubsTweets, args=[username], daemon=True)
    t.start()
    print("sth2")


def twitter(username: str):
    while True:
        print("\n============ TWITTER ============")
        print("Select an option "
          "\n1) Hacer un tweet"
          "\n2) Seguir a alguien"
          "\n3) Ver seguidores"
          "\n4) Ver suscripciones"
          "\n5) Ver timeline"
          "\n6) Exit")
        option =int(input())
        if option==1: tweet(username)
        elif option==2: follow(username)
        elif option==3: printFollowers(username)
        elif option==4: printSubs(username)
        elif option==5: seeTimeline(username)
        else: return
    
def controller():
    print("\n============= MENU =============")
    print("Select an option: "
          "\n\t1) Log In"
          "\n\t2) Register")
    option = int(input())
    login() if option == 1 else register()

stop_threads = False
r = redis.Redis(host='localhost', port=6379, db = 1)
r.sadd("sebas:Subs", "efrenbbprecioso")
# r.flushall()
controller()
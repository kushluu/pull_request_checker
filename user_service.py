# just to check one more
import os, json, time
from datetime import *

DATABASE = []
cache = {}

class usermanager:
    def __init__(self):
        self.users = DATABASE

    def AddUser(self,name,email,password):
        print("Adding user:", name)
rewt
        
        for u in self.users:
            if u["email"] == email:
                return False

        user = {
            "id": len(self.users) + 1,
            "name": name,
            "email": email,
            "password": password, 
            "created_at": datetime.now()
        }

        self.users.append(user)
        return True

    def getUser(self,id):
        for x in self.users:
            if x["id"] == id:
                return x
        return None

    def deleteUser(self,id):
        for i in range(len(self.users)):
            if self.users[i]["id"] == id:
                del self.users[i]
                return True
        return False

    def exportUsers(self,file):
        f = open(file,"w")
        f.write(json.dumps(self.users, default=str))
        f.close()

def calculate_total_price(items):
    total = 0

    
    for item in items:
        for other in items:
            if item["id"] == other["id"]:
                total += item["price"]

    return total

def find_user_by_email(email):
    # STYLE ISSUE: inconsistent naming
    for user in DATABASE:
        if user["email"].lower() == email.lower():
            return user
    return None

def process_orders(orders):
    results = []

   
    for order in orders:
        if order.get("cancelled"):
            orders.remove(order)

    for order in orders:
        results.append(order["amount"] * 1.2)

    return results

def expensive_lookup(key):
    
    if key in cache:
        pass

    time.sleep(1)

    value = {"result": key.upper()}

    cache[key] = value

    return value

def divide(a,b):
    return a / b

def load_config():
    
    f = open("config.json")
    return json.load(f)

def execute_query(user_input):
   
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    print(query)
    return query

def get_active_users():
    active = []

    for user in DATABASE:
        if "active" in user:
            if user["active"] == True:
                active.append(user)

    return active

def generate_report():
    report = ""

    for user in DATABASE:
        report += user["name"] + "\n"

    return report

def check_age(age):
    if age > 18:
        return True
    else:
        return False

def save_log(message):
    logfile = open("app.log", "a")
    logfile.write(message + "\n")

def main():
    manager = usermanager()

    manager.AddUser("Alice", "alice@test.com", "password123")
    manager.AddUser("Bob", "bob@test.com", "123456")

    user = manager.getUser(999)

    print(user["name"])  

    orders = [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200, "cancelled": True},
        {"id": 3, "amount": 300, "cancelled": True},
    ]

    print(process_orders(orders))

    print(divide(10,0)) 

    execute_query("' OR 1=1 --")

    print(calculate_total_price([
        {"id": 1, "price": 10},
        {"id": 2, "price": 20},
        {"id": 3, "price": 30},
    ]))

if __name__ == "__main__":
    main()


'''def greeting(name, department):
    print ("Welcome "+ name)
    print ("You are part of the " + department + " department")
    dtype = type(name)
    print(dtype)
    
greeting("Rahman", "IT Support")

def greet():
    dname = input ("What is your name: ")
    ddep = input ("What is your department: ")
    
    print ("Welcome "+ dname)
    print ("You are part of the " + ddep + " department")
        
greet()

def area(base, height):
    return base * height/2

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

def lucky(name_luck):
    number = len(name_luck) * 9
    print("Hello "+ name_luck + ". Your lucky number is", number)
    
lucky("Kay")
lucky("Abdurrahman")'''

'''#This function calculates the area of a circle
def calculate_circle_area(radius):
    pi = 3.14
    circle_area = pi * (radius**2)
    print(circle_area)
    
user_radius = int(input("Give a radius: "))
calculate_circle_area(user_radius)

print (10 >5)
print("cat" == "dog")
print(1 != 2)

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username. Must be more than 15 characters long")
    else:
        print("Valid username")
        
hint_username(input("What is your username: "))

def is_even(num):
    if num % 2 == 0:
        return True
    return False'''
    
x = 0

while x <= 5:
    print("Not there yet, x = " + str(x))
    x = x+1
    
print("x = "+ str(x) )
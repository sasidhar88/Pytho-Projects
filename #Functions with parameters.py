#Functions with parameters
def greet():
    print("Hello")
    print("Hello")
    print("Hello")

greet()
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Hello {name}")
    print(f"Hello {name}")

greet_with_name("Sasi")
# Funtions with more than 1 input

def greet_with(name,location):
    print(f"hello {name}\n"f"this is my {location}")

greet_with("sasi","Tirupati")


def greet_with_Keys(name,location):
    print(f"hello {name}\n"f"this is my {location}")

greet_with_Keys(location="Tirupati",name="sasi")

# Prime nuber checker
#Write your code below this line 👇

def prime_checker(number):
    is_prime = True
    for each in range(2,number):
        if number % each == 0:
           is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

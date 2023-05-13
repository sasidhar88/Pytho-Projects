'''
myvar= "abc"
my_dict = {
    "a": "b",
    "c": "d"

}
# print(my_dict["c"])
my_dict["e"] = "hello"
# print(my_dict)
# empty_dict = {}

for key in my_dict:
    print(key)
    print(my_dict[key])

# travel_log ={
#      {"Country": "France","cities_visited" :["Paris","Lille","Dijon"],"Num":12}
      
# }
'''
#functions with outputs
#calculator
#Creating the add funtion
def add(n1,n2):
    """ this functions adds by taking two inputs"""
    return n1 + n2

def sub(n1,n2):
    """ this functions subtracts by taking two inputs"""
    return n1 - n2

def mul(n1,n2):
    """ this functions multiplies by taking two inputs"""
    return n1 * n2

def div(n1,n2):
    """ this functions divides by taking two inputs"""
    return n1 / n2

operations ={
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}
def calculator():
    num1 = int(input("Please enter the number: "))
    for each in operations:
        print(each)
    should_cont = True
    while should_cont:
        op_sym = input("Please pick an operation : ")
        num2 = int(input("Please enter the number: "))
        cal_c = operations[op_sym]
        answer = cal_c(num1, num2)
        print(f"{num1}  {op_sym}  {num2} = {answer}")
        if input("Please selet 'Y' to continue ans 'N' to end:  ") == 'y':
            num1 = answer
        else:
            should_cont = False
            calculator()

calculator()
        


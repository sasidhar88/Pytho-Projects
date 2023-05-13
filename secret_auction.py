
#HINT: You can call clear() to clear the output in the console.
def winner(bidder_records):
    highest = 0
    for key in bidder_records:
        bider_amt = my_dict[key]
        if bider_amt > highest:
            won = key
            highest = bider_amt
    print(f"the winner is {won} with the bid amount {highest}.")
nums = True
my_dict = {}
while nums:
    print("welcome to the secret auction programme")
    name=input("what is your name ?:")
    price = input("Whats your bid?: $")
    bid = int(price)
    choice=input("Are there any other bidders, Type 'Yes' or 'No'")
    my_dict[name] = bid
    if choice == "No":
        nums = False
        winner(my_dict)
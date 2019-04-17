number = int(input("What number do you want to factor? "))
factor = 2 #factors to try start at 2
factors_multiplied = 1 #factors multiplied together, once this equals number you're done
while factor <= number:
    if number % factor == 0: #can number be divided by factor?
        factors_multiplied *= factor #increment up (1*2 = 2)
        number /= factor #decrement number (12/2 = 6)
        print(factor)
        factor = 2 #start back at 2
    else:
        factor += 1 #if the number can't be divided by the factor, add 1 and try again


"""
for first_num in range(0,11):
    for second_num in range(0,11):
        multiple = first_num * second_num
        print("%d X %d = %d" % (first_num, second_num, multiple))
"""
"""
height = int(input("How tall is the triangle? "))
index = 1
while index <= height:
    print_string = " " * (height - index) + "*" * (1 + (2 * (index - 1)))
    print(print_string)
    index += 1
"""
"""
How many coins?

should_run = True
coin_count = 0
while should_run:
    print("You have %d coins" % coin_count)
    answer = input("Would you like a coin? ").lower()
    if answer == "yes":
        coin_count += 1
    elif answer == "no":
        should_run = False
        print("Goodbye")
    else:
        print("What? ")
    
"""
"""
start_number = int(input("What number should I start with? "))
end_number = int(input("What number should I end with? "))

while start_number <= end_number:
    print(start_number)
    start_number += 2
"""
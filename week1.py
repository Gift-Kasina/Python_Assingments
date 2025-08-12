# Step 1: Ask the user to input the first number
# We use 'float()' to make sure our numbers can have decimals.
num1 = float(input("Enter the first number: "))

# Step 2: Ask the user to input the second number
num2 = float(input("Enter the second number: "))

# Step 3: Ask the user what they want to do with these numbers
sign = input("What do you want to do with these numbers? (+,-,/,*): ")
# Step 4: Perform the operation based on user input
if sign == "+":
    result = num1 + num2 
    print(f"Sum: {result}")       
elif sign == "-":
    result = num1 - num2
    print(f"Difference: {result}")
elif sign == "*":
    result = num1 * num2
    print(f"Product: {result}")
elif sign == "/":
    if num2 != 0:
        result = num1 / num2  
        print(f"Quotient: {result}")
          
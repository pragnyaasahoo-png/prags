print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")
choice = input("Enter choice (1/2/3/4): ")


if(choice in ('1', '2', '3', '4')): 
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == '1':
        print(num1, "+", num2, "=", num1 + num2)
    elif choice == '2':
        print(num1, "-", num2, "=", num1 - num2)
    elif choice == '3':
        print(num1, "*", num2, "=", num1 * num2)
    elif choice == '4':
      if num2 != 0:
            print(num1, "/", num2, "=", num1 / num2)
 
      else:           
        print("Error: Division by zero is not allowed.")
  
else:
  {  print("Invalid Input")  
  }
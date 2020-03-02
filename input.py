num = int(input("enter the number?"))  
if num%2 == 0:  
    print("Number is even")

num1 = int(input("enter the number?"))  
num2 = int(input("enter the number?"))  
if num1+num2 == 100:  
    print('You won the price') 
else:
    print('Better luck next time')

num1 = int(input("enter the number?"))  
num2 = int(input("enter the number?"))  
num3 = int(input("enter the number?"))  
if num1>num2 and num1>num3:  
    print('num1 is greater') 
elif num2>num1 and num2>num3:
    print('num2 is greater') 
elif num3>num1 and num3>num2:
    print('num3 is greater') 
else:
    print('All numbers are equal')
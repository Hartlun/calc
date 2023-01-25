import math
print ('1 add')
print ('2 subtract')
print ('3 multiply')
print ('4 divide')
operation = input ()
if operation == '1':
    num1 = input('enter number: ')
    num2 = input('enter second number: ')
    result = ( int(num1) + int(num2))
    print(result)
elif operation == '2':
    num1 = input('enter number: ')
    num2 = input('enter second number: ')
    result = ( int(num1) - int(num2))
    print(result)
elif operation == '3':
    num1 = input('enter number: ')
    num2 = input('enter second number: ')
    result = ( int(num1) * int(num2))
    print(result)
elif operation == '4':
    num1 = input('enter number: ')
    num2 = input('enter second number: ')
    result = ( int(num1) / int(num2))
    print(result)
else:
    print ('wrong Value')

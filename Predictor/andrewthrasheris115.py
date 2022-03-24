"""
Andrew Thrasher
IS115
completed  - 03/23
time - 1 hr

Two programs here, first is a basic calculator, input two numbers and perform operation baseed on user inputs
Second, figures grand total price based on qty and price and then adjsuted for tax, shipping and discounts
"""
#required input
um1 = float(input("Please input your first number:  "))

num2 = float(input("Please input your second number: "))
sign = input("Please enter the operator: +, -, *, /, or % (Note if / or % the second number cannot be zero.) * ")


#apply operation based on operator and give output 
if sign ==  '+':
    answer = float(num1) + float(num2)
    print(num1, '+', num2, " = ", answer)

elif sign == '-':
    answer = float(num1) - float(num2)
    print(num1,  '-', num2, '=', answer)

elif sign == '*':
    answer = float(num1) * float(num2)
    print(num1, '*', num2, '=', answer)

elif sign == '/':
    answer  = float(num1)/float(num2)
    print(num1, '/', num2, '=', answer)
elif sign == '%':
    answer = float(num1) % float(num2)
    print(num1, '%', num2, '=', answer)
else:
    print("ERROR --- Invalid operator")

"""

#input qty and price
qty = float(input("Enter number of items purchased: "))
price  = float(input("Enter the retail price:  "))
price = format(price, '.2f')


#error check
if qty <= 0:
    print("“ERROR – This cannot be processed – good bye!” ")

#discount checks
if qty >= 0 and qty <= 9:
    discount = 0
elif qty  >= 10 and qty <= 19:
    discount = .10
elif  qty >= 20 and qty <= 39:
    discount = .15
elif qty >= 40 and qty <= 79:
    discount = .20
elif qty >= 80 and qty <= 99:
    discount = .25
elif qty >= 100:
    discount = .30

#shipping check 
if qty > 50:
    shipping = 0
else:
    shipping = 35

#required formulas for totals
total = float(qty)  * float(price)
discount = float(total) * float(discount)

tax = .08 * float(total)
grandTotal = (total - discount) + tax + shipping

#required output
print("Quantity = ",qty )
print("Retail Price = ", price)
print("Total = $", total)
print("Discount = $", discount)
print("Tax =$", tax)
print("Shipping fee = $", shipping)
print("Grand Total = $", grandTotal)
"""
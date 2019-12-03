'''
This program checks if a credit card numnber is valid according to Luhn's
algorithm.
---Program written by Son Nguyen---
'''
credit_number = int(input("Input your credit card number: "))
credit_string = str(credit_number)
num_digits = len(credit_string)
first_two_digits = int(credit_string[:2])
first_digit = int(credit_string[:1])
total_sum = 0
credit_type = ""
invalid = False

for i in range(num_digits):
    number = credit_number % 10
    if i % 2 == 1:
        number = number * 2
        if number > 10:
            number = number // 10 + number % 10
        total_sum = total_sum + number
    else:
        total_sum = number + total_sum
    credit_number = credit_number // 10

if num_digits == 15 and (first_two_digits == 37 or first_two_digits == 34):
    credit_type = "AMEX"
elif num_digits == 16 and 51 <= first_two_digits <= 55:
    credit_type = "MASTERCARD"
elif (num_digits == 13 or num_digits == 16) and first_digit == 4:
    credit_type = "VISA"
else:
    invalid = True

if total_sum % 10 == 0 and not(invalid):
    print(credit_type)
else:
    print("INVALID")

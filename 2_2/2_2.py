number = int(input('Ввести 5-значное число:'))

reversed_number = 0

while number > 0:
    digit = number % 10
    number= number// 10

    reversed_number = reversed_number * 10 + digit

print(reversed_number)
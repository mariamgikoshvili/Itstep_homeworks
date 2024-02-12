'''დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს "n" და ბეჭდავს 1-დან "n"-მდე რიცხვების ჯამს.'''

num = eval(input("Enter a number: "))

n = 0
for i in range(1,num):
    n += i
print(n)


'''დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს და შემდეგ 
იყენებს "while" ციკლს რომ რევესრულად დაბეჭდოს რიცხვები 0-მდე. მაგალითად თუ შეიყვანს 4, დაიბეჭდოს 4, 3, 2, 1'''

num = eval(input('Enter a number: '))

while num > 0:
    print(num, end = ' ')
    num -= 1
    
    
'''დაწერეთ პითონის პროგრამა თამაშისთვის, რომელიც მუდმივად სთხოვს მომხმარებელს გამოიცნოს წინასწარ განსაზღვრული რიცხვი. 
როდესაც მომხმარებელი გამოიცნობს სწორ რიცხვს, დაასრულებს პროგრამა მუშაობას.'''

import random
number = random.randint(0, 100)
guess = eval(input("Enter a number"))


while guess != number:
    if guess > number:
        print(f"The number is less than {guess}")
        guess = eval(input("Enter a number: "))
    else:
        print(f"The number is more than {guess}")
        guess = eval(input("Enter a number: "))

print('You guessed the number!')

'''დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მუდმივად რიცხვებს. შექმენით საწყისი ცვლადი total_sum = 0, 
შეამოწმეთ რიცხვი თუ დადებითია, მხოლოდ მაშინ დაუმატეთ total_sum ცვლადს.
ეს პროცესი გაგრძელდეს იქამდე სანამ მომხმარებელი არ შეიყვანს 'sum' ტექსტს, რის შემდეგაც დაიბეჭდება შეყვანილი დადებითი რიცხვების ჯამი.'''

total_sum = 0

while True:
    number = input("Enter a number or type 'sum' to result total sum of positive numbers entered:  ")
    if number == 'sum':
        print(total_sum)
        break
    elif int(number) > 0:
        total_sum += int(number)



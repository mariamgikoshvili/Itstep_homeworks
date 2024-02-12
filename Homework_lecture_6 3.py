''' 1. დაწერეთ პითონის პროგრამა, რომელიც დასაწყისში შექმნის ცარიელ სიას ([]), 
თუ მომხარებელი შეიყვანს სიმბოლო 'a'-ს, ნიშნავს რომ უნდა დაამატოთ სიაში რიცხვი; 
თუ აკრიფა 'r', სიიდან უნა წაიშალოს რიცხვი; 'e'-ს შეტანისას პროგრამამ უნდა დაასრულოს მუშაობა. 
მიღებული შედეგი დაბეჭდეთ კონსოლში.
მომხარებელმა უნდა შეიყვანოს შემდეგი სტრუქტურით ბრძანება "{command} {number}" commands:

a – append

r – remove

e – exit

მხოლოდ გამოიყენეთ ეს ბრძანებები და მოახდინეთ სიაზე ზემოქმედება.'''

list_1 = []

while True:
    command = input("Enter a command:\na - append\nr - romove\ne - exit\n")
    
    if command == 'a':
        num = int(input("Enter a number: "))
        list_1.append(num)
    elif command == 'r':
        num = int(input("Enter a number: "))
        list_1.remove(num)
    elif command == 'e':
        print(f'The final list is {list_1}.')
        break
        

''' დაწერეთ პითონის პროგრამა, რომელიც შექმნის სიას my_list = [43, '22', 12, 66, 210, ["hi"], და შეასრულებს შემდეგ ნაბიჯებს:
a. დაბეჭდავს 210-ის ინდექსს;

b. დაამატებს ბოლო ელემენტში ტექსტს "hello";

c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს სიას;

d. შექმენით ახალი სია my_llist_2, რომელსაც ექნება my_llist-ის მნიშვნელობა, გაასუფთავეთ my_llist_2-ის მნიშნველობა და დაბეჭდეთ ორივე სია.

my_list = [43, '22', 12, 66, 210, ['Hi']]'''

print(f' The index of 210 is {my_list.index(210)}.')
my_list.append("Hello")
my_list.remove(my_list[2])
print(my_list)

my_list_2 = my_list.copy()

my_list_2.clear()
print(my_list)
print(my_list_2)



'''3.დაწერეთ პითნის პროგრამა, რომელიც მიიღებს ტელეფონის ნომერს და regex-ით შეამოწმებს შეყვანილი ნომერი 
იცავს თუ არა "(123) 456-789" ფორმატს, 
თუ იცავს დააბრუნეთ შეყნვაილი ტელეფონის ნომერი, წინააღმდეგ შემთხვევაში გამოიტანეთ "Invalid format" ტექსტი.'''

import re
number = input("Enter a number: ")

pattern =  r"\(+\d{3}+[)]\s\d{3}+[-]+\d{3}"
found = re.match(pattern, number)

if found:
    print(number)
else:
    print("Invalid format.")
'''შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], in-ის გამოყენებით დაწერეთ პროგრამა
რომელიც შეამოწმებს თქვენს მიერ შეტანილი რიცხვი არის თუ არა სიაში.'''

num_list=[44, 23, 11, 8, 20, 56, 33, 55]

number = eval(input("Enter a number: "))

if number in num_list:
    print('The number is in list')
else:
    print('The number not in list')

'''დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეყვანილი რიცხვის ლუწობასა და კენტობას. 
თუ რიცხვი ლუწია გამოიტანეთ ტექსტი 'even' თუ კენტია 'odd'.'''

number = eval(input('Enter a number'))

if number % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')

'''შექმენით ორი სტრინგის ტიპის ცვლადი st1 და st2, 
შეადარეთ ისინი is-ის გამოყენებით, თუ ემთხვევა გამოიტანეთ ტექსტი "Same object", წინააღმდეგ შემთხვევაში "Different object"'''

str1 = 'book'
str2 = 'pen'

if str1 is str2:
    print('Same object')
else:
    print('Different object')

'''შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], შეიტანეთ რიცხვი და დაწერეთ შემდეგი პირობა:
1. თუ შეტანილი რიცხვი მეტია სიაში არსებულ მე-3 ელემენტზე და
  ნაკლებია ბოლო ელემენტზე გამოიტანეთ ტექსტი "More than list elements";
2. თუ შეტანილი რიცხვი უდრის სიის მე-6 ელემენტს გამოიტანეთ ტექსტი "Equal"; 
3. სხვა ნებისმიერ შემთხვევაში გამოიტანეთ ტექსტი "None of the conditions were met".
რიცხვის შეტანის ოპერაციისთვის გამოიყენეთ input მეთოდი.'''

num_list = [44, 23, 11, 8, 20, 56, 33, 55]
number = eval(input("Enter a number"))

if number > num_list[2] and number < num_list[-1]:
    print('more than list elements')
elif number == num_list[5]:
    print('Equal')
else:
    print('None of the conditions were met')
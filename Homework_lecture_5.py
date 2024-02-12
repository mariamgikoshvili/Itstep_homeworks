'''დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს სტრიქონის UTF-8 დაშიფრულ ვერსიას'''

str = input("Enter a string: ")

str1 = str.encode("utf-8")
print(str1)

'''დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს. ჩამოაშორეთ ზედმეტი ინტერვალები. ყველა სიმბოლო გადაიყვანეთ პატარა 
ასოებში და დაუმატეთ ქვესტრიქონი 'Python'. თუ შეყვანილ სტრიქონში არსებობს სიტყვა "python", ჩაანაცვლეთ "Python"-ით.'''

str = input("Enter a string: ")

str1 = str.lower().strip()

if "python" in str1:
    print(str1.replace("python", "Python") + "\nPython")
else:
    print(str1 + "\nPython")

'''დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და 
აბრუნებს ახალ სტრიქონს, რომელიც შედგება შეყვანილი სტრიქონის პირველი ნახევრისაგან.'''

str = input("Enter a string: ")

print(str[0:len(str)//2])

'''დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს. string მოდულის გამოყენებით დაწერეთ შემოწმება.
 სტრიქონი ვალიდურია მაშინ, როდესაც ის შეიცავს ერთ ციფრს და არ არის დამატებითი სიმბოლოები ('!', '~', '#', '$' და ა.შ.)'''

import string
str = input("Enter a string: ")

symbols = string.punctuation
digits = string.digits
num_of_digits = 0
num_of_symbols = 0

for i in str:
    if i in digits:
        num_of_digits += 1

for i in str:
    if i in symbols:
        num_of_symbols +=1 


if num_of_symbols > 0 or num_of_digits != 1:
    print("The string is not valid")
else:
    print("The string is valid")


'''დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს, სტრიქონი გადაყავს ბაიტებში, 
ბეჭდავს მნიშვნელობას და შემდეგ კი გადაყავს ბაიტებიდან სტრიქონში და ბეჭდავს სტრიქონს.'''

import base64
str = input("Enter a string: ")

str_b = base64.b64encode(str.encode("utf-8"))
print(str_b)

str_decoded = base64.b64decode(str_b).decode("utf-8")

print(str_decoded)

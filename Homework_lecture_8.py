'''შექმენით გლობალური ცვლადი int_list = [10,20,30,40] და დაწერეთ პითონის ფუნქცია, რომელიც
მიიღებს რიცხვს პარამეტრად და გლობალურ int_list სიაში ჩაამატებს პარამეტრად მიღებულ რიცხვს.'''

int_list = [10, 20, 30, 40]

def add_list(n):
    int_list.append(n)
    
    return int_list
    


number = int(input("Enter a number: "))
print(add_list(number))


'''დაწერეთ პითნის ფუნქცია რომელიც პარამეტრად იღებს რიცხვების სიას (ლისტს) და აბრუნებს რიცხვების ჯამს.
პარამეტრად უნდა მიიღოს შემდეგი სია [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10].'''


list1 = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]

def sum_list(list):
    return sum(list)
    
print(sum_list(list1))


'''შექმენით გლობალური ცვლადი gl_str = "Global" დადაწერეთ პითონის ფუნქცია რომელიც
ქმნის ლოკალურ ცვლადს იგივე სახელით რაც გლობალურ ცვლადს აქვს (gl_str) და აბრუნებს ლოკალური ცვლადის მნიშვნელობას'''

gl_str = "Global"

def change_local():
    global gl_str
    gl_str = "Local"
    return gl_str

print(change_local())



'''რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს ერთ პარამეტრს number და დააბრუნებს ციფრების ჯამს
(მაგალითად თუ ფუნქციამ მიიღო რიცხვი 12345, უნდა დააბრუნოს 15. რადგან 1+2+3+4+5 უდრის 15-ს).'''

def sum_digits(number: int):
    
    if number < 10:
        return number
    else:
        return sum_digits(number // 10) + number % 10 
   
number = int(input("enter a number: "))
print(sum_digits(number))



'''რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად სტრიქონს
და დააბრუნებს მის შებრუნებულ (revers) სტრიქონს (მაგალითად input: Hello   Output: olleH)'''

def reverse(string):
    if len(string) <= 1:
        return string
    else:
        return reverse(string[1:]) + string[0]


string = input("Enter a string: ")
print(reverse(string))


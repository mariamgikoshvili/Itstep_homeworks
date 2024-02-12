
'''1. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n, და გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას.'''
def fib(n):
    fib_list = [0, 1]
    for i in fib_list:
        while len(fib_list) < n+1:
            x = fib_list[-2]
            y = fib_list[-1]
            z= x+y
            fib_list.append(z)
        return fib_list


n = int(input("Enter a number: "))            
print(fib(n))

'''დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად ორ სტრიქონს და შეამოწმებს არის თუ არა სტრიქონები ანაგრამები.
(ანაგრამი არის სიტყვა ან შესიტყვება, რომელიც წარმოიქმნება სხვა სიტყვის ან შესიტყვების ასოების გადაადგილებით). მაგ.: race და care ანაგრამებია.'''



def anagram_check(word_1, word_2):
    for i in word_1:
        if len(word_1) == len(word_2) and i in word_2:
            return f'These words are anagrams.'
        else:
            return f'These words are not anagrams.'
        
word_1 = input("Enter the first word: ")
word_2 = input("Enter the second word: ")        
    
print(anagram_check(word_1, word_2))

'''დაწერეთ პითონის ფუნქცია რომელიც მიიღებს n რიცხვს და დააბრუნებს მის ფაქტორიალს.'''


def factorial(number):
    fact = 1
    for i in range(n):
        fact *= (i+1)
    return fact

n = int(input("Enter a number: "))
print(factorial(n))


'''დაწერეთ პითნის ფუნქცია რომელიც მიიღებს ორ პარამეტრს, პირველს სტრიქონს და მეორეს სიმბოლოს.
ფუნქციამ უნდა მოძებნოს სტრიქონში რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს მისი რაოდენობა.'''



def symbol_finder(symbol, string):
    num = 0
    for i in string:
        if symbol == i:
            num += 1
    return f'The symbol "{symbol}" is {num} times in "{string}".'


string = input("enter a string: ")
symbol = input("Enter a symbol to find in word: ")
print(symbol_finder(symbol, string))



    
    
    
    







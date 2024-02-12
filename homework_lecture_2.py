''' 1. დაწერეთ პროგრამა რომელიც input მეთოდის 
საშუალებით მიიღებს 2 რიცხვს და დააბრუნებს ამ რიცხვებს შორის შესრულებული 
არითმეტიკული ოპერაციების შედეგებს (მიმატება, გამოკლება, გამრავლება, გაყოფა, ახარისხება). '''


n1 = eval(input('First number: '))
n2 = eval(input('Second number: '))

print(f'{n1} + {n2} = {n1 + n2}')
print(f'{n1} - {n2} = {n1 - n2}')
print(f'{n1} * {n2} = {n1 * n2}')
print(f'{n1} / {n2} = {n1 / n2}')
print(f'{n1} ** {n2} = {n1 ** n2}')


'''2. დაწერეთ პროგრამა რომბის ფართობის გამოსათვლელად. მომხმარებელს კლავიატურის გამოყენებით შეაქვს ორი დიაგონალის სიგრძე.'''

d1 = eval(input("Enter the length of first diagonal: "))
d2 = eval(input("Enter the length of second diagonal: "))

area = (d1 * d2) / 2
print(f' The area of rhombus is {area}.')

'''3. მომხმარებელის შეაქვს მეტრების რაოდენობა. დაბეჭდეთ შესაბამისი 
მნიშვნელობა სანტიმეტრებში, დეციმეტრებში, მილიმეტრებში, მილში.'''

metres = eval(input("Enter the value of metres: "))
cm = metres * 100
dm = metres * 10
milimetres = metres * 1000
miles = metres * 0.000621

print(f'{metres} metres is {cm} centimetres.')
print(f'{metres} metres is {dm} decimetres.')
print(f'{metres} metres is {milimetres} milimetres.')
print(f'{metres} metres is {miles} miles.')

'''4. დაწერეთ პროგრამა, რომელიც ითვლის სამკუთხედის ფართობს.
 მომხმარებელს კონსოლიდან შეყავს სამკუთხედის სიმაღლისა და ფუძის მნიშვნელობა.'''

height = eval(input("Enter the height of a triangle: "))
base = eval(input("Enter the base of a triangle: "))

area_triangle = (height * base) / 2

print(f'Area of the traingle is {area_triangle}.')
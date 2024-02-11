'''. 1 შექმენით პითონის კლასი Car, ატრიბუტებით ბრენდით, 
მოდელით და წლით. ასევე, შექმენით კლასის მეთოდი car_info(), რომელიც დაბეჭდავს ატრიბუტების ინფორმაციას.'''

class Car:
    number_of_cars = 0
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        '''4. დაამატეთ Car კლასს ატრიბუტი number_of_cars, 
        რომელიც დაითვლის მანქანების სრულ რაოდენობას. გაზარდეთ ეს ცვლადი ყოველ ჯერზე, მანქანის შექმნისას. '''
        Car.number_of_cars += 1
        
    def car_info(self):
        print(f'{self.brand}, {self.model}, {self.year}')

    '''5. Car კლასს დაამატეთ მეთოდი total_cars(), რომელიც გამოიტანს მანქანების მთლიან რაოდენობას.'''
    def  total_cars(self):
        print(Car.number_of_cars)
    
    '''2. Car კლასში დაამატეთ მეთოდი age_of_car, რომელიც დაითვლის მანქანის ასაკს.'''
    def age_of_car(self):
        age = 2024 - self.year
        print(age)

'''3. შექმენით კლასი ElectricCar, რომელიც მემკვიდრეობით მიიღებს Car class-ს. დაამატეთ ახალი ატრიბუტი battery_life და 
მეთოდი battery_info(), რომელიც დაბეჭდავს შემდეგ სტრიქონს "ამ მანქანის ბატარეის ხანგრძლივობა არის [battery_life] საათი".'''

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life

    def battery_info(self):
        print(f'Battery duration of this car is {self.battery_life}')

car1 = Car("Nissan", "Juke", 2013)
car2 = Car("Toyota", "Prius", 2006)
car1.car_info()
car1.age_of_car()
car2.car_info()
car2.age_of_car()
car1.total_cars()
car3 = ElectricCar("Nissan", "Juke", 2013, 15)
car3.battery_info()
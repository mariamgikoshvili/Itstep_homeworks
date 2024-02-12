'''დაწერეთ პითნის პროგრამა, რომელიც გააგზავნის მოთხოვნას requests-მოდულის გამოყენებით "https://fakestoreapi.com/products"
 მისამართზე, შეამოწმებს სტატუს და გადაიყვანს მიღებულ სიას, პითონის ლისტად და შეასრულეთ შემდეგი მოქმედებები:'''

import requests

def get_products():
  try:
    url = "https://fakestoreapi.com/products"

    response = requests.get(url)

    if response.status_code == 200:
      return response.json()
  except requests.exceptions.HTTPError as err:
    print("Http error: {err}")
  except requests.exceptions.ConnectionError as con_err:
    print(f"Connection error: {con_err}")
  except Exception as err:
    print(f"Somethin g wrong error: {err}")

print(get_products())

'''ა) შექმენით პროდუქტის ფასების სია და გამოიტანეთ როგორც მაქსიმალური ასევე მინიმალური და სასშუალო ფასები'''

def prices():
  products = get_products()
  price_list = []
  for product in products:
    price_list.append(product['price'])
    max_price = max(price_list)
    min_price = min(price_list)
    avg_price = sum(price_list)/len(price_list)

  print(f'Maximum price is {max_price}')
  print(f'Minimum price is {min_price}')
  print(f'Average price is {avg_price}')

prices()

'''ბ) შექმენით კატეგორიების სია (დუბლიკაციების გარეშე) და დაასორტირეთ'''
def categories():
  products = get_products()
  cat_list = []
  for product in products:
    cat_list.append(product['category'])
    cat_list = set(cat_list)
    
  cat_list.sort() 
  print(cat_list)

categories()

'''გ) შექმენით სია რომელშიც გექნებად პროდუქტის აღწერა (title) და id. დაასორტირეთ შედეგი title-ის მიხედვით'''
def descr():
  products = get_products()
  description = []

  for product in products:
    dict = {}
    dict['title'] = product['title']
    dict['id'] = product['id']
    description.append(dict)
  description = sorted(description, key=lambda x: x['title'])
  print(description)

descr()


'''დ) შემქენით რეიტინგების სია რომელიც იქნება დასორტირებული ("rate"-ის მიხედვით) ზრდადობით'''

def rates():
  products = get_products()
  rate_list = []
  for product in products:
    rate_list.append(product['rating']['rate'])
  rate_list.sort()
  print(rate_list)

rates()

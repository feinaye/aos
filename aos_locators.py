from faker import Faker
import random
fake = Faker(locale='en_CA')

app = 'AOS'
aos_homepage_url = 'https://advantageonlineshopping.com/#/'
aos_homepage_title = '\xa0Advantage Shopping'

first_name = '2369'+fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
username = f'{first_name}'[:15]
password = fake.password()
email = f'{username}@{fake.free_email_domain()}'
phone = fake.phone_number()[:14]
country = fake.current_country()
city = fake.city()
address = fake.street_address().replace("\n", " ")[:50]
state = fake.province()[:10]
postalcode = fake.postalcode()
description = f'User added by {username} via Python Selenium Automated Script'
aos_select_product_url = 'https://advantageonlineshopping.com/#/product/3'
aos_order_payment_url = 'https://advantageonlineshopping.com/#/orderPayment'
safepay_username = f'{first_name}fake.number()'[:12]
safepay_password = 'SPay_1236'

color = ['BLUE', 'BLACK', 'GREY', 'DARK BLUE', 'RED', 'YELLOW']
quantity = [1, 2, 3]
aos_order_date = fake.date()

print(f'{username}')
print(f'{full_name}')
print(f'{password}')
print(f'{aos_order_date}')
print(f'{safepay_password}')




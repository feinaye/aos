from faker import Faker
import random
fake = Faker(locale='en_CA')

app = 'AOS'
aos_homepage_url = 'https://advantageonlineshopping.com/#/'
aos_homepage_title = '\xa0Advantage Shopping'

first_name = fake.first_name()
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
categoryListboxContactUs = ['Laptops', 'Headphones', 'Tablets', 'Speakers', 'Mice']
I = len(categoryListboxContactUs)
productListboxContactUs = ['HP Chromebook 14 G1(ENERGY STAR', 'HP Chromebook 14 G1(ES)', 'HP ENVY - 17t Touch Laptop',
                           'HP ENVY X360 - 15t Laptop', 'HP Pavilion 15t Touch Laptop', 'HP Pavilion 15z Laptop', 'HP Pavilion 15z Touch Laptop'
                           'HP Pavilion x360 -11t Touch Laptop', 'HP Spectre x360 -13-4102dx', 'HP Stream - 11 -do20nr Laptop', 'HP ZBook 17 G2 Mobile Workstation']
value = random.choice(productListboxContactUs)
description = f'User added by {username} via Python Selenium Automated Script'
AOS_select_product_url = 'https://advantageonlineshopping.com/#/product/3'
AOS_order_payment_url = 'https://advantageonlineshopping.com/#/orderPayment'
safepay_username = f'{first_name}+fake.number()'[:12]
safepay_password = f'{first_name}{password}'[:10]
AOS_order_quantity = [1, 2, 3]
AOS_order_number = random.randint(6660000000, 6669999999)
AOS_order_total = random.uniform(0, 5000)
AOS_tracking_number = random.randint(6668000000, 6668999999)
AOS_order_date = fake.date()

print(f'{username}')
print(f'{password}')
print(f'{AOS_order_number}')
print(f'{AOS_tracking_number}')
print(f'{AOS_order_date}')



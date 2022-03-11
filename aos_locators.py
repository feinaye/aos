from faker import Faker
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

print(f'{username}')
print(f'{password}')



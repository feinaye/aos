import datetime
from time import sleep
import aos_locators as locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver  # import selenium to the file


driver = webdriver.Chrome('../chromedriver.exe')

print('.........................Data.......................')

def set_up():

    driver.maximize_window()

    driver.implicitly_wait(30)

    driver.get(locators.aos_homepage_url)

    print(driver.title)

    print(driver.current_url)

    if driver.current_url == locators.aos_homepage_url and driver.title == locators.aos_homepage_title:

        print('Advantage Online Shopping App Launched Successfully!')

        print(' ')

        print(f'Advantage Online Shopping URL: , {driver.current_url}')

        print(f'Advantage Online Shopping Homepage Title: {driver.title}')

        # Check if the url and home page title are displayed as expected.
        sleep(2)

    else:

        print('AOS APP is not launched')

        print(f'-----The current URL is {driver.current_url}')

        print(f'-----The current title is {driver.title}')

        sleep(2)


def create_new_account():
    if driver.current_url == locators.aos_homepage_url:
        sleep(2)

        driver.find_element(By.ID, 'menuUser').click()
        sleep(2)

        driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
        sleep(0.5)

        print('We are on the "CREATE ACCOUNT" page.')
        sleep(0.25)

        driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.username)
        sleep(0.5)

        driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
        sleep(0.25)

        driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.password)
        sleep(0.25)

        driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.password)
        sleep(0.25)

        print('Account Details completed. ')

        driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
        sleep(0.25)

        driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
        sleep(0.25)

        driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone)
        sleep(0.25)

        Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text('Canada')
        sleep(0.25)

        driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)

        sleep(0.25)

        driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
        sleep(0.25)

        driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.state)
        sleep(0.25)

        driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postalcode)
        sleep(0.25)

        print('Personal Details completed.')

        x = driver.find_element(By.NAME, 'i_agree').is_selected()

        if x is False:

            driver.find_element(By.NAME, 'i_agree').click()
            sleep(0.5)

        else:
            print('Something is wrong with your registration.')
            sleep(0.25)

        driver.find_element(By.ID, 'register_btnundefined').click()
        sleep(0.25)

        print(f'The registered username is: {locators.username}; the password is: {locators.password}')
        sleep(2)

    else:
        print('Something went wrong with create a new account. Please check your codes and try again.')
        sleep(2)


def sign_out():

    if driver.current_url == locators.aos_homepage_url:
        sleep(2)

        assert driver.find_element(By.LINK_TEXT, locators.username).is_displayed()
        sleep(0.5)

        driver.find_element(By.LINK_TEXT, locators.username).click()
        sleep(0.5)

        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"Sign out")]').click()
        sleep(0.5)

        print('Ordering products has been finished. Now we Logged out our account.')
        sleep(2)

    else:
        print("Something is wrong with sign out. Please check your codes and try again.")
        sleep(2)


def log_in():

    if driver.current_url == locators.aos_homepage_url:
        sleep(2)

        driver.find_element(By.ID, 'menuUser').click()
        sleep(0.5)

        driver.find_element(By.NAME, 'username').send_keys(locators.username)
        sleep(0.5)

        driver.find_element(By.NAME, 'password').send_keys(locators.password)
        sleep(0.5)

        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(0.5)

        driver.find_element(By.ID, 'menuUserLink').is_displayed()
        sleep(0.5)

        print('New user successfully logged in.')
        sleep(2)

    else:
        print("Something is wrong with log in. Please check your codes and try again.")
        sleep(2)


def tear_down():

    if driver is not None:

        print('--------------------$$$$$$--------------------')

        print(f'The test finished at: {datetime.datetime.now()}')

        sleep(2)

        driver.close()

        driver.quit()


# set_up()
# create_new_account()
# sign_out()
# log_in()
# tear_down()
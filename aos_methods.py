import datetime
from time import sleep
import aos_locators as locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium import webdriver

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


def validate_homepage():
    if driver.current_url == locators.aos_homepage_url and driver.title == locators.aos_homepage_title:
        sleep(2)

        # 1. Check that SPEAKERS, TABLETS, HEADPHONES, LAPTOPS, MICE texts are displayed.
        driver.find_element(By.ID, 'speakersTxt').is_displayed()
        sleep(0.25)

        driver.find_element(By.ID, 'tabletsTxt').is_displayed()
        sleep(0.25)

        driver.find_element(By.ID, 'laptopsTxt').is_displayed()
        sleep(0.25)

        driver.find_element(By.ID, 'miceTxt').is_displayed()
        sleep(0.25)

        driver.find_element(By.ID, 'headphonesTxt').is_displayed()
        sleep(0.25)

        print('The texts of SPEAKERS, TABLETS, HEADPHONES, LAPTOPS, MICE are displayed.')
        sleep(1)

    else:
        print('Something is wrong with homepage texts. Please check your codes and try again.')
        sleep(1)

    # 2. Click if the links of SPECIAL OFFER, POPULAR ITEMS and CONTACT US at the top nav menu are clickable.
    if driver.current_url == locators.aos_homepage_url:
        sleep(1)

        driver.find_element(By.LINK_TEXT, 'OUR PRODUCTS').click()
        sleep(0.25)

        driver.find_element(By.LINK_TEXT, 'SPECIAL OFFER').click()
        sleep(0.25)

        driver.find_element(By.LINK_TEXT, 'POPULAR ITEMS').click()
        sleep(0.25)

        print('The links for SPECIAL OFFER, POPULAR ITEMS and CONTACT US at the top nav menu are clickable.')
        sleep(1)

    else:
        print('Something is wrong with top navigation menu links. Please check your codes and try again.')
        sleep(1)

    # 3. Check if the main logo is displayed.
    if driver.current_url == locators.aos_homepage_url:
        sleep(2)

        driver.find_element(By.XPATH, '/html/body/header/nav/div/a/span[1][contains(., "dvantage")]').is_displayed()
        sleep(0.25)

        driver.find_element(By.XPATH, '/html/body/header/nav/div/a/span[2][contains(.,"DEMO")]').is_displayed()
        sleep(0.25)

        print('The main logo of Advantage Online Shopping application is displayed.')
        sleep(1)

    else:
        print('Something is wrong with the display of main logo. Please check your codes and try again.')
        sleep(1)

    # 4. Check if the CONTACT US form works properly.
    if driver.current_url == locators.aos_homepage_url:
        sleep(2)

        driver.find_element(By.XPATH, '//*[@id="supportCover"][contains(., "CONTACT US")]').is_displayed()
        sleep(1)

        driver.find_element(By.NAME, 'chat_with_us').is_displayed()
        sleep(1)

        driver.find_element(By.NAME, 'categoryListboxContactUs').click()
        sleep(1)

        driver.find_element(By.NAME, 'productListboxContactUs').click()
        sleep(1)

        driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.email)
        sleep(1)

        driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.description)
        sleep(2)

        driver.find_element(By.ID, 'send_btnundefined').is_enabled()
        sleep(1)

        driver.find_element(By.ID, 'send_btnundefined').click()
        sleep(1)

        driver.find_element(By.XPATH, '//p[contains(., "Thank you for contacting Advantage support.")]').is_displayed()
        sleep(1)


        print('CONTACT US form works properly. "Thank you for contacting Advantage support" confirmation is displayed.')
        sleep(1)

    else:
        print('CONTACT US is not successful. Please check your information and try again.')
        sleep(0.25)

    if driver.find_element(By.LINK_TEXT, 'CONTINUE SHOPPING').is_displayed():
        sleep(1)

        driver.find_element(By.LINK_TEXT, 'CONTINUE SHOPPING').is_enabled()
        sleep(1)

        print('CONTINUE SHOPPING is displayed and clickable.')
        sleep(1)

    else:
        print('CONTINUE SHOPPING is not displayed and not clickable.')
        sleep(1)

    # 5. Check out if FOLLOW US section works properly.
    if driver.current_url == locators.aos_homepage_url:
        sleep(2)

        driver.find_element(By.XPATH, '/html/body/div[3]/footer/div/h3[contains(., "FOLLOW US")]')
        sleep(1)

        driver.find_element(By.NAME, 'follow_facebook').is_displayed()
        sleep(1)

        driver.find_element(By.NAME, 'follow_facebook').is_enabled()
        sleep(1)

        driver.find_element(By.NAME, 'follow_twitter').is_displayed()
        sleep(1)

        driver.find_element(By.NAME, 'follow_twitter').is_enabled()
        sleep(1)

        driver.find_element(By.NAME, 'follow_linkedin').is_displayed()
        sleep(0.25)

        driver.find_element(By.NAME, 'follow_linkedin').is_enabled()
        sleep(1)

        print('FOLLOW US Section works properly.')
        sleep(2)

    else:
        print('FOLLOW US Section does not work properly, something is wrong with it. Please check and try again.')
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

        driver.find_element(By.NAME, 'countryListboxRegisterPage').send_keys('Canada')
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

        driver.find_element(By.ID, 'menuUserLink').is_displayed()
        print('Creating new account is successful, validated by username appears on the homepage.')


def sign_out():

    if driver.current_url == locators.aos_homepage_url:
        sleep(2)

        assert driver.find_element(By.ID, 'menuUser').is_displayed()
        sleep(0.5)

        driver.find_element(By.ID, 'menuUser').click()
        sleep(0.5)

        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3][contains(.,"Sign out")]').click()
        sleep(2)

        print('Ordering products has been finished. Now we Logged out our account.')
        sleep(1)

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

        driver.find_element(By.XPATH, '//button[contains(., "SIGN IN")]').click()
        sleep(0.5)

        driver.find_element(By.ID, 'menuUserLink').is_displayed()
        sleep(0.5)

        print('New user successfully logged in.')
        sleep(2)

    else:
        print("Something is wrong with log in. Please check your codes and try again.")
        sleep(2)


def checkout_shopping_cart():

    driver.find_element(By.XPATH, '//span[contains(., "EXPLORE THE NEW DESIGN")]').is_selected()
    sleep(1)

    driver.find_element(By.XPATH, '//button[contains(., "see_offer_btn)"]').click()
    sleep(2)

    if driver.current_url == locators.aos_select_product_url:
        sleep(1)
        print('We are on the right place for shopping.')
        sleep(0.25)

        driver.find_element(By.XPATH, '//span[contains(., "YELLOW")]')
        sleep(0.25)

        driver.find_element(By.XPATH, '//label[contains(., "Quantity:")]').send_keys(locators.AOS_order_quantity[0])
        sleep(0.25)

        driver.find_element(By.NAME, 'save_to_cart').click()
        sleep(1)

        driver.find_element(By.ID, 'menuCart').is_displayed()
        sleep(0.25)

        driver.find_element(By.ID, 'checkOutPopUp').click()
        sleep(2)

        if driver.current_url == locators.aos_order_payment_url:
            sleep(1)

            driver.find_element(By.XPATH, '//label[contains(., "1. SHIPPING DETAILS ")]').is_displayed()
            sleep(0.25)

            driver.find_element(By.XPATH, '//label[contains(., "full_name")]').is_displayed()
            sleep(2)

            print('We are on Order Payment page.')
            sleep(0.25)

            driver.find_element(By.XPATH, '//h5[contains(., " ORDER SUMMARY")]').is_displayed()
            sleep(1)

            driver.find_element(By.ID, 'next_btn').click()
            sleep(2)

            driver.find_element(By.NAME, 'safepay').is_selected()
            sleep(1)

            driver.find_element(By.NAME, 'safepay_username').send_keys(locators.safepay_username)
            sleep(1)

            driver.find_element(By.NAME, 'safepay_password').send_keys(locators.safepay_password)
            sleep(1)

            driver.find_element(By.ID, 'pay_now_btn_SAFEPAY').click()
            sleep(2)

            assert(driver.find_element(By.XPATH, '//span[contains(., "Thank_you_for_buying_with_Advantage")]')).is_displayed()
            sleep(1)

            driver.find_element(By.XPATH, '//label[contains(., "locators.AOS_order_number")]').is_displayed()
            sleep(0.25)

            driver.find_element(By.XPATH, '//label[contains(., "locators.AOS_tracking_number")]').is_displayed()
            sleep(0.25)

            driver.find_element(By.XPATH, '//label[contains(., "locators.full_name")]').is_displayed()
            sleep(0.25)

            driver.find_element(By.XPATH, '//label[contains(., "locators.address")]').is_displayed()
            sleep(0.25)

            driver.find_element(By.XPATH, '//label[contains(., "locators.phone")]').is_displayed()
            sleep(0.25)

            driver.find_element(By.XPATH, '//a[contains(., "locators.aos_order_date")]').is_displayed()
            sleep(0.25)

            driver.find_element(By.XPATH, '//span[contains(., "locators.username")]').click()
            sleep(1)

            driver.find_element(By.LINK_TEXT, 'My orders').click()
            sleep(2)

            driver.find_element(By.XPATH, '//label[contains(., "locators.AOS_order_number")]').is_displayed()
            sleep(0.25)

            driver.find_element(By.XPATH, '//span[contains(., "locators.username")]').click()
            sleep(1)

            driver.find_element(By.LINK_TEXT, 'Sign out').click()
            sleep(0.5)

            print('Your ordering and checking out is successful!')
            sleep(0.25)

        else:
            print('Your payment is not successful. Please check and pay again.')
            sleep(1)


def delete_account():
    if driver.current_url == locators.aos_homepage_url:
        sleep(2)

        driver.find_element(By.XPATH, '//span[contains(., "username")]').is_displayed()
        sleep(0.25)

        driver.find_element(By.XPATH, '//span[contains(., "locators_username")]').click()
        sleep(1)

        driver.find_element(By.LINK_TEXT, 'My orders').is_selected()
        sleep(1)

        driver.find_element(By.LINK_TEXT, 'My orders').click()
        sleep(1)

        driver.find_element(By.XPATH, '//label[contains(., " - No orders - ")]').is_displayed()
        sleep(1)

        driver.find_element(By.XPATH, '//span[contains(., "locators_username")]').click()
        sleep(1)

        driver.find_element(By.LINK_TEXT, 'My account').click()
        sleep(1)

        driver.find_element(By.XPATH, '//label[contains(., "locators.full_name")]').is_displayed()
        sleep(1)

        driver.find_element(By.XPATH, '//div[contains(., "Delete Account")]').click()
        sleep(1)

        driver.find_element(By.ID, 'menuUser').click()
        sleep(2)

        driver.find_element(By.ID, 'menuUser').click()
        sleep(2)

        driver.find_element(By.NAME, 'username').send_keys(locators.username)
        sleep(1)

        driver.find_element(By.NAME, 'password').send_keys(locators.password)
        sleep(0.25)

        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(1)

        driver.find_element(By.XPATH, '//label[contains(., ("Incorrect user name or password."))]').is_displayed()
        sleep(1)

        print('User name or password is deleted, please create a new account and try logining again.')
        sleep(1)


def tear_down():

    if driver is not None:

        print('--------------------$$$$$$--------------------')

        print(f'The test finished at: {datetime.datetime.now()}')

        sleep(2)

        driver.close()

        driver.quit()


set_up()
validate_homepage()
create_new_account()
sign_out()
log_in()
# delete_account()
# checkout_shopping_cart()
tear_down()
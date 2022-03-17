import sys
import datetime
from time import sleep
import aos_locators as locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium import webdriver



options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

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
# 1. Check that SPEAKERS, TABLETS, HEADPHONES, LAPTOPS, MICE texts are displayed.
    assert driver.find_element(By.ID, 'speakersTxt').is_displayed()
    print('SPEAKERS text is displayed.')
    sleep(0.25)

    assert driver.find_element(By.ID, 'tabletsTxt').is_displayed()
    print('TABLETS text is displayed.')
    sleep(0.25)

    assert driver.find_element(By.ID, 'laptopsTxt').is_displayed()
    print('LAPTOPS text is displayed')
    sleep(0.25)

    assert driver.find_element(By.ID, 'miceTxt').is_displayed()
    print('MICE text is displayed.')
    sleep(0.25)

    assert driver.find_element(By.ID, 'headphonesTxt').is_displayed()
    print('HEADPHONES text is displayed.')
    sleep(0.25)

    print('The texts of SPEAKERS, TABLETS, HEADPHONES, LAPTOPS, MICE are all displayed.')
    sleep(1)

# 2. Click if the links of SPECIAL OFFER, POPULAR ITEMS and CONTACT US at the top nav menu are clickable.
    driver.find_element(By.LINK_TEXT, 'OUR PRODUCTS').click()
    sleep(0.25)

    driver.find_element(By.LINK_TEXT, 'SPECIAL OFFER').click()
    sleep(0.25)

    driver.find_element(By.LINK_TEXT, 'POPULAR ITEMS').click()
    sleep(0.25)

    print('The links for SPECIAL OFFER, POPULAR ITEMS and CONTACT US at the top nav menu are all clickable.')
    sleep(1)

# 3. Check if the main logo is displayed.
    driver.find_element(By.XPATH, '/html/body/header/nav/div/a/span[1][contains(., "dvantage")]').is_displayed()
    sleep(0.25)

    driver.find_element(By.XPATH, '/html/body/header/nav/div/a/span[2][contains(.,"DEMO")]').is_displayed()
    sleep(0.25)

    print('The main logo of Advantage Online Shopping application is displayed.')
    sleep(1)

# 4. Check if the CONTACT US form works properly.
    sleep(1)
    Select(driver.find_element(By.NAME, 'categoryListboxContactUs')).select_by_visible_text('Laptops')
    sleep(1)

    Select(driver.find_element(By.NAME, 'productListboxContactUs')).select_by_index(2)
    sleep(1)

    driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.email)
    sleep(1)

    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.description)
    sleep(2)

    driver.find_element(By.ID, 'send_btnundefined').is_enabled()
    sleep(1)

    driver.find_element(By.ID, 'send_btnundefined').click()
    sleep(0.5)

    assert driver.find_element(By.XPATH, '//p[contains(., "Thank you for contacting Advantage support.")]')
    sleep(0.25)

    print('CONTACT US form works properly. "Thank you for contacting Advantage support" confirmation is displayed.')
    sleep(1)

    if driver.find_element(By.LINK_TEXT, 'CONTINUE SHOPPING').is_enabled():
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

        driver.find_element(By.NAME, 'follow_facebook').is_enabled()
        sleep(1)

        driver.find_element(By.NAME, 'follow_twitter').is_enabled()
        sleep(1)

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

        Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).\
            select_by_visible_text('Canada')
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
        sleep(0.25)

        driver.find_element(By.ID, 'menuUser').click()
        sleep(0.25)

        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3][contains(.,"Sign out")]').click()
        sleep(0.25)

        print('Ordering products has been finished. Now we Logged out our account.')
        sleep(0.25)

    else:
        print("Something is wrong with sign out. Please check your codes and try again.")
        sleep(0.25)


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
    driver.find_element(By.ID, 'see_offer_btn').click()
    sleep(2)

    if driver.current_url == locators.aos_select_product_url:
        sleep(1)
        print('You are on the right place for shopping.')
        sleep(0.25)

        driver.find_element(By.NAME, 'save_to_cart').click()
        sleep(1)

        driver.find_element(By.ID, 'checkOutPopUp').click()
        sleep(2)

        if driver.current_url == locators.aos_order_payment_url:
            sleep(1)

            assert driver.find_element(By.XPATH, '//label[contains(., "1. SHIPPING DETAILS ")]').is_displayed()
            sleep(0.5)

            if driver.find_element(By.XPATH, f'//div[contains(., "{locators.full_name}")]').is_displayed():
                print(f'------{locators.full_name} is found! ------')

            if driver.find_element(By.XPATH, f'//h5[contains(., "ORDER SUMMARY")]').is_displayed():
                print('Order Summary is displayed.')
                sleep(1)

                driver.find_element(By.ID, 'next_btn').click()
                sleep(1)

                driver.find_element(By.NAME, 'safepay').is_selected()
                sleep(1)

                driver.find_element(By.NAME, 'safepay_username').send_keys(locators.safepay_username)
                sleep(1)

                driver.find_element(By.NAME, 'safepay_password').send_keys(locators.safepay_password)
                sleep(1)

                driver.find_element(By.ID, 'pay_now_btn_SAFEPAY').click()
                sleep(2)

                assert driver.find_element(By.ID, 'orderPaymentSuccess')

                orders = driver.find_element(By.ID, 'orderPaymentSuccess').text
                print(orders)

                if driver.find_element(By.XPATH, f'//span[contains(., "{locators.username}")]').is_displayed():
                    sleep(1)
                    print('')


                driver.find_element(By.ID, 'menuUser').click()

                driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3][contains(.,"Sign out")]').click()
                sleep(2)

                print('Your ordering and checking out is successful!')
                sleep(0.25)

            else:
                print('Your payment is not successful. Please check and pay again.')
                sleep(1)


def delete_account():
    driver.find_element(By.XPATH, f'//a/span[contains(., "{locators.username}")]').click()
    sleep(1)

    driver.find_element(By.XPATH, '/html/body[contains(., "My orders")]').click()
    sleep(0.25)

    assert driver.find_element(By.XPATH, '//div/label[contains(., "No orders")]').is_displayed()
    sleep(0.25)
    print(f'No order is displayed.')

    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(0.25)

    driver.find_element(By.XPATH, '//a/div/label[contains(., "My account"]').click()
    print('')
    sleep(0.5)

    assert driver.find_element(By.XPATH, 'f//*[contains(., "{locators.full_name}")]').is_displayed()
    print(f'User full name has displayed.')
    sleep(1)

    driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
    sleep(2)

    driver.find_element(By.XPATH, '//div[@class="deletePopupBtn deleteRed"]').click()

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


# set_up()
# validate_homepage()
# create_new_account()
# sign_out()
# log_in()
# checkout_shopping_cart()
# tear_down()
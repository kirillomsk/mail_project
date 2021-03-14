import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome("chromedriver")
    yield driver
    driver.quit()


url = 'https://mail.ru/'
login_data = {'login': 'testname',
              'domain': '@internet.ru',
              'password': 'test1012000'}
message_theme = 'some theme'
recipient = 'kirill.omsk11@gmail.com'

login_locator = (By.CSS_SELECTOR, 'div.email-input-container > input')
select_domain_locator = 'div.select-wrapper.svelte-1eyrl7y > select'
button_password_locator = (By.CSS_SELECTOR, 'button.button.svelte-1eyrl7y')
password_locator = (By.CSS_SELECTOR, 'div.password-input-container.svelte-1eyrl7y > input')
login_button_locator = (By.CSS_SELECTOR, 'button.second-button.svelte-1eyrl7y')
write_message_button_locator = (By.CSS_SELECTOR, 'div.layout__column-wrapper > div > div > div > div:nth-child(1) > '
                                                 'div > div > a')
recipient_input_locator = (By.CSS_SELECTOR, 'label > div > div > input')
theme_input_locator = (By.CSS_SELECTOR, 'div.container--3QXHv > div > input')
message_input_locator = (By.XPATH, '/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[5]/div/div/div[2]/div[1]')
send_message_button_locator = (By.CSS_SELECTOR, 'span.button2.button2_base.button2_primary.button2_hover-support.js'
                                                '-shortcut')
f = open('./mail_tests/message.txt', encoding='utf-8')
message = f.read()
f.close()

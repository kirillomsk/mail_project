from page_mail import page


def test_mail(browser):
    login = page(browser)
    login.get_site()
    login.write_login()
    login.select_domain()
    login.click_password_button()
    password = page(browser)
    password.write_password()
    password.click_login_button()
    mail = page(browser)
    mail.click_write_message_button()
    mail.input_recipient()
    mail.input_theme()
    mail.input_message()
    mail.send_message()

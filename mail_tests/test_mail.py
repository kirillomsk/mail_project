from page_mail import page


def test_mail(browser):
    mail = page(browser)
    mail.get_site()
    mail.write_login()
    mail.select_domain()
    mail.click_password_button()
    mail.write_password()
    mail.click_login_button()
    mail.click_write_message_button()
    mail.input_recipient()
    mail.input_theme()
    mail.input_message()
    mail.send_message()

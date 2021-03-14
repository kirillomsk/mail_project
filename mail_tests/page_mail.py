from base_mail import base
import conftest


class page(base):
    def write_login(self):
        login_input = self.find_element(conftest.login_locator)
        login_input.clear()
        login_input.send_keys(conftest.login_data['login'])
        return login_input

    def select_domain(self):
        return self.select(conftest.select_domain_locator, conftest.login_data['domain'])

    def click_password_button(self):
        password_button = self.find_element(conftest.button_password_locator)
        password_button.click()
        return password_button

    def write_password(self):
        password_input = self.find_element(conftest.password_locator)
        password_input.send_keys(conftest.login_data['password'])
        return password_input

    def click_login_button(self):
        login_button = self.find_element(conftest.login_button_locator)
        login_button.click()
        return login_button

    def click_write_message_button(self):
        write_message_button = self.find_element(conftest.write_message_button_locator)
        write_message_button.click()
        return write_message_button

    def input_recipient(self):
        recipient = self.find_element(conftest.recipient_input_locator)
        recipient.clear()
        recipient.send_keys(conftest.recipient)
        return recipient

    def input_theme(self):
        theme = self.find_element(conftest.theme_input_locator)
        theme.clear()
        theme.send_keys(conftest.message_theme)
        return theme

    def input_message(self):
        message = self.find_xpath(conftest.message_input_locator)
        message.send_keys(conftest.message)
        return message

    def send_message(self):
        sender = self.find_element(conftest.send_message_button_locator)
        sender.click()
        return sender

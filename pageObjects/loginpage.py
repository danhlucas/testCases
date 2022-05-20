
class LoginPage():
    email_xpath = '//*[@id="identifierId"]'
    
    btn_login = '//*[@id="identifierNext"]/div/button/span'

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.email_xpath).send_keys(email)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.btn_login).click()
    

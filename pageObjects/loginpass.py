class LoginPass():
    pass_word_xpath = '//*[@id="password"]/div[1]/div/div[1]/input'

    btn_click_xpath = '//*[@id="passwordNext"]/div/button/span'

    def __init__(self, driver):
        self.driver = driver

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.pass_word_xpath).send_keys(password)

    def clickLoginPass(self):
        self.driver.find_element_by_xpath(self.btn_click_xpath).click()
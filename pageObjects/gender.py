class Gender():
    btn_click_gender = '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/c-wiz/div/div[3]/div/div/c-wiz/section/div[2]/div/div/div[4]/div[2]/a/div/div[2]/figure/span'

    def __init__(self, driver):
        self.driver = driver

    def clickGender(self):
        self.driver.find_element_by_xpath(self.btn_click_gender).click()
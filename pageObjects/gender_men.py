class GenderMen():
    btn_click_gender_men = '//*[@id="yDmH0d"]/c-wiz[3]/div/div[2]/div[2]/c-wiz/div/div[4]/div/div[2]/div[1]/div[2]/div/div'

    def __init__(self, driver):
        self.driver = driver

    def clickGenderMen(self):
        self.driver.find_element_by_xpath(self.btn_click_gender_men).click()
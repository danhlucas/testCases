class Profileder():
    btn_click_profileder = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/c-wiz/c-wiz/div/div[1]/div[3]/c-wiz/nav/ul/li[2]/a'

    def __init__(self, driver):
        self.driver = driver

    def clickProfileder(self):
        self.driver.find_element_by_xpath(self.btn_click_profileder).click()
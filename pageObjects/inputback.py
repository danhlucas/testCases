class InputBack():
    btn_click_inputback = '//*[@id="yDmH0d"]/c-wiz[3]/div/div[2]/div[1]/div[1]/div[1]/div[1]'

    def __init__(self, driver):
        self.driver = driver

    def clickInputBack(self):
        self.driver.find_element_by_xpath(self.btn_click_inputback).click()
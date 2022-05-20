import sys
import time

sys.path.append('E:\Kiểm thử phần mềm 1\PythonFinalTest1POM')
from pageObjects.gender_men import GenderMen

class testGenderMen():
    def __init__(self, driver):
        self.driver = driver
        self.test_gender_men = GenderMen(driver)

    def testGenderMen(self):
        
        self.test_gender_men.clickGenderMen()
        time.sleep(2)
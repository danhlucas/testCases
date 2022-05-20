import sys
import time

sys.path.append('E:\Kiểm thử phần mềm 1\PythonFinalTest1POM')
from pageObjects.gender import Gender

class testGender():
    def __init__(self, driver):
        self.driver = driver
        self.test_gender = Gender(driver)

    def testGender(self):
        time.sleep(2)
        self.test_gender.clickGender()
        time.sleep(2)
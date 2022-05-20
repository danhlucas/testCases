import sys
import time

sys.path.append('E:\Kiểm thử phần mềm 1\PythonFinalTest1POM')
from pageObjects.inputback import InputBack

class testInputBack():
    def __init__(self, driver):
        self.driver = driver
        self.test_inputback = InputBack(driver)

    def testInputBack(self):
        time.sleep(2)
        self.test_inputback.clickInputBack()
        time.sleep(2)
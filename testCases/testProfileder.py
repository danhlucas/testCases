import sys
import time

sys.path.append('E:\Kiểm thử phần mềm 1\PythonFinalTest1POM')
from pageObjects.profileder import Profileder

class testProfileder():
    def __init__(self, driver):
        self.driver = driver
        self.test_profileder = Profileder(driver)

    def testProfileder(self):
        time.sleep(2)
        self.test_profileder.clickProfileder()
        time.sleep(2)
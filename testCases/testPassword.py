import sys
import time

sys.path.append('E:\Kiểm thử phần mềm 1\PythonFinalTest1POM')

from pageObjects.loginpass import LoginPass

class testPass():
    value ='danhlucas3003'
    def __init__(self, driver):
        self.diver = driver
        self.login_pass = LoginPass(driver)

    def testLoginPass (self):
        self.login_pass.setPassword(self.value)
        time.sleep(2)
        self.login_pass.clickLoginPass()
        time.sleep(2)
       
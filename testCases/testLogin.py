
import sys
import time

sys.path.append('E:\Kiểm thử phần mềm 1\PythonFinalTest1POM')

from pageObjects.loginpage import LoginPage

class testLogin():

    value ='danh48467@donga.edu.vn'
    def __init__(self, driver):
        self.driver = driver
        self.Login = LoginPage(driver)
        

    def testLogin(self):
        self.Login.setEmail(self.value)
        time.sleep(2)
        self.Login.clickLogin()
        time.sleep(2)


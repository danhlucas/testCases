import time
import unittest
import HtmlTestRunner
from selenium import webdriver

import sys


sys.path.append('E:\Kiểm thử phần mềm 1\PythonFinalTest1POM')
from testCases.testLogin import testLogin
from testCases.testPassword import testPass
from testCases.testProfileder import testProfileder
from testCases.testGender import testGender
from testCases.testGenderMen import testGenderMen
from testCases.testInputBack import testInputBack

class MovieTest(unittest.TestCase):
    driver = webdriver.Chrome(executable_path="E:\\Kiểm thử phần mềm 1\\PythonFinalTest1POM\\drivers\\chromedriver.exe")
    baseURL = "https://accounts.google.com/signin"

    driver.get(baseURL)
    driver.maximize_window()
    time.sleep(2)

    def test_gmail(self):
        test_login = testLogin(self.driver)
        test_login.testLogin()
        time.sleep(1)
        test_pass = testPass(self.driver)
        test_pass.testLoginPass()
        time.sleep(1)
        test_profile = testProfileder(self.driver)
        test_profile.testProfileder()
        time.sleep(1)
        test_gender = testGender(self.driver)
        test_gender.testGender()
        time.sleep(1)
        test_gender_men = testGenderMen(self.driver)
        test_gender_men.testGenderMen()
        time.sleep(1)
        test_inputback = testInputBack(self.driver)
        test_inputback.testInputBack()

        time.sleep(5)



        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="reports"))
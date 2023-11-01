import time
import pytest
from pageObjects.LoginPage import LoginPage
from testCases.conftest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()


    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("********** Test_001_Login *************")
        self.logger.info("********** Verifying Home Page Title *************")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.logger.info("********** Home Page Title is Passed  *************")

        else:
            self.driver.save_screenshot("//home//mohammedsalahudeen//PycharmProjects//nopcommerceApp//Screenshots//test_homePageTitle.png")
            self.logger.error("********** Home Page Title is Failed *************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("********** Verifying Login Test *************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********** Login test is passed  *************")

        else:
            self.driver.save_screenshot("//home//mohammedsalahudeen//PycharmProjects//nopcommerceApp//Screenshots//test_login.png")
            self.logger.error("********** Login test  is Failed *************")
            assert False




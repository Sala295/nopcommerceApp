import time
import pytest
from pageObjects.LoginPage import LoginPage
from testCases.conftest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_Login():
    baseURL = ReadConfig.getApplicationURL()
    path = "/home/mohammedsalahudeen/PycharmProjects/nopcommerceApp/TestData/LoginData.xlsx"
    logger=LogGen.loggen()


    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("********** Test_002_DDT_login *************")
        self.logger.info("********** Verifying Login Test *************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp=LoginPage(self.driver)

        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows in Excel:",self.rows)
        list_status = []
        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password= XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title="Dashboard / nopCommerce administration"
            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("******Passed")
                    self.lp.clickLogout()
                    list_status.append("Passed")
                elif self.exp=="Fail":
                    self.logger.info("******Failed")
                    self.lp.clickLogout()
                    list_status.append("Failed")
            elif act_title != exp_title:
                if self.exp=="Pass":
                    self.logger.info("******Failed")
                    self.lp.clickLogout()
                    list_status.append("Failed")

                elif self.exp == 'Fail':
                    self.logger.info("***Passed***")
                    self.logger.info("****passed****")
                    list_status.append("Passed")

        if "Fail" not in list_status:
            self.logger.info("Login DDT is test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT is test failed")
            self.driver.close()
            assert False

        self.logger.info("******End of Login DDT Test**********")













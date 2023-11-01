import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class AddCustomer:
    # Add customer page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(.,'Customer')]"
    btnAddnew_xpath="//a[@class='btn btn-primary']"
    txtEmail_xpath="//input[@name='Email']"
    txtPassword_xpath="//input[@name='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@name='LastName']"
    rdMaleGender_id = "//*[@id='Gender_Male']"
    rdFemaleGender_id = "//*[@id='Gender_Female']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@name='Company']"
    txtcustomerRoles_xpath="//div[@class='input-group-append input-group-required']//div//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath="//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath="//li[contains(text(),'Registered')]"
    lstitemGuests_xpath="//li[contains(text(),'Guests')]"
    lstitemVendors_xpath="//li[contains(text(),'Vendors')]"
    drpmgrOfVendors_xpath="//select[@name='VendorId']"
    txtAdminContent_xpath="//textarea[@id='AdminComment']"
    btnSave_xpath="//button[@name='save']//i"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomerMenu(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.lnkCustomers_menu_xpath))).click()

    def clickOnCustomerMenuItem(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.lnkCustomers_menuitem_xpath))).click()

    def clickOnAddnew(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btnAddnew_xpath))).click()

    def setEmail(self,email):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.txtEmail_xpath))).send_keys(email)

    def setPassword(self,password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.txtPassword_xpath))).send_keys(password)

    def setCustomerRoles(self,role):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.txtcustomerRoles_xpath))).click()
        if role == 'Registered':
            self.listitem=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.lstitemRegistered_xpath)))
        elif role == 'Adminintrators':
            self.listitem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.lstitemAdministrators_xpath)))
        elif role == 'Guests':
            #here user can either be registered or guest but cannot be combo of both while selecting
            #Suppose you want to add Guests you have to delete Registered
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]"))).click()
            self.listitem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.lstitemGuests_xpath)))
        elif role == 'Registered':
            self.listitem=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.lstitemRegistered_xpath)))
        elif role == 'Vendors':
            self.listitem=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.lstitemVendors_xpath)))
        else:
            self.listitem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.lstitemGuests_xpath)))
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)


    def setManagerOfVendor(self,value):
        drp=Select(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.drpmgrOfVendors_xpath))))
        drp.select_by_visible_text(value)
        print("Selected vendor")

    def setGender(self,gender):
        if gender=='Male':
           WebDriverWait(self.driver,  10).until(EC.element_to_be_clickable((By.XPATH, self.rdMaleGender_id))).click()
           print("Selected Male button")
        elif gender=='Female':
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.rdFemaleGender_id))).click()
        else:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.rdMaleGender_id))).click()

    def setFirstName(self,fname):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.txtFirstName_xpath))).send_keys(fname)

    def setLasttName(self,lname):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.txtLastName_xpath))).send_keys(lname)

    def setDob(self,dob):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.txtDob_xpath))).send_keys(dob)

    def setCompanyName(self,compname):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.txtCompanyName_xpath))).send_keys(compname)

    def setAdminContent(self,content):
        print("Before selecting admin content")
        WebDriverWait(self.driver, 20,ignored_exceptions=[TimeoutException]).until(EC.presence_of_element_located((By.XPATH, self.txtAdminContent_xpath))).send_keys(content)
        print("After selecting admin content")
        time.sleep(5)

    def clickOnSave(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btnSave_xpath))).click()




from selenium import webdriver


def login(driver):
    # chrome_driver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
    # driver = webdriver.Chrome(executable_path=chrome_driver)
    driver.get('http://testsaasadmin.tonggangfw.net/#/user/login')
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.find_element_by_id('userName').click()
    driver.find_element_by_id('userName').send_keys('18825262465')
    driver.find_element_by_id('password').click()
    driver.find_element_by_id('password').send_keys('123456yhl')
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div[2]/div/form/div[3]/div/div/div/button').click()
    driver.implicitly_wait(2)


if __name__ == "__main__":
    login()

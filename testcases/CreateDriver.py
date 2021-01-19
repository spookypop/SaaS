import os
import random
from selenium import webdriver
import time
from common.Login import login
from common.IdCardGennerator import IdNumber



def main():
    chrome_driver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=chrome_driver)
    # 登录
    login(driver)
    time.sleep(3)
    print("我已登录")
    # 司机填写页面
    driver.get('http://testsaasadmin.tonggangfw.net/#/capacity/join-new?driver_id=undefined&type=new')
    # 司机手机号
    driver.find_element_by_id('cell').send_keys(str(random.randint(10020100001, 10020999999)))
    driver.find_element_by_id('biz_source').click()
    time.sleep(1)
    # 加入源是所属公司
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div/div[2]/div').click()
    # 加入源是个人，还是不要切换了，改了加入源，后面字段的路径都变了
    # driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div/div[1]/div').click()
    time.sleep(1)
    driver.find_element_by_id('area_id').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div[1]/div/div/div[1]/div').click()
    time.sleep(1)
    driver.find_element_by_id('county_id').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div[1]/div/div/div[1]/div').click()
    time.sleep(1)
    # 加入源是所属公司，选择公司
    driver.find_element_by_id('company_id').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[1]/div').click()
    time.sleep(1)
    driver.find_element_by_id('name').send_keys('小叶')
    driver.find_element_by_id('id_no').send_keys(IdNumber.generate_id())
    driver.find_element_by_id('id_valid_date').send_keys('2023-01-31')
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div[2]/div/div[2]/form/div[2]/div[1]/div/div[2]/div/div/div/span/div[1]/span/div/div/div/span').click()
    time.sleep(3)
    os.system(r"C:\Users\X1\Desktop\file.exe")
    time.sleep(3)
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div[2]/div/div[2]/form/div[2]/div[2]/div/div[2]/div/div/div/span/div[1]/span/div/div/div/span').click()
    time.sleep(3)
    os.system(r"C:\Users\X1\Desktop\file.exe")
    time.sleep(3)
    driver.find_element_by_id('lic_no').send_keys('12345678')
    time.sleep(1)
    driver.find_element_by_id('lic_class').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div/div/div/div[1]/div').click()
    driver.find_element_by_id('lic_valid_date').send_keys('2023-01-31')
    driver.find_element_by_id('lic_issue_date').send_keys('2021-01-05')
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div[3]/div/div[2]/form/div[2]/div/div/div[2]/div/div/div/span/div[1]/span/div/div/div/span').click()
    time.sleep(3)
    os.system(r"C:\Users\X1\Desktop\file.exe")
    time.sleep(3)
    driver.find_element_by_id('plate_no').send_keys('桂A' + str(random.randint(50000, 59999)))
    driver.find_element_by_xpath('//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div[4]/div/div[2]/form/div[1]/div[2]/div/div[2]/div/div/div/div/span[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[10]/div/div/div/div[2]/div[1]/div/div/div[1]/div').click()
    time.sleep(1)
    driver.find_element_by_id('owner').send_keys('个人')
    driver.find_element_by_id('owner_address').send_keys('车辆所有人地址')
    driver.find_element_by_id('fuel_id').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[11]/div/div/div/div[2]/div/div/div/div[1]/div').click()
    time.sleep(1)
    driver.find_element_by_id('brand_name').send_keys('宝马')
    driver.find_element_by_id('series_name').send_keys('M5')
    driver.find_element_by_id('property').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[12]/div/div/div/div[2]/div/div/div/div[1]/div').click()
    time.sleep(1)
    driver.find_element_by_id('seat_num').send_keys('5')
    driver.find_element_by_id('drive_distance').send_keys('500')
    driver.find_element_by_id('color').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[13]/div/div/div/div[2]/div[1]/div/div/div[1]/div').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div[4]/div/div[2]/form/div[2]/div[1]/div/div[2]/div/div/div/span/div[1]/span/div/div/div/span').click()
    time.sleep(3)
    os.system(r'C:\Users\X1\Desktop\file.exe')
    time.sleep(3)
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div[4]/div/div[2]/form/div[2]/div[2]/div/div[2]/div/div/div/span/div[1]/span/div/div/div/span').click()
    time.sleep(3)
    os.system(r'C:\Users\X1\Desktop\file.exe')
    time.sleep(3)
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div[4]/div/div[2]/form/div[2]/div[3]/div/div[2]/div/div/div/span/div[1]/span/div/div/div/span').click()
    time.sleep(3)
    os.system(r'C:\Users\X1\Desktop\file.exe')
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div[7]/div/div/button/span').click()
    time.sleep(2)
    company_url = 'http://testsaasadmin.tonggangfw.net/#/capacity/join'
    current_url = driver.current_url
    print("当前页面的url是：", current_url)
    assert current_url == company_url, '页面跳转错误'


if __name__ == '__main__':
    main()

import os
import random
from selenium import webdriver
import time
from common.Login import login


def main():
    chrome_driver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=chrome_driver)
    # 登录
    login(driver)
    time.sleep(5)
    print("我已登录")
    # 创建公司填写页面
    driver.get('http://testsaasadmin.tonggangfw.net/#/settings/company-new')
    driver.find_element_by_id('company_name').click()
    driver.find_element_by_id('company_name').send_keys('测试公司' + str(random.randint(1, 1000)))
    driver.find_element_by_id('agent_type').click()
    time.sleep(1)
    # 代理商类型是省级代理
    # driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div/div/div/div[1]/div').click()
    # 代理商类型是市级代理
    # driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div/div/div/div[2]/div').click()
    # 代理商类型是租赁公司
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div/div[3]/div').click()
    time.sleep(1)
    driver.find_element_by_id('area_id').click()
    time.sleep(1)
    # 测试数据合作城市选择北京市
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div[1]/div/div/div[1]/div').click()
    time.sleep(1)
    driver.find_element_by_id('cooperative_mode').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div/div/div[1]/div').click()
    time.sleep(1)
    driver.find_element_by_id('transport_mode').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[1]/div').click()
    time.sleep(1)
    driver.find_element_by_id('company_registered_address').send_keys('注册地址')
    driver.find_element_by_id('company_business_address').send_keys('办公地址')
    driver.find_element_by_id('registered_capital').send_keys('500')
    driver.find_element_by_id('driver_num').send_keys('1000')
    driver.find_element_by_id('car_num').send_keys('5000')
    driver.find_element_by_xpath('//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div/div[3]/button/span').click()
    time.sleep(2)
    # 跳转到资质信息填写页面
    driver.find_element_by_id('identifier_code').send_keys('111111111111111')
    driver.find_element_by_id('legal_name').send_keys('小叶')
    driver.find_element_by_id('legal_idno').send_keys('11010119940504393X')
    driver.find_element_by_id('legal_photo').send_keys('10029000001')
    driver.find_element_by_id('email').send_keys('a11@qq.com')
    # 文件上传
    driver.find_element_by_css_selector('#root > div > section > section > main > div > div.ant-pro-grid-content > div > div > div > div > div > div.ant-card.steps-content.ant-card-bordered > div > form > div:nth-child(7) > div.ant-col.ant-col-16.ant-form-item-control > div > div > div > span > div.ant-upload.ant-upload-drag.file-uploader > span > div > div > div > span').click()
    time.sleep(3)
    os.system(r"C:\Users\X1\Desktop\file.exe")
    time.sleep(3)
    driver.find_element_by_css_selector('#root > div > section > section > main > div > div.ant-pro-grid-content > div > div > div > div > div > div.ant-card.steps-content.ant-card-bordered > div > form > div:nth-child(8) > div.ant-col.ant-col-16.ant-form-item-control > div > div > div > span > div.ant-upload.ant-upload-drag.file-uploader > span > div > div > div > span').click()
    time.sleep(3)
    os.system(r"C:\Users\X1\Desktop\file.exe")
    driver.find_element_by_css_selector('#root > div > section > section > main > div > div.ant-pro-grid-content > div > div > div > div > div > div.ant-card.steps-content.ant-card-bordered > div > form > div:nth-child(9) > div.ant-col.ant-col-16.ant-form-item-control > div > div > div > span > div.ant-upload.ant-upload-drag.file-uploader > span > div > div > div > span').click()
    time.sleep(3)
    os.system(r"C:\Users\X1\Desktop\file.exe")
    time.sleep(2)
    driver.find_element_by_css_selector('#root > div > section > section > main > div > div.ant-pro-grid-content > div > div > div > div > div > div.steps-action > button.ant-btn.ant-btn-primary > span').click()
    # 跳转到银行卡信息填写页面
    time.sleep(2)
    driver.find_element_by_id('legal_area').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[1]/div/div/div[1]/div').click()
    time.sleep(1)
    driver.find_element_by_id('bank_name').send_keys('中国工商银行')
    driver.find_element_by_id('account_opening_branch').send_keys('车公庙支行')
    driver.find_element_by_id('bank_code').send_keys('00028000000158437')
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div/div[3]/button[2]/span').click()
    # 跳转到签约信息页面
    time.sleep(3)
    driver.find_element_by_id('broker_name').send_keys('小叶')
    driver.find_element_by_id('broker_phone').send_keys(str(random.randint(10020100001, 10020999999)))
    driver.find_element_by_id('broker_idno').send_keys('11010119940504393X')
    driver.find_element_by_id('broker_email').send_keys('abh' + str(random.randint(0, 1000)) + '@qq.com')
    driver.find_element_by_id('max_acount_num').send_keys('50')
    driver.find_element_by_id('cooperate_date').send_keys('')
    driver.find_element_by_id('cooperate_date').send_keys('2023-01-01')
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div/div[3]/button[2]/span').click()
    time.sleep(2)
    company_url = 'http://testsaasadmin.tonggangfw.net/#/settings/company'
    current_url = driver.current_url
    print("当前页面的url是：", current_url)
    assert current_url == company_url, '页面跳转错误'


if __name__ == '__main__':
    # 输入对接人手机号
    main()

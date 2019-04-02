from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from lib.browser import wait_for_page_load

mobile_emulation = {
    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 4.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/72.0.3626.105 Mobile Safari/535.19" }
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)


driver = webdriver.Chrome(chrome_options = chrome_options)
driver.implicitly_wait(3)
# driver = webdriver.Chrome()

driver.get('https://www.google.com/')
time.sleep(3)
driver.get('https://www.youtube.com/')
time.sleep(5)
driver.get('https://www.textnow.com/signup?redirectTo=/wireless')
time.sleep(1000)
#driver.refresh()

# driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/form/div[1]/div[1]/authv2-text-field/div/div/input').send_keys('test1122@test.com')
# driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/form/div[1]/div[2]/authv2-text-field/div/div/input').send_keys('test1234')
# time.sleep(2)
# iframe = driver.find_elements_by_tag_name('iframe')
# for i in iframe:
#     try:
#         driver.switch_to.frame(i)
#         driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[5]').click()
#         print('3')
#         time.sleep(3)
#         driver.switch_to.default_content()
#         iframe1 = driver.find_elements_by_tag_name('iframe')
#         for j in iframe1:
#             try:
#                 driver.switch_to.frame(j)
#                 driver.find_element_by_xpath('//*[@id="recaptcha-audio-button"]').click()
#                 print('4')
#                 break
#             except:
#                 driver.switch_to.default_content()
#         driver.switch_to.default_content()
#         break
#     except:
#         driver.switch_to.default_content()

# driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/form/div[2]/button/span').click()
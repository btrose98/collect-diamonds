from selenium import webdriver
import yaml, time

conf = yaml.load(open('loginDetails.yml'))

username = conf['coinmarketcap_user']['email']
password = conf['coinmarketcap_user']['password']

driver = webdriver.Chrome()

driver.get('https://coinmarketcap.com/account/my-diamonds/')
try:
    driver.find_element_by_css_selector('#__next > div > div.main-content > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div > div > div:nth-child(2) > div > div:nth-child(4) > div:nth-child(2) > div.sc-1snuar3-4.dCKehS > button').click()
    time.sleep(1)
    
    driver.find_element_by_css_selector('body > div.t8xka3-0.clxZon.modalOpened > div > div > div > div:nth-child(3) > input').send_keys(username)
    driver.find_element_by_css_selector('body > div.t8xka3-0.clxZon.modalOpened > div > div > div > div.sc-1htht4q-3.kHSKLo.last > div.sc-1srpo52-0.ciHfxX > input').send_keys(password)
    driver.find_element_by_css_selector('body > div.t8xka3-0.clxZon.modalOpened > div > div > div > div.sc-1htht4q-6.kUXNCx > button').click()
    time.sleep(1)

    driver.find_element_by_css_selector('#__next > div > div.main-content > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div > div > div:nth-child(2) > div > div:nth-child(4) > div:nth-child(2) > div.sc-1snuar3-4.dCKehS > button').click()

except:
    print('---- An error has occured while accessing the website. ----')

finally:
    exit()
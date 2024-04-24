import time
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

conf = yaml.safe_load(open('loginDetails.yml'))

username = conf['coinmarketcap_user']['email']
password = conf['coinmarketcap_user']['password']

driver = webdriver.Chrome()

driver.get('https://coinmarketcap.com/account/my-diamonds/')
try:
    login_button_selector = "#__next > div.sc-e742802a-1.fprqKh.global-layout-v2 > div > div.cmc-body-wrapper > div > div > div > div:nth-child(2) > div > div:nth-child(4) > div:nth-child(2) > div.sc-8a2da6a1-4.kugsrA > div.sc-8a2da6a1-11.jgVnqT > button"
    driver.find_element(By.CSS_SELECTOR, login_button_selector).click()

    login_tab_selector = "body > div.sc-acb6320-0.jVSkTR.modalOpened > div > div > div > div > div.sc-79c2884f-1.hmAaQh > div.sc-79c2884f-2.jEAjov.tab-item"
    driver.find_element(By.CSS_SELECTOR, login_tab_selector).click()

    email_input_selector = "body > div.sc-acb6320-0.jVSkTR.modalOpened > div > div > div > div > div:nth-child(2) > div:nth-child(1) > input"
    driver.find_element(By.CSS_SELECTOR,email_input_selector).send_keys(username)

    password_input_selector = "body > div.sc-acb6320-0.jVSkTR.modalOpened > div > div > div > div > div:nth-child(2) > div.sc-1cf81b5e-8.kQPJck.last > div.sc-f23c2c4c-0.gEqHyg > input"
    driver.find_element(By.CSS_SELECTOR, password_input_selector).send_keys(password)

    login_with_credentials_button_selector = "body > div.sc-acb6320-0.jVSkTR.modalOpened > div > div > div > div > div:nth-child(2) > div.sc-1cf81b5e-11.hcnPEY > button"
    driver.find_element(By.CSS_SELECTOR,login_with_credentials_button_selector).click()
    time.sleep(1)

    collect_diamonds_button_selector = "#__next > div.sc-e742802a-1.fprqKh.global-layout-v2 > div > div.cmc-body-wrapper > div > div > div > div:nth-child(2) > div > div:nth-child(4) > div:nth-child(2) > div.sc-8a2da6a1-4.kugsrA > div.sc-8a2da6a1-11.jgVnqT > button"
    driver.find_element(By.CSS_SELECTOR, collect_diamonds_button_selector).click()

except Exception as e:
    print('---- An error has occured while accessing the website. ----\n')
    print(f"Error:\n{e}")

finally:
    driver.quit()
    exit()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get('https://esportsawards.com/vote/')
driver.maximize_window()

cookies = driver.find_element(By.ID, 'sizzle-gdpr-accept')
cookies.click()

time.sleep(3)

driver.execute_script("window.scrollTo(0, 4800)")

time.sleep(2)

tarik = driver.find_element(By.CSS_SELECTOR, 'img[src="https://esportsawards.com/wp-content/uploads/2022/06/Tarik-01.png"]')
driver.execute_script("arguments[0].click();", tarik)

time.sleep(2)

submit_vote = driver.find_element(By.XPATH, '//*[@id="vote-actions"]/button')
driver.execute_script("arguments[0].click();", submit_vote)

time.sleep(2)

Name = driver.find_element(By.CSS_SELECTOR, '#details-form > div:nth-child(7) > div.n-form-item-blank > div > div.n-input-wrapper > div.n-input__input > input')
Name.send_keys('LIL BRO')

time.sleep(4)

Email = driver.find_element(By.CSS_SELECTOR, '#details-form > div:nth-child(9) > div.n-form-item-blank > div > div.n-input-wrapper > div.n-input__input > input')
Email.send_keys('badapipe+1@finews.biz')

time.sleep(1)

no_news_receive = driver.find_element(By.CSS_SELECTOR, '#details-form > div:nth-child(10) > div.n-form-item-blank > div > div > label:nth-child(6)')
driver.execute_script("arguments[0].click();", no_news_receive)

no_offers = driver.find_element(By.CSS_SELECTOR, '#details-form > div:nth-child(11) > div.n-form-item-blank > div > div > label:nth-child(6)')
driver.execute_script("arguments[0].click();", no_offers)

submit_vote_2 = driver.find_element(By.CSS_SELECTOR, '#details-form > button > span')
driver.execute_script("arguments[0].click();", submit_vote_2)

time.sleep(2)

gender = driver.find_element(By.CSS_SELECTOR, '#additional-form > div:nth-child(6) > div.n-form-item-blank > div.field-options > div > label:nth-child(1) > input')
driver.execute_script("arguments[0].click();", gender)

age = driver.find_element(By.CSS_SELECTOR, '#additional-form > div:nth-child(7) > div.n-form-item-blank > div.field-options > div > label:nth-child(3) > input')
driver.execute_script("arguments[0].click();", age)

submit_vote_3 = driver.find_element(By.CSS_SELECTOR, '#additional-form > button > span')
driver.execute_script("arguments[0].click();", submit_vote_3)

# driver.close()


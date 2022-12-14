from termios import B1000000
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service
from webdriver_manager.chrome import ChromeDriverManager

options = ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless")
service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service,options=options)

driver.get("https://www.cincinnati.com/story/sports/high-school/high-school-sports/2022/10/25/vote-cincinnati-enquirer-high-school-athletes-of-the-week-oct-24/69585959007/")
#/html/body/div[2]/main/article/div[4]/aside[13]/iframe
test = driver.find_element(By.XPATH, "/html/body/div[2]/main/article/div[4]/aside[13]")
#frame = test.find_element(By.CLASS_NAME, "gnt_em_hf_if")
driver.implicitly_wait(5)

driver.switch_to.frame(12)   #driver.find_element(By.XPATH, "/html/body/div[2]/main/article/div[4]/aside[13]/iframe"))
#survey = driver.find_element(By.XPATH, "/html/body/div/form/div/div/div/div/div[2]/span")
surveyclicker = driver.find_element(By.ID, "PDI_answer51312243")
test = driver.find_element(By.XPATH, "/html/body/div/form")

button = driver.find_element(By.ID, "pd-vote-button11227228")

surveyclicker.click()
button.click()

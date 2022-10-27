from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path


service_object = Service(binary_path)
driver = webdriver.Chrome(service=service_object)
driver.get("https://www.cincinnati.com/story/sports/high-school/high-school-sports/2022/10/25/vote-cincinnati-enquirer-high-school-athletes-of-the-week-oct-24/69585959007/")
survey = driver.find_element(By.ID, "PDI_answer51312243")
button = driver.find_element(By.ID, "pd-vote-button11227228")

survey.click()
button.click()

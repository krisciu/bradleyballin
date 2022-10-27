from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.cincinnati.com/story/sports/high-school/high-school-sports/2022/10/25/vote-cincinnati-enquirer-high-school-athletes-of-the-week-oct-24/69585959007/")
survey = driver.find_element(By.ID, "PDI_answer51312243")
button = driver.find_element(By.ID, "pd-vote-button11227228")

survey.click()
button.click()

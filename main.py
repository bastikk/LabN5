from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

url = "https://dota2protracker.com/"
browser = webdriver.Chrome(executable_path="C:\\Users\\b1504\PycharmProjects\LabN5\chromedriver\chromedriver.exe")
browser.get(url)

browser.implicitly_wait(30)

browser.find_element(By.CSS_SELECTOR, '[id="autocomplete"]').send_keys("Earthshak")
browser.find_element(By.CSS_SELECTOR, '[href="/hero/Earthshaker"]').send_keys(Keys.RETURN)

actual_text = browser.find_element(By.CSS_SELECTOR, '[class="hero-stats-name"').text

expected_text = "Earthshaker"

print(actual_text == expected_text)

assert actual_text == expected_text

from selenium import webdriver
from selenium.webdriver.common.by import By

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--incognito")
chromeOptions.add_argument("--headless")

fromCity = "Cambui, mg"
toCity = "São paulo, SP"

driver = webdriver.Chrome(options=chromeOptions)
driver.get('https://www.google.com/maps/dir/{}/{}'.format(fromCity, toCity))

result = driver.find_element(By.XPATH, '//*[@id="section-directions-trip-0"]/div[1]/div[1]/div[1]/div[2]/div').text
driver.save_screenshot("{}-{}.png".format(fromCity, toCity))
print(result)
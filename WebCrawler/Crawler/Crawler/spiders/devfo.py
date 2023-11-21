from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Path to your ChromeDriver executable
chrome_driver_path = '"C:/Users/Charudatta/Desktop/ChromeDriver/chromedriver-win64/chromedriver.exe"'

service = Service(chrome_driver_path)
service.start()

options = webdriver.ChromeOptions()
options.headless = True  # Run in headless mode to not open a browser window

driver = webdriver.Chrome(service=service, options=options)

url = 'https://devfolio.co/hackathons/past'
driver.get(url)

# Find elements by class name
titles = driver.find_elements_by_class_name('sc-dkzDqf')  # or 'sc-dkzDqf lecwTx'

# Extract and print the text from these elements
for title in titles:
    print(title.text.strip())

driver.quit()
service.stop()

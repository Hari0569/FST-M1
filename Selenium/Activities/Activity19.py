# Set up the Firefox Driver with WebDriverManger
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

service = FirefoxService(GeckoDriverManager().install())

# Start the Driver
with webdriver.Firefox(service=service) as driver:
    # Navigate to the URL
    driver.get("https://www.training-support.net/selenium/javascript-alerts")
    # Print the title of the page
    print("Page title is: ", driver.title)

    # Find the confirm button and click it
    driver.find_element(By.ID, "confirm").click()
    # Switch focus to the alert
    confirm_alert = driver.switch_to.alert
    # Print the text in the alert
    print(confirm_alert.text)
    # Close the alert with either one of the methods
    # with OK
    confirm_alert.accept()
    # with Cancel
    # confirm_alert.dismiss()
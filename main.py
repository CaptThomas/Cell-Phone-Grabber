import time
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
# Initialize the browser
chromedriver_autoinstaller.install()
# Install Chrome web driver from selenium package
browser = webdriver.Chrome()

#CONFIGURATIONS
### CHANGE ME! ###
STATE = "Massachusetts"
CITY = "Winchester"
### CHANGE ME! ###
link = "https://411.info/white-pages/"+STATE+"/"+CITY
browser.get(link)
for let in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]:
    browser.get(link+"?letter="+let)
    time.sleep(1)
    # Get all elements in each div class "span4"
    elements = browser.find_elements(By.CLASS_NAME, "span4")
    for element in elements:
        # Get all elements in each div class that are a tags
        a_elements = element.find_elements(By.TAG_NAME, "a")
        # New empty list to store links
        links = []
        for a_element in a_elements:
            # Get the href of each a tag and store in links
            links.append(a_element.get_attribute("href"))
        print(links)
# Don't forget to close the browser when you're done
browser.quit()

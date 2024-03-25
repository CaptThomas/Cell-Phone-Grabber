import time
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By

# Initialize the browser
chromedriver_autoinstaller.install()
# Install Chrome web driver from selenium package
browser = webdriver.Chrome()

# CONFIGURATIONS
### CHANGE ME! ###
STATE = "Massachusetts"
CITY = "Winchester"
### CHANGE ME! ###
numbers = []
# Open numbers.csv and write all numbers to numbers list
with open("numbers.csv") as f:
    for line in f:
        numbers.append(line.strip())
link = "https://411.info/white-pages/" + STATE + "/" + CITY
browser.get(link)
for let in [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]:
    browser.get(link + "?letter=" + let)
    time.sleep(1)
    # Get all elements in each div class "span4"
    elements = browser.find_elements(By.CLASS_NAME, "span4")
    for element in elements:
        # Get all elements in each div class that are a tags
        try:
            a_elements = element.find_elements(By.TAG_NAME, "a")
        except:
            continue
        # New empty list to store links
        links = []
        for a_element in a_elements:
            # Get the href of each a tag and store in links
            links.append(a_element.get_attribute("href"))
        for l in links:
            browser.get(l)
            time.sleep(1)
            div_elements = browser.find_elements(By.CLASS_NAME, "phone")
            for div_element in div_elements:
                # Append to numbers if not already in the list
                if div_element.text not in numbers:
                    numbers.append(div_element.text)
                    # Write numbers to file
                    with open("numbers.csv", "a") as f:
                        f.write("%s\n" % div_element.text)

# Save all numbers to a csv file
with open("numbers.csv", "w") as f:
    for number in numbers:
        f.write("%s\n" % number)
    f.close()

# Don't forget to close the browser when you're done
browser.quit()

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")

searchFieldElement = driver.find_element(By.NAME, "search_query")
sleep(5)
searchFieldElement.send_keys("benjamin diary of jane")
searchFieldElement.send_keys(Keys.ENTER)
sleep(5)

firstVideoElement = driver.find_element(By.XPATH, "//ytd-video-renderer[@id='contents']/ytd-video-renderer[1]")
sleep(5)
firstVideoElement.click()
sleep(25)

# secondVideoElement = driver.find_element(By.XPATH, "//*[@id='dismissible']")
# sleep(5)
# secondVideoElement.click()
# sleep(25)


playPauseButton = driver.find_element(By.CLASS_NAME, "ytp-play-button.ytp-button")
playPauseButton.click()
sleep(3)

# Vardan jan erb porcum em sleep() vayrkyanner@ qchacnem im mot error e talis.
# miayn 18 toxy kap chuni inchqan em nshum ashxatum e.

# Ays tarberakov ashxatum e. hnaravor e hushes inchic klini.????



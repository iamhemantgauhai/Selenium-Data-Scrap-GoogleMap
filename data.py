# Importing libraries
import pprint
from pip import main
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import NoSuchElementException
import csv
import time

# Loading Selenium Webdriver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 3)

# Opening Google maps
driver.get("https://www.google.com/maps")
time.sleep(3)

# Finding the search box
searchbox = driver.find_element_by_id('searchboxinput')
time.sleep(3)
searchbox.send_keys("Restaurants in Sydney")
time.sleep(3)
searchbox.send_keys(Keys.ENTER)
time.sleep(3)

index = 0

templist = []

inner_index = 0

while(index < 1):

    data_xpath = driver.find_element_by_xpath(
        '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')
    time.sleep(3)

    html = driver.find_element_by_xpath(
        '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]')
    html.send_keys(Keys.END)
    time.sleep(3)

    html = driver.find_element_by_xpath(
        '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]')
    html.send_keys(Keys.END)
    time.sleep(3)

    html = driver.find_element_by_xpath(
        '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]')
    html.send_keys(Keys.END)
    time.sleep(3)

    html = driver.find_element_by_xpath(
        '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]')
    html.send_keys(Keys.END)
    time.sleep(3)

    restaurant_data = str(data_xpath.text.encode("utf-8")).replace('b"Sort by', "").replace("b'Sort by", "").replace('bSort by', "").replace("\n", "").replace("\\xc2\\xb7", "").replace("\\xe2\\x8b\\x85", "").replace('  Dine-in', "").replace('Takeaway', "").replace('No takeaway',"").replace('Delivery', '').replace('No Delivery','').replace('  RESERVE A TABLE', '').replace('Kerbside pickup', '').replace('No-contact delivery', "").replace('Drive-through', "").replace("Noida Restaurant", "").replace("business.google.com/chai-roti-bar", "").replace('"', "").replace("'", "").replace("//n", "").replace("\n", "").replace("\xe2\x8b\x85", "").replace("\xc2\xb7", "").replace("\u00b7", "").replace("\u22c5", "").replace("\u20b9\u20b9", "").replace("\u00e9", "").replace(
        "\u0938\u0940", "").replace("Ad", "").replace("\u20b9\u20b9\u20b9", "").replace("\ud83d\uddfc", "").replace("'\'", "").replace("\u00ae", "").replace("\\xe2\\x82\\xb9\\xe2\\x82\\xb9", "").replace("\u2019", "").replace("\xe2\x82\xb9\xe2\x82\xb9", "").replace('Build-your-own sandwich chain', "").replace("Update results when map moves", "").replace("Showing results 1 - 20", "").replace("Showing results 21 - 40", "").replace("Showing results 41 - 60", "").replace("Showing results 61 - 80", "").replace("Showing results 81 - 100", "").replace("Showing results 101 - 120", "").replace("Showing results 121 - 140", "").replace("Showing results 141 - 160", "").replace("Showing results 161 - 180", "").replace("Showing results 181 - 200", "").replace("Showing results 201 - 220", "")

    driver.find_element_by_xpath(
        "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/button[2]").click()
    time.sleep(3)

    restaurant_data.strip()

    list_data = restaurant_data.split("\\n")

    del(list_data[:2])

    for i in list_data:
        if i == '':
            continue
        else:
            templist.append(i)

    index += 1

pprint.pprint(templist)
table = 4
count = 0

with open("Restaurant-Details.csv", "a") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        ["Hotel Names", "Ratings", "Addresses", "Timings"])
    while table <= len(templist):
        main_data = [templist[count:table]]
        writer.writerows(main_data)
        table += 4
        count += 4

pprint.pprint("Done")

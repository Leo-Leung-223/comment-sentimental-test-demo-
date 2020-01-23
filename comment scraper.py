#import selenium package for web scraping
from selenium import webdriver
import csv
driver = webdriver.Chrome()

#use web driver to go to the website
driver.get("https://www.openrice.com/zh/hongkong/r-%E5%BF%83%E4%B9%8B%E9%A3%9F%E5%A0%82-%E9%8A%85%E9%91%BC%E7%81%A3-%E6%97%A5%E6%9C%AC%E8%8F%9C-%E5%A3%BD%E5%8F%B8-%E5%88%BA%E8%BA%AB-r511427")

#extract list of commment base on xpath
comments=driver.find_elements_by_xpath("//div[contains(@class, 'text js-text is-truncated')]")

#loop through page comment
for comment in comments:
    text=comment.text
    data=[]
    data.append(text)
    print(text)
    with open('comment.csv', 'a', encoding="utf-8 ") as datafile:
        writer = csv.writer(datafile, delimiter='.')
        writer.writerows(data)
    print('get comment complete')
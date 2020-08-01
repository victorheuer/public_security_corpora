# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 09:57:40 2020

@author: Victor
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time

def get_target_html(url):
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    
    #Finding target HTML
    print('Accessing page 1')
    site_html = wait.until(lambda driver: driver.find_element_by_xpath('//div[@class="gsc-expansionArea"]').get_attribute('innerHTML'))
    driver.close() 
    
    #Wrinting and saving the first page target HTML
    print('Saving page 1 html')
    with open('target_page_1.html', 'wt', encoding='utf-8') as file:
        file.write(site_html)

def get_next_pages(url):
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    #wait = WebDriverWait(driver, 10)
    driver.get(url)
    
    #Creating a list that receives all elements according to the given XPATH
    pages_list = driver.find_elements_by_xpath('//div[@class="gsc-cursor-page"]')
    pages_amount = len(pages_list)
    
    #Creating a loop to update the pages list and get their target HTML
    for index in range(pages_amount):
        number = str(index+2)
        updated_page_list = driver.find_elements_by_xpath('//div[@class="gsc-cursor-page"]')
        print(f'Accessing page {number}')
        updated_page_list[index].click()
        time.sleep(5)
        #wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="gsc-expansionArea"]')))
        target_html = driver.find_element_by_xpath('//div[@class="gsc-expansionArea"]').get_attribute('innerHTML')
        
        #Writing and saving a HTML file with the target code
        print(f'Saving page {number} html')
        with open(f'target_page_{number}.html', 'wt', encoding='utf-8') as file:
            file.write(target_html)
            
    driver.close()
    print('Finished')

#Starting URL
url = 'https://www.diariodepernambuco.com.br/capa_busca.html?q=seguran%C3%A7a&q=seguran%C3%A7a%20%2B%20p%C3%BAblica%20%2B%20pernambuco&q=%22seguran%C3%A7a%20p%C3%BAblica%22%20%2B%20pernambuco&q=%22seguran%C3%A7a%20p%C3%BAblica%22%20%2B%20crime*%20%2B%20pernambuco&q=%22seguran%C3%A7a%20p%C3%BAblica%22%20%2B%20crim*%20%2B%20pernambuco'

#Applying get_target_html function
initial_page = get_target_html(url)

#Getting the next pages HTML
get_next_pages(url)

from selenium import webdriver #simulate brawser use
from selenium.webdriver.common.by import By #find informations 
import openpyxl #create workboot

driver = webdriver.Chrome()

workboot = openpyxl.Workbook()
workboot.create_sheet('Games')

sheet_games = workboot['Games']
sheet_games['A1'].value = 'Game'
sheet_games['B1'].value = 'Price'

# Primeira URL
driver.get('https://www.lojasgamemania.com.br/jogo-playstation-4')

titles = driver.find_elements(By.XPATH, "//h3[@class='product-name']")
prices = driver.find_elements(By.XPATH, "//span[@class='price-boleto']")

for title, price in zip(titles, prices):
    sheet_games.append([title.text, price.text])

# Segunda URL
driver.get('https://www.lojasgamemania.com.br/jogo-playstation-4?p=2')

titles = driver.find_elements(By.XPATH, "//h3[@class='product-name']")
prices = driver.find_elements(By.XPATH, "//span[@class='price-boleto']")

for title, price in zip(titles, prices):
    sheet_games.append([title.text, price.text])

workboot.save('Games.xlsx')

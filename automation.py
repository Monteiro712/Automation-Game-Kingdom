from selenium import webdriver 
from selenium.webdriver.common.by import By 
import openpyxl 

def collect_data(url):
    driver.get(url)
    titles = driver.find_elements(By.XPATH, "//h3[@class='product-name']")
    prices = driver.find_elements(By.XPATH, "//span[@class='price-boleto']")
    return zip(titles, prices)

def add_to_sheet(data, sheet):
    for title, price in data:
        sheet.append([title.text, price.text])

driver = webdriver.Chrome()

workboot = openpyxl.Workbook()
workboot.create_sheet('Games PS4')

sheet_games_ps4 = workboot['Games PS4']
sheet_games_ps4['A1'].value = 'Game'
sheet_games_ps4['B1'].value = 'Price'

data = collect_data('https://www.lojasgamemania.com.br/jogo-playstation-4')
add_to_sheet(data, sheet_games_ps4)

data = collect_data('https://www.lojasgamemania.com.br/jogo-playstation-4?p=2')
add_to_sheet(data, sheet_games_ps4)

workboot.create_sheet('Games SWITCH')
sheet_games_sw = workboot['Games SWITCH']
sheet_games_sw['A1'].value = 'Game'
sheet_games_sw['B1'].value = 'Price'

data = collect_data('https://www.lojasgamemania.com.br/jogos-de-nintendo-switch')
add_to_sheet(data, sheet_games_sw)

workboot.save('Games.xlsx')

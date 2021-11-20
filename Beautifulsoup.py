
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter.scrolledtext import ScrolledText as st
import os

url = "http://www.cbr.ru/scripts/XML_daily.asp"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'lxml')
print(soup)

lst = soup.find_all('name')

for item in lst:
    print(item)

url = "https://seaborn.pydata.org/examples/index.html"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
print(soup)
# print(soup.prettify())

lst = soup.find_all('p')

for item in lst:
    print(item)

def clean_item(my_item):
    position = my_item.find('<a')
    return my_item[3:position]

print("")

for item in lst:
    print(clean_item(str(item)))

def clean_item2(my_item):
    position = my_item.find('</p')
    return my_item[3:position]

for item in lst:
    print(clean_item2(str(item)))
    
url = "http://api.weatherapi.com/v1/forecast.xml?key=006e246f32f846e4a35171023211511&q=London&days=1&aqi=no&alerts=no"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'lxml')
print(soup)
print("")
# print(soup.prettify())

# Создание главного окна
window = tk.Tk()
window.geometry("550x550")
window.title("Программа ")

# Создание меток вывода
label_00 = tk.Label(text = "Путь к файлу:")
label_00.grid(row=0, column=0, padx=10, pady=10, sticky="e")

# Добавление полей ввода
label_01 = tk.Entry(text = "")
label_01.place(x=120, y=10, width=300, height=20)
label_01.grid(row=0, column=1, sticky="w")

label_10 = tk.Label(text = "Строк:")
label_10.grid(row=1, column=0, padx=10, pady=10, sticky="e")

label_11 = tk.Label(text = "")
label_11.grid(row=1, column=1, sticky="w")

label_20 = tk.Label(text = "Столбцов:")
label_20.grid(row=2, column=0, padx=10, pady=10, sticky="e")

label_21 = tk.Label(text = "")
label_21.grid(row=2, column=1, sticky="w")

# Создание текстового вывода c прокруткой
output_text = st(height = 22, width = 50)
output_text.grid(row=3, column=1, padx=10, pady=10, sticky="w")

lst = soup.find_all('temp_c')

for item in lst:   
    output_text.insert(tk.END, str(item) + os.linesep)
    print(item)
# print

button=tk.Button(window, text="Прочитать файл")
button.grid(row=4, column=1)

window.mainloop()

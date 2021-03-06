import requests
import xmltodict
import tkinter as tk
from tkinter.scrolledtext import ScrolledText as st
import os

url = "http://www.cbr.ru/scripts/XML_val.asp"
response = requests.get(url)
data = xmltodict.parse(response.content)
print(data)

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

my_array = []
for item in data['Valuta']['Item']:
    my_set = [item['Name'], item['EngName'], item['Nominal'], item['ParentCode']];
    my_array.append(my_set)
    output_text.insert(tk.END, str(my_set) + os.linesep)
# print(my_set)
# print(my_array)

# Создание кнопки
button=tk.Button(window, text="Прочитать файл")
button.grid(row=4, column=1)

# Запуск цикла mainloop
window.mainloop()

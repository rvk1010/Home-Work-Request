import requests
import json

list_super = ['Hulk', 'Captain America', 'Thanos']  # имена супергероев для поиска
age_super = {'Hulk': -1, 'Captain America': -1, 'Thanos': -1}  # возраст для поиска

url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)  # считываем с сайта
print(response.ok)
json_url = response.json()  # сохраняем объект как json

for person in json_url:  # пробегаемся по json и ищем супергероев
    if person['name'] in list_super:
        age_super[person['name']] = person['powerstats']['intelligence']

sort_super = dict(sorted(age_super.items(), key=lambda item: item[1], reverse=True))
print(list(sort_super)[0])  # выводим имя самного умного супергероя

import json
import urllib.request
import webbrowser
import gzip
# import grab

print('Программа по работе с онлайн-сервисом OpenWeatherMap \n')

def get_appid():
    print('Получите бесплатный APPID для доступа к сервису')
    print('1. Получить APPID вручную')
    print('2. Получить APPID автоматически')
    user_input = input('Выберите вариант получения APPID: ')
    if user_input == '1':
        print('Пройдите регистрацию на сайте')
        webbrowser.open('https://home.openweathermap.org/users/sign_up')
    if user_input == '2':
        pass
    return get_appid()

def get_city():
    print('Получите список городов')
    print('1. Получить список городов вручную')
    print('2. Получить список городов автоматически')
    user_input = input('Выберите вариант получения списка городов: ')
    if user_input == '1':
        print('Скачайте список городов и распакуйте')
        webbrowser.open('http://bulk.openweathermap.org/sample/city.list.json.gz')
    if user_input == '2':
        url = 'http://bulk.openweathermap.org/sample/city.list.json.gz'
        urllib.request.urlretrieve(url, 'city.gz')
        in_file = gzip.open('city.gz', 'rb')
        out_file = open('city.txt', 'wb')
        out_file.write(in_file.read())
        in_file.close()
        out_file.close()
    return get_city

def url_weather():
    print('Получите погоду')
    appid = input('Введите свой APPID: ')
    city_name = input('Введите название города на латинском: ')
    unit = 'metric'
    api_url_part = 'http://api.openweathermap.org/data/2.5/weather?id='
    api_url_full = api_url_part + str(city_name) + '&mode=json&units=' + unit + '&APPID=' + appid
    return api_url_full

def get_weather(api_url_full):
    url = urllib.request.urlopen(api_url_full)
    output = url.read().decode('utf-8')
    raw_api_dict = json.loads(output)
    url.close()
    return raw_api_dict

def form_weather(raw_api_dict):
    data = dict(
        city=raw_api_dict.get('name'),
        country=raw_api_dict.get('sys').get('country'),
        temp=raw_api_dict.get('main').get('temp')
    )
    return data

def output_weather(data):
    print('Текущая температура в: {}, {}:'.format(data['city'], data['country']))


if __name__ == '__main__':
    try:
        output_weather(form_weather(get_weather(url_weather(get_city()))))
    except IOError:
        print('Проверьте доступ в Интернет')
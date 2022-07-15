import requests
from bs4 import BeautifulSoup
from item import Weather
import csv


def getData(url, headers):
    # Http GET 网络请求
    resp = requests.get(url=url, headers=headers)
    # 指定网络请求响应编码
    resp.encoding = 'UTF-8'

    # 返回网页源代码数据
    return resp.text


def analizesData(html):
    list = []

    soup = BeautifulSoup(html, 'lxml')
    divs = soup.find('div', {'class':'hanml'}).find('div', {'class':'conMidtab'}).find_all('div', {'class':'conMidtab2'})
    print(len(divs));
    for div in divs:
        trs = div.select('table tr')[2:]
        province = div.find('td', {'class':'rowsPan'}).find('a').string.strip()

        for tr in trs:
            weather = Weather()
            tds = tr.select('td:not(.rowsPan)')
            print(tds)

            weather.province = province  # 省/直辖市
            weather.city = tds[0].a.string.strip()  # 城市
            weather.weather_day = tds[1].string  # 日间天气现象
            weather.weather_night = tds[3].string.strip()  # 夜间天气现象
            weather.wind_direction_day = tds[2].span.string.strip()  # 日间风向
            weather.wind_direction_night = tds[5].find_all('span')[0].string.strip()  # 夜间风向
            weather.wind_power_day = tds[2].find('span', {'class':'conMidtabright'}).string.strip()  # 日间风力等级
            weather.wind_power_night = tds[5].find('span', {'class':'conMidtabright'}).string.strip()  # 夜间风力等级
            weather.temperature_high = tds[3].string.strip()  # 最高气温
            weather.temperature_low = tds[3].string.strip()  # 最低气温
            weather.href_info = tds[7].a.attrs['href']  # 详情链接
            print(weather)
            list.append(weather)

    return list


def writeCSV(weathers):
    with open('weather.csv', 'w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file)
        for weather in weathers:
            writer.writerow([weather.province,
                             weather.city,
                             weather.weather_day,
                             weather.weather_night,
                             weather.wind_direction_day,
                             weather.wind_direction_night,
                             weather.wind_power_day,
                             weather.wind_power_night,
                             weather.temperature_high,
                             weather.temperature_low,
                             weather.href_info])
        file.close()

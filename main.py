# This is a sample Python script.
from CSVTest01 import writeCSV
from CSVTest01 import analizesData
from CSVTest01 import getData
from fake_useragent import UserAgent
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = 'http://www.weather.com.cn/textFC/hb.shtml'
    headers = {
        'Cookie': 'userNewsPort0=1; f_city=%E9%93%9C%E4%BB%81%7C101260601%7C; defaultCty=101260601; defaultCtyName=%u94DC%u4EC1; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1657854333',
        'Referer': 'http://www,weather.com.cn',
        'User-Agent': UserAgent().random
    }
    writeCSV(analizesData(getData(url=url, headers=headers)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

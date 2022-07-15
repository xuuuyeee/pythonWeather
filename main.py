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
        'User-Agent': UserAgent().random
    }
    writeCSV(analizesData(getData(url=url, headers=headers)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

class Weather():

    def __init__(self):
        self.province = ''  # 省/直辖市
        self.city = ''  # 城市
        self.weather_day = ''  # 日间天气现象
        self.weather_night = ''  # 夜间天气现象
        self.wind_direction_day = ''  # 日间风向
        self.wind_direction_night = ''  # 夜间风向
        self.wind_power_day = ''  # 日间风力等级
        self.wind_power_night = ''  # 夜间风力等级
        self.temperature_high = ''  # 最高气温
        self.temperature_low = ''  # 最低气温
        self.href_info = ''  # 详情链接

    def __str__(self):
        return 'province:%s ;' \
               'city:%s ;' \
               'weather_day:%s ;' \
               'weather_night:%s ;' \
               'wind_direction_day:%s ;' \
               'wind_direction_night:%s ;' \
               'wind_power_day:%s ;' \
               'wind_power_night:%s ;' \
               'temperature_high:%s ;' \
               'temperature_low:%s ;' \
               'href_info:%s ;' \
               % (self.province,
                  self.city,
                  self.weather_day,
                  self.weather_night,
                  self.wind_direction_day,
                  self.wind_direction_night,
                  self.wind_power_day,
                  self.wind_power_night,
                  self.temperature_high,
                  self.temperature_low,
                  self.href_info)
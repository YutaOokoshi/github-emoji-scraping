import configparser
import os

"""

[APP]
name: user-name

# 上記のようなconfig.iniの場合、 以下のように使う

from config import CONFIG

print(CONFIG['APP']['name']) # print of "user-name"

"""

c = configparser.ConfigParser()
c.read('config.ini', encoding='UTF-8')


# 環境ごとに異なる設定を読み込む場合はココ
if os.getenv('ENV') == 'local':
    pass
elif os.getenv('ENV') == 'test':
    pass
elif os.getenv('ENV') == 'dev':
    pass
elif os.getenv('ENV') == 'prod':
    pass
else:
    pass

CONFIG = {}

for section in c.sections():
    d = {}
    for option in c.options(section):
        d[option] = c.get(section, option)
    CONFIG[section] = d

# print(CONFIG)

ENV_TUPLE = ('local', 'dev', 'prod', 'test')

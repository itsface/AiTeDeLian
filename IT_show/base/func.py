import random
from IT_show import settings
import logging

chNum = "0123456789"
chAlphaLow = "qwertyuiopasdfghjklzxcvbnm"
chAlphaHigh = "QWERTYUIOPASDFGHJKLZXCVBNM"

identifyName = 'identify.png'
identifyDir = settings.MEDIA_ROOT
identifyPath = identifyDir + identifyName

# 生成几位数的验证码
identifyLen = 4

# 生成验证码图片的高度和宽度
identifySize = (80, 30)

# 背景颜色，默认为白色
identifyBgcolor = (255, 255, 255)

# 字体颜色，默认为蓝色
identifyFontcolor = (0, 0, 255)

# 干扰线颜色。默认为红色
identifyLinecolor = (255, 0, 0)

# 是否要加入干扰线
identifyDraw_line = True

# 加入干扰线条数的上限
identifyLine_number = 5


def randomString(chSet, len):
    strlen = str(chSet).__len__()
    backString = ""
    for i in range(0, len):
        r = random.randint(0, strlen-1)
        backString = backString + chSet[r]
    logging.debug("随机串："+backString)
    return backString


def randomCode():
    return randomString(chAlphaHigh + chAlphaLow + chNum, 10)

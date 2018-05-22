import random

chNum = "0123456789"
chAlphaLow = "qwertyuiopasdfghjklzxcvbnm"
chAlphaHigh = "QWERTYUIOPASDFGHJKLZXCVBNM"

def randomString(chSet, len):
    strlen = str(chSet).__len__()
    backString = ""
    for i in range(0, len):
        r = random.randint(0, strlen)
        backString = backString + chSet[r]
    return backString


def randomCode():
    return randomString(chAlphaHigh + chAlphaLow + chNum, 10)

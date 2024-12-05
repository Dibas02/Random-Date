import random
import time


def getrandomdate(stDate, endDate):
    random_gen = random.random()
    format = '%m/%d/%Y'


    stTime = time.mktime(time.strptime(stDate, format))
    endtime = time.mktime(time.strptime(endDate, format))

    randomTime = stTime + random_gen*(endtime - stTime)
    randomDate = time.strftime(format, time.localtime(randomTime))
    return randomDate

print("Random date=", getrandomdate('1/1/2017', '2/5/2017'))
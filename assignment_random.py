import random
import datetime

dateCreate = datetime.datetime.now()

RandomFirst = random.uniform(0,1)
RandomSecond = random.randint(1,10)

print("Timestamp:",dateCreate,"")

print ("Between 0 and 1 : ",RandomFirst,"")

print ("Between 1 and 10: ",RandomSecond,"")

print("Timestamp and Random Val :", dateCreate, RandomFirst, RandomSecond, "")
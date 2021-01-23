import time

t = time.strptime("30/01/2021", "%d/%m/%Y")
print(time.mktime(t)-time.time())

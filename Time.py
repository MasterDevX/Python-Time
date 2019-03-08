import time

x = time.time()
time.sleep(1)
y = time.time()
z = round((y - x), 3)
print(z)

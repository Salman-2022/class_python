#creating a countdown timmer of 5 seconds
import time

def countdown(t):
    while t:
        print(t)
        t-=1
        time.sleep(1)
    print('time\'s up')

countdown(5)





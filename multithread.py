import threading
import time

def number():
    for i in range(10):
        time.sleep(2)
        print(f"number is {i}")


def square():
    for i in range(10):
        time.sleep(2)
        print(f"square of number is {i*i}")




#### creating thread

t1=threading.Thread(target=number)
t2=threading.Thread(target=square)

#### start threads 

t=time.time()

t1.start()
t2.start()


### we join thread

t1.join()
t2.join()

time_now=time.time()-t


print(f"time for this program is {time_now}")
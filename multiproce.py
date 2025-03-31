import multiprocessing

import time

def number():
    for i in range(10):
        time.sleep(2)
        print(f"number is {i}")


def square():
    for i in range(10):
        time.sleep(2)
        print(f"square of number is {i*i}")


if __name__=="__main__":
    p1=multiprocessing.Process(target=number)
    p2=multiprocessing.Process(target=square)
    
    ### start process
    
    t=time.time()
    p1.start()
    p2.start()
    
    p1.join()
    p1.join()
    time_now=time.time()-t
    
    print(f"time for this program is {time_now}")
    
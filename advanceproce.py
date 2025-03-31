from concurrent.futures import ProcessPoolExecutor

import time

def square(num):
    time.sleep(2)
    print(f"square of number is {num*num}")
    



if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=3) as excute:
        excute.map(square,[1,3,6,9,10,11])
        
from concurrent.futures import ThreadPoolExecutor

import time

def number(n):
    
    time.sleep(2)
    print(f"number is {n}")
   

def square(n):
    
    time.sleep(2)
    print(f"square of number is {n*n}")


with ThreadPoolExecutor(max_workers=4) as excuter:
    excuter.map(number,[1,2,3,4,5,6])


with ThreadPoolExecutor(max_workers=3) as excuter1:
    excuter1.map(square,[1,2,3,4,5,6])
    

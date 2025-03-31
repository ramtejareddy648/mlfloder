from logger import logging
from logger import*

def add(a,b):
    logging.debug("addition functon is running")
    logging.error("addition functon is running")
    return a+b


logging.debug("addition variable is sending")
add(1,3)

def sub(c,d):
    logger1.debug("sub operation is doing")
    return c-d


logger2.debug("sub variables are going")
sub(4,3)

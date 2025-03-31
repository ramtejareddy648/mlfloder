import logging

logger1=logging.getLogger("mode1")
logger1.setLevel(level=logging.DEBUG)
logger2=logging.getLogger("mode2")
logger2.setLevel(level=logging.DEBUG)

logging.basicConfig(
    filename='app',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
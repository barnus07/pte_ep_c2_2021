import random
import time


def szamlalo(hossz: int, leptek: int):
    for i in range(hossz // leptek):
        print(random.randint(0, 100))
        time.sleep(leptek)

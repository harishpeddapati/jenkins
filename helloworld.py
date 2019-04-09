#!/usr/bin/env python

import time

class helloworld:
    def __init__(self):
    	pass
    def test(self):
        for i in range(10):
            print(i,"Hello world")
            time.sleep(3)

def main():
    obj = helloworld()
    obj.test()


if __name__ == "__main__":
    main()


#!/usr/bin/env python

import time

class helloworld:
	def __init__(self):
		for i in range(10):
			print(i,"Hello world")
                        time.sleep(5)


def main():
	obj = helloworld()
	

if __name__ == "__main__":
	main()

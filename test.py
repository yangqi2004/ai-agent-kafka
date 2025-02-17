#!/usr/bin/python3

import sys
def fun2():
    print('list')
    msg = 'this is a long list'
    print(msg[0])

def fun1():
    print('String function')
    msg = 'This is a long number' + '1' * 1000
    print(msg)

def main():
    print('this is the main function')
    fun1()
    fun2()



if __name__ == '__main__':
	main()



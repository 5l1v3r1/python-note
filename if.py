#!/usr/bin/python
#coding:utf-8
from random import randint
num = randint(1, 10);
# print num;
answer = int(raw_input('输入一个数字: '));
while True:
    if num == answer:
        print '猜对啦';
        break;
    elif answer > num:
        print '猜大啦～'
    else:
        print '猜小啦';

    answer = int(raw_input('输入一个数字: '));
#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/7/5 下午4:27
# @Author  : MiracleYoung
# @File    : test.py


import string
import random
import argparse

letters = string.ascii_letters
nick = ''.join([random.choice(letters) for _ in range(16)])
parser = argparse.ArgumentParser(prog='app', description='这是一个MagCore客户端启动器')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 2.0')
parser.add_argument('--map', dest='map', type=str, default='RectSmall', help='地图名字。现在有RectSmall,RectMid,RectLarge')
parser.add_argument('--is_new', dest='is_new', type=bool, default=True, help='是否创建游戏')
parser.add_argument('--nick', dest='nick', type=str, default=nick, help='玩家昵称')
parser.add_argument('--color', dest='color', type=int, choices=range(0, 10), default=0, help='玩家颜色')
args = parser.parse_args()
m, nick, is_new, color = args.map, args.nick, args.is_new, args.color

print(m, nick, is_new, color)
#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/7/10 下午9:02
# @Author  : MiracleYoung
# @File    : attack.py


class Attack:
    def __init__(self, gid, pid, api):
        self._gid = gid
        self._pid = pid
        self._api = api

    def get_owner_cells(self, gid, idx) -> list:
        '''获得自己所有的单元格'''
        cells = self._api.get_game(gid).json()['Cells']
        return [[cell['X'], cell['Y']] for row in cells for cell in row if cell['Owner'] == idx]

    def is_alive(self, pid) -> bool:
        return self._api.get_player(pid).json()['State'] == 1

    def get_enemy_bases(self, idx, gid=0, game=None) -> dict:
        '''获取所有敌人基地坐标'''
        cells = game['Cells'] if game else self._api.get_game(gid).json()['Cells']
        return {cell['Owner']: (cell['X'], cell['Y']) for row in cells for cell in row if cell['Owner'] not in (idx, 0)}

    def attack_left(self, owner_cells, gid, pid, ):
        '''攻击左侧距离为1的单元格'''
        for x, y in owner_cells:
            # 判断不是自己单元格并且没有越界
            if [x - 1, y] not in owner_cells and x - 1 >= 0:
                self._api.attack_cell(gid, pid, x - 1, y)

    def attack_right(self, owner_cells, gid, pid, max):
        '''攻击右侧距离为1的单元格'''
        for x, y in owner_cells:
            if [x + 1, y] not in owner_cells and x + 1 < max:
                self._api.attack_cell(gid, pid, x + 1, y)

    def attack_up(self, owner_cells, gid, pid, max):
        '''攻击上方距离为1的单元格'''
        for x, y in owner_cells:
            if [x, y + 1] not in owner_cells and y + 1 < max:
                self._api.attack_cell(gid, pid, x, y + 1)

    def attack_down(self, owner_cells, gid, pid):
        '''攻击下方距离为1的单元格'''
        for x, y in owner_cells:
            if [x, y - 1] not in owner_cells and y - 1 >= 0:
                self._api.attack_cell(gid, pid, x, y - 1)

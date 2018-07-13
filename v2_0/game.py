#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/13/18 4:09 PM
# @Author  : Miracle Young
# @File    : game.py


from v2_0.api import API


class Game:
    def __init__(self, gid):
        self._gid = gid
        self._api = API()

    def run(self):
        return self._api.start_game(self._gid)

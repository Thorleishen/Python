#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/9/10 2:56 下午
# @Author : zhenyu lei
# @File : monostate.py
# @desc : 共享模式

class Monostate(object):
    __share_state = {}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__share_state


class MonostateV2(object):
    __share_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__share_state
        return obj


# 应用场景
class GameManager(object):
    __games = {}

    def __init__(self):
        pass

    def get_game_detail(self, game_name: str) -> dict:
        if game_name not in self.__games:
            return self.get_game_cache()
        return self.__games[game_name]

    def _get_game_cache(self, game_name) -> dict:
        """从数据库中获取缓存 并加入到内存中 类变量共享
        数据库没有，默认5分钟缓存，防止缓存穿透
        注：当数据库修改数据时，__games的数据也需要修改，或者删除，该设计模式更适合无需修改的类型或者状态
        """
        key = ''
        cache = ''  # 缓存数据
        if not cache:
            mysql = ''
            cache = mysql
            if cache:
                self.__games[game_name] = cache
        return cache


if __name__ == '__main__':
    m = Monostate()
    m1 = Monostate()

    m.x = 4

    print(m.__dict__)
    print(m1.__dict__)


# -*- coding: utf-8 -*-

import sqlite3

import numpy as np

from xrd.backend.xrd_pattern import XrdPattern

db_path = 'pattern.db'


class PatternDao:
    def __init__(self):
        self.conn = sqlite3.connect(db_path)

    def insert(self, p):
        if isinstance(p, XrdPattern):
            pass

    def close(self):
        self.conn.commit()
        self.conn.close()


if __name__ == '__main__':
    print(np.cos(82 * np.pi / 180))

# -*- coding: utf-8 -*-

from sklearn.feature_extraction import DictVectorizer
import csv

from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO

class DecisionTree:
    """
    DecisionTree
    """
    name = 'decision'

    def __init__(self):
        self.data = []

    def load(self, csvfile):
        reader = csv.reader(open(csvfile))
        for line in reader:
            print(line)


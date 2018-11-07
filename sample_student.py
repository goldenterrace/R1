# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:36:11 2015
@author: zhengzhang

Edited by Joyce 07/12/2018
"""
import util
import helper
NO_NAME_PRINT = True

# Sample class
class Sample(object):
    """
    each instance of the Sample class is one data point in the k-means problem
    """
    def __init__(self, name, features, label = None):
        #Assumes features is an array of numbers
        """for the 2-d k-means prob, features are the x, y coordinates
        stores in a list [x, y] """
        self.name = name
        self.features = features
        self.label = label  # for group info?

    def dimensionality(self):
        return len(self.features)

    def getFeatures(self):
        return self.features[:]

    def getLabel(self):
        return self.label

    def getName(self):
        return self.name

    def distance(self, other):
        return util.minkowskiDist(self.features, other.getFeatures(), 2)

    def setLabel(self, new_label):
        self.label = new_label

    def setName(self, new_name):
        self.label = new_name

    def __add__(self, other):
        """ other is another Sample instance"""
        f = []
        for i in range(self.dimensionality()):
            f.append(self.getFeatures()[i] + other.getFeatures()[i])
        return Sample(self.name + '+', f, self.label)

    def __truediv__(self, n):
        f = []
        for e in self.getFeatures():
            f.append(e/float(n))
        return Sample(self.name + '/' + str(n), f, self.label)

    #### Implement an overwrite of the '-' operator here!
    def __sub__(self, other):
        ''' replace the line below with you code
            refer to the __add__ for ideas '''
        #------- your code below -----------#
        return helper.__sub__(self, other)


        #-------- end of your code ----------#

    def __mul__(self, other):
        ''' bonus: can you do vector multiplication?
            this is two vectors element-wise multiplication '''
        #------- your code below ------------#
        return helper.__mul__(self, other)


        #-------- end of your code ----------#
    def __str__(self):
        if NO_NAME_PRINT:
            return str(self.features)
        else:
            return self.name +' : '+ str(self.features) + ' : ' + str(self.label)

if __name__ == "__main__":
    a = Sample('a', [1, 1,2,3])
    b = Sample('b', [-1, -1,2,3])

    # a = "17.99	10.38	122.8	1001	0.1184	0.2776	0.3001	0.1471	0.2419	0.07871	1.095	0.9053	8.589	153.4	0.006399	0.04904	0.05373	0.01587	0.03003	0.006193	25.38	17.33	184.6	2019	0.1622	0.6656	0.7119	0.2654	0.4601	0.1189".split()
    # fa = [float(i) for i in a]
    # a = Sample('a', fa)
    # b = "20.57	17.77	132.9	1326	0.08474	0.07864	0.0869	0.07017	0.1812	0.05667	0.5435	0.7339	3.398	74.08	0.005225	0.01308	0.0186	0.0134	0.01389	0.003532	24.99	23.41	158.8	1956	0.1238	0.1866	0.2416	0.186	0.275	0.08902".split()
    # fb = [float(i) for i in b]
    # b = Sample('b', fb)

    print(a)
    print(b)
    print(a + b)
    print(a - b)
    print(a / 2)
    print(a * b)
    print(a.dimensionality())
    print(a.getFeatures())
    print(a.distance(b))

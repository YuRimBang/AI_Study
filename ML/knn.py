import numpy as np
from scipy.spatial import distance
import math as m

class Knn:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def Euclidean(self):
        a = self.a
        b = self.b
        dist = np.linalg.norm(a - b)
        print("넘파이를 이용한 유클리드 거리 ", dist)

        dist = np.sqrt(np.sum(np.square(a -b)))
        print("수학공식을 구현한 유클리드 거리1 ", dist)

        temp = a - b
        dist = np.sqrt(np.dot(temp.T, temp))
        print("수학공식을 구현한 유클리드 거리2 ", dist)

        res = distance.euclidean(a, b)
        print("scipy 라이브러리를 이용한 유클리드 거리 ", res)

        res = m.dist(a,b)
        print("math 모듈을 이용한 유클리드 거리 ", res)

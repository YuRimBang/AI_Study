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

    def Manhattan(self):
        a = self.a
        b = self.b

        dist = np.sum(np.abs(a - b))
        print("넘파이를 이용한 맨해튼 거리 ", dist)

        dist_math = np.abs(a[0] - b[0]) + np.abs(a[1] - b[1])
        print("수학공식을 구현한 맨해튼 거리 ", dist_math)
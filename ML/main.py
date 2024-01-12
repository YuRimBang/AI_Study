import knn
import numpy as np
'''
knn
- 유클리드  거리 계산
'''

#유클리드 거리 계산

a = np.array((1, 2))
b = np.array((4, 5))

myKnn = knn.Knn(a,b)

myKnn.Euclidean()
myKnn.Manhattan()
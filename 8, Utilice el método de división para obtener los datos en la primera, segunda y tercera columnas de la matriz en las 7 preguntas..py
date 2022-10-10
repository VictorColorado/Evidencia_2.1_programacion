
import numpy as np

data7 = np.arange(25).reshape(5,5)
print(data7)

print("------")
print(data7[1,0])
print("------")
print(data7[2,1])

data8 = data7
print(data8)

print("------")
print(data8[0])
print("------")
print(data8[1])
print("------")
print(data8[0:5,1])
print("------")
print(data8[0:5,2])
import numpy as np

data7 = np.arange(25).reshape(5,5)
print(data7)

print("------")
print(data7[1,0])
print("------")
print(data7[2,1])

data9=data7
print(data9)
print("------")
print(data9[1,1:3])

import numpy as np

data4= np.arange(64).reshape(4,4,4)
data4=data4.transpose(2,0,1)

print(data4.dtype.name)
data4.dtype="float32"
print("")
data4.dtype.name


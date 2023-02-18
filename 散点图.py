import matplotlib.pyplot as plt
import numpy as np
# print(plt.rcParams.keys())
plt.rcParams['font.sans-serif']=['SimHei']  # 显示中文

# x=np.random.randint(0,50,(10,))
# y=np.random.randint(0,100,(10,))
# plt.scatter(x,y,marker='*')

price=np.array([1.9,2.8,3.3,4.5,3.8,2.6])
sales=np.array([19,48,38,45,28,66])
profit=(price-1)*sales
plt.scatter(price,sales,marker='o',s=5,c=profit)
cbar=plt.colorbar()
cbar.set_label('利润')
plt.title('销量价格关系')
plt.xlabel('价格')
plt.ylabel('销量')
plt.show()
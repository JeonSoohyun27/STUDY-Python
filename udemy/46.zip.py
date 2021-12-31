days = ['월','화','수','목','금']
fruits = ['사과','바나나','파인애플','오렌지','토마토']
drinks = ['커피','물','홍차','녹차','맥주']

# for i in range(len(days)):
#     print(days[i],fruits[i],drinks[i])

# zip 함수를 이용하면 위처럼 복잡하게 쓰지 않아도 된다.

for day,fruit,drink in zip(days,fruits,drinks):
    print(day,fruit,drink)

i = 0 
for fruit in ['apple','banana','orange']:
    print(i, fruit)
    i += 1

# # enumerate 를 사용할 경우 위처럼 하지 않아도 됨.

for i,fruit in enumerate(['apple','banana','orange']):
    print(i,fruit)
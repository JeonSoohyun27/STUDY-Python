def ss(word,word1,word2):
    print(word,word1,word2)

ss('a','b','c')
# 결과 값 -> a b c

# 인수가 많게 되면 복잡하니 *args 를 사용해서 튜플화 시켜준다.
# 인수가 몇개가 들어 올지 모를때도 써줌

def ss1(*args):
    print(args)

ss1('a','b','c')
# 결과 값 -> ('a', 'b', 'c')

def ss2(**kwargs):
    print(kwargs)

ss2(apple='a',banana='b',carot='c')

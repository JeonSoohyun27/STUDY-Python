def ss2(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

d = {
    'apple':'a',
    'banana':'b',
    'carot':'c'
}
ss2(**d)

def ss2(food,*args,**kwargs):
    print(food)
    print(args)
    print(kwargs)

ss2('banana','apple','pineapple',dinner='soup',disert='coffee')
# ss2('banana',dinner='soup',disert='coffee','apple','pineapple') = X
# * ** 중 * 한개가 먼저 위치해야함.

# 결과값
# banana
# ('apple', 'pineapple')
# {'dinner': 'soup', 'disert': 'coffee'}
# 문자열 포멧
print('a'+'b')
print('a','b')

# 방법1
print('나는 %d살 입니다.'% 20)                                             # d: 정수를 의미
print('나는 %s을 좋아해요' % '파이썬')                                      # s: 문자열을 의미
print('apple은 %c로 시작해요' %'a')                                        # a: 문자를 의미 a-->O, aaa-->X
print('나는 %s색과 %s색을 좋아해요.' %('녹','갈'))  

# 방법2 
print('나는 {}살 입니다.'.format(20))
print('나는 {}색과 {}색을 좋아해요.'.format('갈','녹'))
print('나는 {0}색과 {1}색을 좋아해요'.format('갈','녹'))                     # 숫자를 사용하면 format 순서대로 가능
print('나는 {1}색과 {0}색을 좋아해요'.format('갈','녹'))

# 방법3 
print('나는 {age}살 이며, {color}색을 좋아해요.'.format(age=20,color='녹'))  # 순서에 상관없이 원하는 문장출력

# 방법4
age = 20
color = '빨강'
print(f'나는 {age}살 이며, {color}색을 좋아해요')               
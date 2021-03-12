# 문자열 처리함수
python = 'Python is Amazing'
print(python.lower())                   # .lower: 소문자 출력
print(python.upper())                   # .upper: 대문자 출력
print(python[0].isupper())              # 첫번째 글자가 대문자인가? 알려줌 True
print(len(python))                      # 문자열 전체길이를 반환해줌
print(python.replace('Python','Java'))  # Python이라는 문자를 찾아서 java로 변환

a = python.index('n')                   # index: 어떤 문자가 어느위치에 있는지 확인
print(a)
a = python.index('n', a +1)             # 두번째 n을 찾기위해 index(첫번째n) +1 적용
print(a)

print(python.find('java')   )           # 문자열에는 java가 없으니까 -1이라고 출력이 된다.
'''print(python.index('java'))로 할경우 오류가 생겨 다음문자가 출력이 안된다.'''
print(python.count('n'))                # count: 문자열에 n이 총 몇번 등장하는지 알려줌  
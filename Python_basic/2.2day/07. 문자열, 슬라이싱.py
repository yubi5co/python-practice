# 문자열 
sentence = 'hello world'
print(sentence)
sentence2 = "hello human"
print(sentence2)
sentence3 = '''
it's funny programming
and easy language!!'''
print(sentence3)

# 슬라이싱 
주민번호 = '990120-1234567'

print('성별 :' +주민번호[7])                    # []: 번호의 위치 (순서는 왼쪽에서 오른쪽으로, 0부터이다.)
print('년 :' +주민번호[0:2])                    # [0:2]: 0부터2직전값 까지(0~1)
print('월 :' +주민번호[2:4])   
print('일 :' +주민번호[4:6]) 
print('생년월일 :' + 주민번호[:6])               # [:6]: 처음부터 6직전까지(0~5)
print('뒤 7자리 :' + 주민번호[7:])               # [7:]: 7부터 끝까지(7~)
print('뒤 7자리 (뒤에서 부터) :'+주민번호[-7:])   # 맨 뒤에 7번째부터 끝까지
# 숫자처리함수
print(abs(-5))       # 절대값
print(pow(4,2))      # 4의 2제곱
print(max(1,4,3))    # 최대값
print(min(1,4,3))    # 최소값
print(round(3.14))   # 반올림 '3'
print(round(3.85))   # 반올림 '4'

# 랜덤함수
from random import *

print(random())            # 0.0~1.0 미만의 임의의(랜덤)값을 생성
print(random()*10)         # 0.0~10.0 미만의 임의의 값을 생성
print(int(random()*10))    # 소수점이 보기싫은 경우 int삽입
print(int(random()*10)+1)  # 1~10이하의 임의의 값을 생성 (0을 제거하고싶은 경우사용)

print(randrange(1,46))     # 1~46 미만의 임의의 값 생성
print(randint(1,45))       # 숫자의 양쪽 끝 값 모두를 포함, 1~45이하의 임의의 값 생성

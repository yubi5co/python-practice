# 리스트

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10,20,30]
print(subway)

subway = ['A','B','C']
print(subway)

# B는 몇 번 칸에 타고 있는가?
print(subway.index('B'))                # index : 문자의 위치를 나타냄
# G는 다음 정류장에서 다음 칸에 탐
subway.append('G')                      # append : 특정문자추가
print(subway)
# B와 C사이에 H를 태워봄                 # insert : 특정한 위치에 넣음 
subway.insert(2,'H')
print(subway)
# 지하철에 있는 사람 C를 꺼냄               # pop : 특정 위치의 문자빼기
print(subway.pop(3))
print(subway)
# 같은 이름의 사람이 몇 명 있는지 확인
subway.append('A')
print(subway)
print(subway.count('A'))                # count : 출현횟수확인

# 정렬도 가능
number = [1,5,9,8,7,4,6,3,2]
number.sort()                            # sort : 순서대로 표시
print(number)
# 모두 지우기 
number.clear()                           # clear : 지우기
print(number)

# 다양한 자료형과 함께 사용
numlist = [5,2,6,8,9]
mixlist = ['A',20,'YOU']
numlist.extend(mixlist)                  # extend : 리스트 확장
print(numlist)
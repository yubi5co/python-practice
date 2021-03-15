# 튜플

menu = ('wine','bread')
print(menu[0])
print(menu[1])

name = 'willson'
age = 40
hobby = 'doctor'
print(name,age,hobby)

# 튜플을 이용하면 
(name,age,hobby) = 'willson',40,'doctor'
print(name,age,hobby)



# 집합(set) {}
myset = {1,2,3,3,3}    # 집합은 중복이 안됨, 순서가 없음
print(myset)

java={'gum','world','shine'}
python=set(['gum','desert'])

# 교집합AND 출력 (java와 python을 모두 할수있는 개발자)
print(java & python)                                            # 방법1 &
print(java.intersection(python))                                # 방법2 intersection
# 합집합OR 출력 (java 도 할수있거나, python도 할수있는 개발자)
print(java | python)                                            # 방법1 |
print(java.union(python))                                       # 방법2 union
# 차집합 출력 (java는 할수있지만 python은 할 줄 모르는 개발자)
print(java - python)                                            # 방법1 - 
print(java.difference(python))                                  # 방법2 defference
# python을 할줄아는 사람이 늘어남
python.add('cloud')                                             # add
print(python)
# java를 까먹었어요.                             
java.remove('gum')                                              # remove
print(java)
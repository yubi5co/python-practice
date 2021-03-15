# 사전

# 사물함의 열쇠번호와 사용자가 있다면?
cabinet = {3:'tom',100:'jeak'}
print(cabinet[3])                                # 열쇠번호는 3이고 그 열쇠는 tom이 사용하고 있다. 
                                                 # 3번 열쇠에는 tom의 짐이 들어있다.
print(cabinet[100])                         
print(cabinet.get(3))                            # cabinet[3]과 같은 의미 (오류발생x)

print(3 in cabinet)                              # True
print(5 in cabinet)                              # False

# 새 손님
print(cabinet)
cabinet[3] = 'kel'                               # kel과 tom 교체
cabinet[50] = 'devin'                            
print(cabinet)

# 간 손님
del cabinet[3]                                   # del : 제거
print(cabinet)

# 총 사용중인 key들만 출력
print(cabinet.keys())                            # keys
# value(사용자)들만 출력
print(cabinet.values())                          # values
# key,value 같이출력
print(cabinet.items())                           # items

# 사물함 폐지
cabinet.clear                                    # clear
print(cabinet)
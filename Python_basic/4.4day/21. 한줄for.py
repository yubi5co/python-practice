# 한줄 for

# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 --> 101,102,103,104
student = [1,2,3,4,5]
print(student)
student = [i+100 for i in student]
print(student)

# 학생이름을 길이로 변환
student = ['iron','gaga','willi']
student = [len(i) for i in student]
print(student)

# 학생이름을 대문자로 변환
student = ['iron','gaga','willi']
student = [i.upper() for i in student]
print(student)
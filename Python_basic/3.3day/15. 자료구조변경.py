# 자료구조의 변경

# 커피숍
menu = {'커피','우유','주스'}   # set형식 {} 
print(menu,type(menu))

menu = list(menu)
print(menu,type(menu))         # list형식 []

menu = tuple(menu)              
print(menu,type(menu))         # tuple형식 <>

menu = set(menu)
print(menu,type(menu))         # set형식 {}
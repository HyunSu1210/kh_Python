# a = b = c = 1
# print(a,b,c)
# # 여러개의 정수를 한번에 대입,
# a,b,c = 1,False,"곰돌이사육사"
# print(a,b,c)
#
# # 타입 확인
# age = int(input("나이를 입력하세요 : "))
# print(type(age))

value = 0xffffff
print(value)

# 불리언 타입 : 참과 거짓 중 하나의 값을 가짐
print(bool(1)) # 참
print(bool(0)) # 거짓
print(bool(-1000)) # 참
print(bool("")) # 거짓
print(bool(None)) # 값이 정해지지 않음 : 거짓
val = None

# 문자열 타입
str = "Hello Python!!!"
print(str)
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 3)
print(str + "TEST")

# 형 변환 : 파이썬은 값이 할당되는 순간 형이 결정됨, 이후 변경하고자 할 때 형 변환
print(10 + int("12"))
print("나이 : " ,30)
print(1 + 3.141592 + float("4.44"))



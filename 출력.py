name = "곰돌이사육사"
age = 20
gender = "남성"
jobs = "소프트웨어 개발자"
addr = "서울시 강남구 역삼동"

# C언어 스타일 : 서식 지정자를 사용하는 방식
print("=" * 5, "C 스타일", "=" * 5)
print("이름 : %s" % name)
print("나이 : %d" % (age))
print("성별 : %s" %(gender))
print("직업 : %s"%(jobs))
print("주소 : %s" %addr, end="\n\n")

# 파이썬 스타일 1 : str.format (3.5 이전)
print("=" * 5, "파이썬 스타일 1", "=" * 5)
print("이름 : {}".format(name))
print("나이 : {}".format(age))
print("성별 : {}".format(gender), end="\n\n")

# 파이썬 현재 스타일 : f-string (3.6 이후)
print("=" * 5, "파이썬 현재 스타일", "=" * 5)
print(f"이름 : {name}")
print(f"나이 : {age}")
print(f"성별 : {gender}", end="\n\n")

# 자바 스타일
print("=" * 5, "자바 스타일", "=" * 5)
print("이름 : " + name)
print("나이 :  " + str(age)) # 문자열 결합은 형이 같아야 함
print("주소 : " + addr)

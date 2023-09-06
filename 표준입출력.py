print(38)  # 정수형
print("문자열")  # 문자열
print([1, 2, 3])  # 리스트형
print(1 + 3)
print("파""이""썬")
print("파" + "이" + "썬")  # 문자열 이어붙이기
print("파", "이", "썬")  # 콤마를 구분자라고 부른다. 한칸의 공백을 가지고 있음
print("파\n\n\n이/t/t썬")
print("""동해물과 백두산이 마르고 닳도록 하느님이
보우하사 우리나라 만세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전 하세
""")  # """ ''' 모두 가능. 여러줄 연속 사용

print("안녕하세요라고 \"곰돌이사육사\"가 말했습니다")

print("-------------------------------------------")

# end와 sep 옵션
# end : 출력문에서 끝에 자동으로 삽입되는 문자를 지정. 기본 값은 \n
# sep : 출력문의 중간에 삽입되는 문자를 지정. 기본 값은 space
print("Hello", end="$")
print("Hello", end="*")
print("Hello")
print("life", "is", "too", "short", end="\\")
print("010","1234","5678",sep="-")

year = 2023
month = 9
day = 6

print(year, month, day, sep="/")

# 출력시 정렬
# < 좌측 정렬
# < 우측 정렬, 생략 가능
# ^ 중앙 정렬
print("|{:5}|".format(10))
print("|{:<5}|".format(10))
print("|{:^6}|".format(10))

print(f"|{10:5}|")
print(f"|{10:<5}|")
print(f"|{10:^6}|")
print(f"{20.33333:.2f}")
PI = 3.14159265334655
print(f"{PI:.2f}")


# 문제
# 두 정수(a, b)를 입력받아
# a와 b가 서로 다르면 1을, 그렇지 않으면 0을 출력하는 프로그램을 작성해보자.

# 입력
# 두 정수 a, b가 공백을 두고 입력된다.
# -2147483647 <= a, b <= +2147483648

# 출력
# a와 b가 다른 경우 1을, 그렇지 않은 경우 0을 출력한다.

A, B = input().split()
A = int(A)
B = int(B)

if A != B :
    print(1)
else :
    print(0)
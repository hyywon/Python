
# 문제
# 1, 2, 3 ... 을 순서대로 계속 더해나갈 때,
# 그 합이 입력한 정수보다 작을 동안만 계속 더하는 프로그램을 작성해보자.
# 즉, 1부터 n까지 정수를 계속 더한다고 할 때,
# 어디까지 더해야 입력한 수보다 같거나 커지는지 알아보고자 하는 문제이다.
# 하지만, 이번에는 그 때의 합을 출력해야 한다.
# 예를 들어 57을 입력하면
# 1+2+3+...+8+9+10=55에 다시 11을 더해 66이 될 때,
# 그 값 66이 출력되어야 한다.

# 입력
# 언제까지 합을 계산할 지, 정수 1개를 입력받는다.
# 단, 입력되는 자연수는 100,000,000이하이다.

# 출력
# 1, 2, 3, 4, 5 ... 순서대로 계속 더해가다가, 그 합이 입력된 정수보다 커지거나 같아지는 경우,
# 그때까지의 합을 출력한다.

A = input()
A = int(A)
i = 1
sum = 0

while sum < A:
    sum = sum+i
    i = i+1

print(sum)

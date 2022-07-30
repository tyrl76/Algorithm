# 차이를 최대로
 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	21217	13666	10549	65.017%
# 문제
# N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

# 입력
# 첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.

# 출력
# 첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.

# 예제 입력 1 
# 6
# 20 1 15 8 4 10
# 예제 출력 1 
# 62

# 라이브러리 사용(모든 조합을 tuple 형태로 가져옴)
# from itertools import permutations
# import sys

# n = int(sys.stdin.readline())
# a = list(map(int, sys.stdin.readline().split()))

# per = permutations(a)
# ans = 0

# for i in per:
#     s = 0
#     for j in range(len(i) - 1):
#         s += abs(i[j] - i[j+1])
#     if s > ans:
#         ans = s

# print(ans)

import sys
 
 
def next_permutation(list_a):
    k = -1
    m = -1
 
    # 증가하는 마지막 부분을 가리키는 index k 찾기
    for i in range(len(list_a)-1):
        if list_a[i] < list_a[i+1]:
            k = i
 
    # 전체 내림차순일 경우, 반환
    if k == -1:
        return [-1]
 
    # index k 이후 부분 중 값이 k보다 크면서 가장 멀리 있는 index m 찾기
    for i in range(k, len(list_a)):
        if list_a[k] < list_a[i]:
            m = i
 
    # k와 m의 값 바꾸기
    list_a[k], list_a[m] = list_a[m], list_a[k]
 
    # k index 이후 오름차순 정렬
    list_a = list_a[:k+1] + sorted(list_a[k+1:])
    return list_a
 
 
# 주어진 값 입력 & 정렬
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
 
ans = 0
# 첫 순열 내 값 차이를 더해(s), ans 보다 크면 ans를 update
s = 0
for j in range(len(a) - 1):
    s += abs(a[j] - a[j+1])
if s > ans:
    ans = s
 
arr = a
 
while True:
    arr = next_permutation(arr)
    if arr == [-1]:
        break
    s = 0
 
    # 순열마다 차이를 더해(s), ans 보다 크면 ans를 update
    for j in range(len(arr) - 1):
        s += abs(arr[j] - arr[j+1])
    if s > ans:
        ans = s
 
print(ans)
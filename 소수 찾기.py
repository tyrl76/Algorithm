# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # 소수 찾기
#
# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
#
# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
#
# (1은 소수가 아닙니다.)
#
# 제한 조건
#
# n은 2이상 1000000이하의 자연수입니다.
#
# 입출력 예
#
# n	result
#
# 10	4
#
# 5	3

# ## My code

# +
import math

def solution(n):
    result = []
    for i in range(2, n + 1):
        count = 0
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                count += 1
                break
        if count == 0:
            result.append(i)
    return len(result)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(10))


# -

# ## answers

# +
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,int(n ** 0.5) + 1):
        if i in num:
            num-=set(range(i*i,n+1,i))
    return len(num)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(10))

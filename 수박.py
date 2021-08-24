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

# # 수박수박수박수박수박수?
#
# 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 
#
# 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.
#
# 제한 조건
#
# n은 길이 10,000이하인 자연수입니다.
#
# 입출력 예
#
# n	return
#
# 3	"수박수"
#
# 4	"수박수박"

# ## My code

# +
def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += "수"
        else:
            answer += "박"
    return answer

print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));


# -

# ## answers

# +
def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2)

print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));

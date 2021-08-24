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

# # 문자열을 정수로 바꾸기
#
# 문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.
#
# 제한 조건
#
# s의 길이는 1 이상 5이하입니다.
#
# s의 맨앞에는 부호(+, -)가 올 수 있습니다.
#
# s는 부호와 숫자로만 이루어져있습니다.
#
# s는 "0"으로 시작하지 않습니다.
#
# 입출력 예
#
# 예를들어 str이 "1234"이면 1234를 반환하고, "-1234"이면 -1234를 반환하면 됩니다.
#
# str은 부호(+,-)와 숫자로만 구성되어 있고, 잘못된 값이 입력되는 경우는 없습니다.

# ## My code

# +
def solution(s):
    if "-" in s:
        answer = int(s.replace("-","")) * (-1)
    else:
        answer = int(s)
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(strToInt("-1234"));


# -

# ## answers

# +
def strToInt(str):
    result = 0

    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)

    return result


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(strToInt("-1234"));


# +
def strToInt(str):
    #함수를 완성하세요
    a = int(str)
    return a


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(strToInt("-1234"));

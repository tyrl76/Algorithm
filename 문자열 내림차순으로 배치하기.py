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

# # 문자열 내림차순으로 배치하기
# 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
#
# s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.
#
# 제한 사항
#
# str은 길이 1 이상인 문자열입니다.
#
# 입출력 예
#
# s	return
#
# "Zbcdefg"	"gfedcbZ"

# ## My code

def solution(s):
    answer = []
    result = ""

    for i in s:
        answer.append(i)

    answer.sort(reverse = True)

    for i in answer:
        result += i

    return result


# ## answers

# +
def solution(s):
    return ''.join(sorted(s, reverse=True))

solution("adjZ")

# sorted는 string에 사용 가능

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

# # 이상한 문자 만들기
#
# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
#
# 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.
#
# 제한 사항
#
# 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
#
# 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.
#
# 입출력 예
#
# s	return
#
# "try hello world"	"TrY HeLlO WoRlD"
#
# 입출력 예 설명
#
# "try hello world"는 세 단어 "try", "hello", "world"로 구성되어 있습니다.
#
# 각 단어의 짝수번째 문자를 대문자로, 홀수번째 문자를 소문자로 바꾸면 "TrY", "HeLlO", "WoRlD"입니다. 
#
# 따라서 "TrY HeLlO WoRlD" 를 리턴합니다.

# ## My code

# +
def solution(s):
    result = ""
    count = 0

    for i in s:
        if i != " ":
            if count % 2 == 0:
                result += i.upper()
                count += 1
            else:
                result += i.lower()
                count += 1
        else:
            result += " "
            count = 0

    return result

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(solution("try hello world")));


# -

# ## answers

# +
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(toWeirdCase("try hello world")));


# +
def toWeirdCase(s):
    res = []
    for x in s.split(' '):
        word = ''
        for i in range(len(x)):
            c = x[i].upper() if i % 2 == 0 else x[i].lower()
            word = word + c
        res.append(word)
    return ' '.join(res)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(toWeirdCase("try hello world")));

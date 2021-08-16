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

# # 가운데 글자 가져오기
#
# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
#
# 재한사항
#
# s는 길이가 1 이상, 100이하인 스트링입니다.
#
# 입출력 예
#
# s	return
#
# "abcde"	"c"
#
# "qwer"	"we"

# ## My code

# +
def solution(s):
    length = len(s)
    if length % 2 == 0:
        return s[length//2-1:length//2+1]
    else:
        return s[length//2]
    
print(solution("power"))


# -

# ## answers

# +
def string_middle(str):

    return str[(len(str)-1)//2:len(str)//2+1]

print(string_middle("power"))

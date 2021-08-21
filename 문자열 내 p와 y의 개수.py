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

# # 문자열 내 p와 y의 개수
#
# 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. 
#
# s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 
#
# 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
#
# 예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.
#
# 제한사항
#
# 문자열 s의 길이 : 50 이하의 자연수
#
# 문자열 s는 알파벳으로만 이루어져 있습니다.
#
# 입출력 예
#
# s	answer
#
# "pPoooyY"	true
#
# "Pyy"	false

# ## My code

# +
def solution(s):
    answer = True
    count_p = 0
    count_y = 0

    for i in s:
        if i == "p" or i == "P":
            count_p += 1
        elif i == "y" or i == "Y":
            count_y += 1

    if count_p == count_y:
        return True
    else:
        return False
    
# 아래는 테스트로 출력해 보기 위한 코드입니다.    
print( numPY("pPoooyY") )
print( numPY("Pyy") )
print( numPY("dkqw") )


# -

# ## answers

# +
def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( numPY("pPoooyY") )
print( numPY("Pyy") )
print( numPY("dkqw") )
# -



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

# # 문자열 다루기 기본
#
# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 
#
# 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.
#
# 제한 사항
#
# s는 길이 1 이상, 길이 8 이하인 문자열입니다.
#
# 입출력 예
#
# s	return
#
# "a234"	false
#
# "1234"	true

# ## My code

def solution(s):
    number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    count = 0

    if len(s) != 4 and len(s) != 6:
        return False

    for i in s:
        if i in number:
            count += 1
    if count == len(s):
        return True    
    else:
        return False


# ## answers

def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)


def alpha_string46(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6 

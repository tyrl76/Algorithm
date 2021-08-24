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

# # 시저 암호
#
# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다.
#
# 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다.
#
# 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.
#
# 제한 조건
#
# 공백은 아무리 밀어도 공백입니다.
#
# s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
#
# s의 길이는 8000이하입니다.
#
# n은 1 이상, 25이하인 자연수입니다.
#
# 입출력 예
#
# s n result
#
# "AB" 1 "BC"
#
# "z" 1 "a"
#
# "a B z" 4 "e F d"

# ## My code

# +
def solution(s, n):
    s_code = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f": 6, "g" : 7, "h" : 8, "i" : 9, "j" : 10, "k" : 11, "l" : 12, "m" : 13, "n" : 14, "o" : 15, "p" : 16, "q" : 17, "r" : 18, "s" : 19, "t" : 20, "u" : 21, "v" : 22, "w" : 23, "x" : 24, "y" : 25, "z" : 26}
    b_code = {"A" : 52, "B" : 53, "C" : 54, "D" : 55, "E" : 56, "F": 57, "G" : 58, "H" : 59, "I" : 60, "J" : 61, "K" : 62, "L" : 63, "M" : 64, "N" : 65, "O" : 66, "P" : 67, "Q" : 68, "R" : 69, "S" : 70, "T" : 71, "U" : 72, "V" : 73, "W" : 74, "X" : 75, "Y" : 76, "Z" : 77}
    trans_code = []
    result = ""

    for i in s:
        if i in s_code:
            trans_code.append(s_code[i] + n)
        elif i in b_code:
            trans_code.append(b_code[i] + n)
        else:
            trans_code.append(0)

    rs_code = {v:k for k,v in s_code.items()}
    rb_code = {v:k for k,v in b_code.items()}

    for i in trans_code:
        if i == 0:
            result += " "
        elif i < 52:
            if i <= 26:
                result += rs_code[i]
            else:
                result += rs_code[i - 26]
        else:
            if i <= 77:
                result += rb_code[i]
            else:
                result += rb_code[i - 26]

    return result

# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + solution("a B z", 4))


# -

# ## answers

# +
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
    # 주어진 문장을 암호화하여 반환하세요.


# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))


# -

def caesar(s, n):
    lower_list = "abcdefghijklmnopqrstuvwxyz"
    upper_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = []

    for i in s:
        if i is " ":
            result.append(" ")
        elif i.islower() is True:
            new_ = lower_list.find(i) + n
            result.append(lower_list[new_ % 26])
        else:
            new_ = upper_list.find(i) + n
            result.append(upper_list[new_ % 26])
    return "".join(result)

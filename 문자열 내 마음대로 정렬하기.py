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

# # 문자열 내 마음대로 정렬하기
#
# 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차
# 순 정렬하려 합니다. 
#
# 예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.
#
# 제한 조건
#
# strings는 길이 1 이상, 50이하인 배열입니다.
#
# strings의 원소는 소문자 알파벳으로 이루어져 있습니다.
#
# strings의 원소는 길이 1 이상, 100이하인 문자열입니다.
#
# 모든 strings의 원소의 길이는 n보다 큽니다.
#
# 인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.
#
# 입출력 예
#
# strings	n	return
#
# ["sun", "bed", "car"]	1	["car", "bed", "sun"]
#
# ["abce", "abcd", "cdx"]	2	["abcd", "abce", "cdx"]

# ## My code

def solution(strings, n):
    strings.sort()
    strings.sort(key = lambda x : x[n])
    return strings


# ## answers

# +
def strange_sort(strings, n):
    def sortkey(x):
        return x[n]
    strings.sort(key=sortkey)
    return strings

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( strange_sort(["sun", "bed", "car"], 1) )

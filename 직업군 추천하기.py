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

# # 직업군 추천하기
#
#
# 개발자가 사용하는 언어와 언어 선호도를 입력하면 그에 맞는 직업군을 추천해주는 알고리즘을 개발하려고 합니다.
#
# 아래 표는 5개 직업군 별로 많이 사용하는 5개 언어에 직업군 언어 점수를 부여한 표입니다.
#
# 점수	SI	CONTENTS	HARDWARE	PORTAL	GAME
#
# 5	JAVA	JAVASCRIPT	C	JAVA	C++
#
# 4	JAVASCRIPT	JAVA	C++	JAVASCRIPT	C#
#
# 3	SQL	PYTHON	PYTHON	PYTHON	JAVASCRIPT
#
# 2	PYTHON	SQL	JAVA	KOTLIN	C
#
# 1	C#	C++	JAVASCRIPT	PHP	JAVA
#
# 예를 들면, SQL의 SI 직업군 언어 점수는 3점이지만 CONTENTS 직업군 언어 점수는 2점입니다. 
#
# SQL의 HARDWARE, PORTAL, GAME 직업군 언어 점수는 0점입니다.
#
# 직업군 언어 점수를 정리한 문자열 배열 table, 개발자가 사용하는 언어를 담은 문자열 배열 languages, 언어 선호도를 담은 정수 배열 preference가 매개변수로 주어집니다. 
#
# 개발자가 사용하는 언어의 언어 선호도 x 직업군 언어 점수의 총합이 가장 높은 직업군을 return 하도록 solution 함수를 완성해주세요. 
#
# 총합이 같은 직업군이 여러 개일 경우, 이름이 사전 순으로 가장 빠른 직업군을 return 해주세요.
#
# 제한사항
#
# table의 길이 = 5
#
# table의 원소는 "직업군 5점언어 4점언어 3점언어 2점언어 1점언어"형식의 문자열입니다. 
#
# 직업군, 5점언어, 4언어, 3점언어, 2점언어, 1점언어는 하나의 공백으로 구분되어 있습니다.
#
# table은 모든 테스트케이스에서 동일합니다.
#
# 1 ≤ languages의 길이 ≤ 9
#
# languages의 원소는 "JAVA", "JAVASCRIPT", "C", "C++" ,"C#" , "SQL", "PYTHON", "KOTLIN", "PHP" 중 한 개 이상으로 이루어져 있습니다.
#
# languages의 원소는 중복되지 않습니다.
#
# preference의 길이 = languages의 길이
#
# 1 ≤ preference의 원소 ≤ 10
#
# preference의 i번째 원소는 languages의 i번째 원소의 언어 선호도입니다.
#
# return 할 문자열은 "SI", "CONTENTS", "HARDWARE", "PORTAL", "GAME" 중 하나입니다.
#
# 입출력 예
#
# table	languages	preference	result
#
# ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]	["PYTHON", "C++", "SQL"]	[7, 5, 5]	"HARDWARE"
#
#
# ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]	["JAVA", "JAVASCRIPT"]	[7, 5]	"PORTAL"

# ## My code

def solution(table, languages, preference):
    re_table = []
    score = []
    result = [0, 0, 0, 0, 0]
    job = []
    same = []
    determin = [0, 4, 3, 1, 2] # 사전순으로 점수 설정

    for i in table:
        re_table += i.split()

    for i in range(len(re_table)):
        if i % 6 == 0:
            job.append(re_table[i])

    for i in range(len(languages)):
        for j in range(len(table)):
            if languages[i] in re_table[6 * j : 6 * (j + 1)]:
                cal = - (re_table[6 * j : 6 * (j + 1)].index(languages[i])) + 6
                score.append(cal * preference[i])
            else:
                score.append(0)

    for i in range(len(score)):
        for j in range(len(table)):
            if i % 5 == j:
                result[j] += score[i]

    while result.count(max(result)) != 1:
        temp = result.index(max(result))
        result[temp] = 0
        same.append(temp)

    same.append(result.index(max(result)))

    if len(same) != 1:
        if 1 in same:
            return job[1]   
        elif 2 in same:
            return job[2]
        elif 4 in same:
            return job[4]
        else:
            return job[3]
    else:
        return job[same[0]]


# ## answers

def solution(table, languages, preference):
    score = {}
    for t in table:
        for lang, pref in zip(languages, preference):
            if lang in t.split():
                score[t.split()[0]] = score.get(t.split()[0], 0) +  (6 - t.split().index(lang)) * pref
    return sorted(score.items(), key = lambda item: [-item[1], item[0]])[0][0]


def solution(table, languages, preference):
    answer = 'ZZZZZZZZ'
    score_dic = {lang: score for lang, score in zip(languages, preference)}
    max_score = 0
    for row in table:
        r = row.split(' ')
        curr_score = 0
        for i in range(1, len(r)):
            curr_score += score_dic.get(r[i], 0) * (6-i)
        if max_score < curr_score:
            max_score = curr_score
            answer = r[0]
        elif max_score == curr_score and answer > r[0]:
            answer = r[0]


    return answer

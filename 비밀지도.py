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

# # 비밀지도
#
# 네오는 평소 프로도가 비상금을 숨겨놓는 장소를 알려줄 비밀지도를 손에 넣었다. 
#
# 그런데 이 비밀지도는 숫자로 암호화되어 있어 위치를 확인하기 위해서는 암호를 해독해야 한다. 
#
# 다행히 지도 암호를 해독할 방법을 적어놓은 메모도 함께 발견했다.
#
# 지도는 한 변의 길이가 n인 정사각형 배열 형태로, 각 칸은 "공백"(" ") 또는 "벽"("#") 두 종류로 이루어져 있다.
#
# 전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있다. 각각 "지도 1"과 "지도 2"라고 하자.
#
# 지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다. 지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.
#
# "지도 1"과 "지도 2"는 각각 정수 배열로 암호화되어 있다.
#
# 암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열이다.

# <img src="images/secret8.png" height="100px" width="500px" align="left">

# 입력 형식
#
# 입력으로 지도의 한 변 크기 n 과 2개의 정수 배열 arr1, arr2가 들어온다.
#
# 1 ≦ n ≦ 16
#
# arr1, arr2는 길이 n인 정수 배열로 주어진다.
#
# 정수 배열의 각 원소 x를 이진수로 변환했을 때의 길이는 n 이하이다. 즉, 0 ≦ x ≦ 2n - 1을 만족한다.
#
# 출력 형식
#
# 원래의 비밀지도를 해독하여 '#', 공백으로 구성된 문자열 배열로 출력하라.
#
# 입출력 예제
#
# 매개변수	값
#
# n	5
#
# arr1	[9, 20, 28, 18, 11]
#
# arr2	[30, 1, 21, 17, 28]
#
# 출력	["#####","# # #", "### #", "# ##", "#####"]
#
# 매개변수	값
#
# n	6
#
# arr1	[46, 33, 33 ,22, 31, 50]
#
# arr2	[27 ,56, 19, 14, 14, 10]
#
# 출력	["######", "### #", "## ##", " #### ", " #####", "### # "]

# ## My code

# +
def binary(n, i):
    result = []
    while True:
        result.append(i % 2)
        i = i // 2
        if i == 0:
            break
    while len(result) != n:
        result.append(0)
    result.reverse()
    return result


def solution(n, arr1, arr2):
    binary_list1 = []
    binary_list2 = []
    trans_list = []

    for i in arr1:
        binary_list1.append(binary(n, i))

    for i in arr2:
        binary_list2.append(binary(n, i))

    for i in range(n):
        temp = ""
        for j in range(n):
            if binary_list1[i][j] + binary_list2[i][j] != 0:
                temp += "#"
            else:
                temp += " "
        trans_list.append(temp)

    return trans_list


# -

# ## answers

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer


def solution(n, arr1, arr2) :
    result = []

    for j in range(0,len(arr1)) :
        ret = ''
        num = arr1[j] | arr2[j]

        for i in range(0, n) :
            if num % 2 == 0 :
                ret = ' ' + ret

            else : 
                ret = '#' + ret

            num = int(num / 2)

        result.append(ret)

    return result

# https://school.programmers.co.kr/learn/courses/30/lessons/17681

from dataclasses import replace


arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
n = 5

def solution(n, arr1, arr2):
    result = []
    for a1, a2 in zip(arr1, arr2):
        a12 = str(bin(a1 | a2)[2:])
        a12 = a12.replace("1", "#")
        a12 = a12.replace("0", " ")
        result.append(a12)
    print(result)
solution(n, arr1, arr2)

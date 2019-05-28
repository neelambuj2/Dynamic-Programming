# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import datetime


def solution(E, L):
    # write your code in Python 3.6
    sh, sm = E.split(":")
    eh, em = L.split(":")
    sh = int(sh)
    sm = int(sm)
    eh = int(eh)
    em = int(em)
    sum = 5
    st = sh*60+sm
    et = eh*60+em
    diff = et-st
    hr = int(diff / 60)
    min = diff%60
    print(hr, min)
solution("10:00","13:21")


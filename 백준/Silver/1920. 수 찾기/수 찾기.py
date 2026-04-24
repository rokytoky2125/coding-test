import sys
input = sys.stdin.readline

N = int(input())
A = set(input().split()) # A: 집합
M = input()
mlst = input().split()
for i in mlst:
    print(1 if i in A else 0)

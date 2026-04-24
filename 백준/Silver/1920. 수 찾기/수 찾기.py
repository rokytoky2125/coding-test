import sys
input = sys.stdin.readline

n = int(input())
nlst = set(input().split())
m = int(input())
mlst = input().split()

for i in mlst:
    print(1 if i in nlst else 0)

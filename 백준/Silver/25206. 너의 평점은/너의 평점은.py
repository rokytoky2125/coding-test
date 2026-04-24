#전공평점 = 전공과목별 (학점*과목평점)의 합 / 학점 총합
score_dict = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}
subject = []
hak = [] #학점
score = [] #과목평점
hak_score = [] #학점 * 과목평점
for i in range(20):
    a, b, c = input().split()
    if c == "P":
        continue
    b = float(b)
    s = score_dict[c]
    
    subject.append(a)
    hak.append(b)
    score.append(s)
    hak_score.append(b * s)
if sum(hak) == 0:
    print("0.000000")
else:
    print(f"{sum(hak_score) / sum(hak):.6f}")


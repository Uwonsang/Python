kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

student_score = [0, 0, 0, 0, 0]
i = 0
for subject in midterm_score: #각 학생마다 개별로 교과 점수를 저장
    print(subject)
    for score in subject: # 학생 index 구분
        student_score[i] += score # 과목이 바뀔 때 학생 인덱스 초기화
        i += 1
    i = 0
else:
    a, b, c, d, e = student_score
    student_average = [a/3,b/3,c/3,d/3,e/3]
    print (student_average)

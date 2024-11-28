n=int(input())
mark=[]
for i in range (n):
        name=input()
        grade=float(input())
        mark.append((name,grade))
     
grades=sorted({student[1] for student in mark},reverse=True)
if len(grades)>=2:
    sec_low_stu=grades[-2]

    sec_low_stus=sorted([student[0] for student in mark if student[1]==sec_low_stu])
    for name in sec_low_stus:
        print(name)
else:
     print("Nothing to show!")
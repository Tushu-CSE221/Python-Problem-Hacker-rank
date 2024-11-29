n = int(input())
stu_score = {}

# Loop to get student data
for _ in range(n):
   data=input().split()
   name=data[0]
   marks=list(map(float,data[1:]))
   stu_score[name] = marks  # Assign marks to the student
st=input()
avg=(sum(stu_score[st])/len(stu_score[st]))
print(f"{avg:.2f}")

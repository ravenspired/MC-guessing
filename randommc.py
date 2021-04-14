import random
import statistics



quiz = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
scantron = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
confidence = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
done = 0
totals = [0, 0, 0, 0]
options = ["A", "B", "C", "D"]

avg = []
print("running tests")


def gradeScantron():
  grade = 0
  maxGrade = len(quiz)
  for g in range(len(quiz)):
    if scantron[g] == quiz[g]:
      grade+=1
    print("Grade: "+str(grade)+"/"+str(maxGrade))


def generateQuiz():
  for i in range(24):
    quiz[i] = random.choice(options)
  print(str(quiz))
  


generateQuiz()

for x in range(len(quiz)):
  if confidence[x] == 1:
    scantron[x] = quiz[x]
    if quiz[x] == "A":
      totals[0]+=1
    if quiz[x] == "B":
      totals[1]+=1
    if quiz[x] == "C":
      totals[2]+=1
    if quiz[x] == "D":
      totals[3]+=1
  else:
    
    scantron[x] = random.choice(options)
    
  gradeScantron()





marks = {'english': 10 , 'nepali' : 20, 'science' : 30 , 'social' : 40 , 'math' : 50}
print(marks.keys())
#sum =0
#for marks in marks.values():
  #  sum += marks
   # print(sum)
    marks["english"] +=5
    print(marks.values())
for subject in marks.keys():
    marks[subject] += 5
    print(marks.values())

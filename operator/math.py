scores = [45,67,82,56,91,38,74,60,49,88]
def class_grade(scores):
   total = 0
   for score in scores:
      total = total + score
   average = total / len(scores)
   return average
result = class_grade(scores)
print("AVERAGE",result)
print("HIGHEST",max(scores))
print("LOWEST",min(scores))
for score in scores:
 if score >= 50:
   print("PASS")
 else:
   print("FAIL")
passed = 0
failed = 0
for score in scores:
  if score >= 50:
    passed += 1
    print("Passed :",passed)
  else:
    failed += 1
    print("Failed :",failed)


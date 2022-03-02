string = "Practice Problems to Drill List Comprehension in Your Head."

words = string.split()

dict1 = {}
for i in words:
    if not dict1.get(i):
        dict1[i] = 1
    else:
        dict1[i] += 1
print(dict1)
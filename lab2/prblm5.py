string = "Practice Problems to Drill List Comprehension in Your Head."
L1 = string.split()
print(L1)

List2 = [words for words in L1 if len(words) < 5]
print(List2) 
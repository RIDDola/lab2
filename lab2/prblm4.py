String = "Practice Problems to Drill List Comprehension in Your Head."

def rem_vowel(String):
    vowels = ['a','e','i','o','u'] 
    return ''.join([i for i in String if i not in vowels]) 
n = rem_vowel(String)
print(n)
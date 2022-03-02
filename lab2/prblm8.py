nested_list = [max([i for i in range(1,10) if num % i == 0]) for num in range(1,1001) ]
print(nested_list)
print(len(nested_list))

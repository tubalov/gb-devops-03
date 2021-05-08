n = input('Введите целое положительное число: ')

# короткий вариант
max_d = max(map(int, n))
print(max_d)

# вариант с while
i = 0
max = n[0]
while i < len(n) - 1:
    if n[i] < n[i+1]:
        max = n[i+1]
    i +=1
print(max)
first_dist = int(input('Количество км за первый день: '))
n_dist = int(input('Количество км за n день: '))


day_num = 1
middle_dist = first_dist
while middle_dist <= n_dist:
    middle_dist = middle_dist + middle_dist * 0.1
    day_num +=1
print(day_num)

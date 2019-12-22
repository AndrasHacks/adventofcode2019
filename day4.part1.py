min = 246540
max = 787419

def is_not_decreasing(num):
    s = str(num)
    prev_index = 0
    for i in range(1, len(s)):
        if s[prev_index] > s[i]:
            return False
        prev_index = i
    return True

# print(is_not_decreasing(111111))

def get_groups(num):
    s = str(num)
    groups = []
    group = []
    in_group = False
    for index in range(len(s) - 1):
        if s[index] == s[index + 1]:
            in_group = True
            group.append(s[index])
        if s[index] != s[index + 1] and in_group:
            group.append(s[index])
            in_group = False
            groups.append(group)
            group = []
        elif index == len(s) - 2 and in_group:
            in_group = False
            group.append(s[index])
            groups.append(group)
    return groups

# print(get_groups(111122))
# print(get_groups(123444))
# print(map(lambda item: len(item), get_groups(122334)))

def has_group_of_two(num):
    groups = get_groups(num)
    len_of_groups = map(lambda item: len(item), groups)
    for i in range(len(len_of_groups)):
        if len_of_groups[i] == 2:
            return True
    return False

c = 0
for i in range(min + 1, max):
    if is_not_decreasing(i) and has_group_of_two(i):
        c += 1

print(c)


list1 = []
list2 = []
with open("day-1/input.txt") as f:
    for line in f:
        a, b = line.split()
        list1.append(int(a))
        list2.append(int(b))

def total_distance_calculator():
    list1.sort()
    list2.sort()

    total_distance = 0
    for i in range(len(list1)):
        total_distance += abs(list1[i] - list2[i])

    return total_distance

#part one: 
print(total_distance_calculator()) #2970687

def calculate_similarity_score():
    similarity_score = 0
    numbers_map = {}
    for number in list2:
        if number not in numbers_map:
            numbers_map[number] = 1
        else:
            numbers_map[number] += 1
    
    for number in list1:
        if number in numbers_map:
            count = number * numbers_map[number]
            similarity_score += count

    return similarity_score

#part two:
print(calculate_similarity_score()) #23963899

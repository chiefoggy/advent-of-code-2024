lis = []
with open("day-2/input.txt") as f:
    for line in f:
        lis.append(list(map(int, line.split())))

def is_good(report):
    inc_or_dec = (report==sorted(report) or report==sorted(report, reverse=True))
    check = True
    for i in range(1, len(report)):
        diff = report[i] - report[i-1]
        if abs(diff) > 3 or abs(diff) < 1:
            check = False
            break
    return inc_or_dec and check

p1, p2 = 0, 0
for report in lis:
    if is_good(report):
        p1 += 1
    
    good = False
    for i in range(len(report)):
        new_lst = report[:i] + report[i+1:]
        if is_good(new_lst):
            good = True
            break
    if good:
        p2 += 1

print(p1)
print(p2)
    

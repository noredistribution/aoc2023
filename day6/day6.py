with open("input.txt", "r") as f:
    data = f.read()

test_data = """Time:      7  15   30
Distance:  9  40  200"""

def parse_data(data: list) -> list:
    '''Parses the data.'''
    t = data.splitlines()[0].split(':')[1].split()
    d = data.splitlines()[1].split(':')[1].split()
    t = [int(i) for i in t]
    d = [int(i) for i in d]
    return t, d

def margin_error(t: list, d: list) -> int:
    '''Calculates the margin of error.'''
    margin = 1
    for ctr, ti in enumerate(t):
        record = []
        for i in range(1,ti+1):
            distance = i*(ti-i)
            if distance > d[ctr]:
                record.append(distance)
        margin = margin * len(record)
    return margin

# beat = 1
# for ctr, ti in enumerate(t):
#     record = []
#     for i in range(1,ti+1):
#         distance = i*(ti-i)
#         if distance > d[ctr]:
#             record.append(distance)
#     beat = beat* len(record)
t, d = parse_data(test_data)
print(margin_error(t, d))

t, d = parse_data(data)
print(margin_error(t, d))
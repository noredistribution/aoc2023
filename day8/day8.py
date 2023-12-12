with open("input.txt", "r") as f:
    data = f.read()

test_data = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

def parse_data(data: str) -> list:
    '''Parses the data.'''
    mapdata = data.splitlines()
    instructions = mapdata[0]
    mapdata.pop(0)
    mapdata.pop(0)
    mapDict = {}
    for i in mapdata:
        temp = i.split("=")
        mapDict[temp[0].strip()] = {"L": temp[1].strip().split(",")[0].strip().replace("(",""), "R": temp[1].strip().split(",")[1].strip().replace(")","")}
    return mapDict, instructions

def direction_sequence(instructions) -> str:
    sequence = instructions
    while True:
        for direction in sequence:
            yield direction

print("====Test data====")
mapDict, instructions  = parse_data(test_data)

position = 'AAA'
counter = 0
instruction = direction_sequence(instructions)
while position != 'ZZZ':
    position = mapDict[position]["L"] if next(instruction) == 'L' else mapDict[position]["R"]
    counter +=1

print(counter)

print("\n\n====Input====")
mapDict, instructions  = parse_data(data)

position = 'AAA'
counter = 0
instruction = direction_sequence(instructions)
while position != 'ZZZ':
    position = mapDict[position]["L"] if next(instruction) == 'L' else mapDict[position]["R"]
    counter +=1

print(counter)
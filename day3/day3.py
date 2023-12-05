import re

def parse_data(data: str) -> list:
    pattern = r'[^\w.]'
    sum_numbers = 0
    for row,column in enumerate(data):

        numbers_in_row = re.finditer(r"\d+", column)
        for number in numbers_in_row:
            start = number.start()
            end = number.end()
            if start > 0 and end < len(column) -1:
                current = data[row][start-1:end+1]
            if start == 0:
                current = data[row][start:end+1]
            if end == len(column)-1:
                current = data[row][start-1:end]
            if row > 0 and len(data)-1 > row:
                if end < len(column)-1 and start > 0:
                    above = data[row-1][start-1:end+1]
                    below = data[row+1][start-1:end+1]
                if end < len(column)-1 and start == 0:
                    above = data[row-1][start:end+1]
                    below = data[row+1][start:end+1]
                if end == len(column)-1 and start > 0:
                    above = data[row-1][start-1:end]
                    below = data[row+1][start-1:end]
            if row == 0:
                if start > 0 and end < len(column) -1:
                    below = data[row+1][start-1:end+1]
                if start == 0:
                    below = data[row+1][start:end+1]
                if start > 0 and end == len(column)-1:
                    below = data[row+1][start-1:end]
            if row == len(data)-1:
                if start > 0 and end < len(column) -1:
                    above = data[row-1][start-1:end+1]
                if start == 0:
                    above = data[row-1][start:end+1]
                if start > 0 and end == len(column)-1:
                    above = data[row-1][start-1:end]
            try:
                find_current = re.findall(pattern, current)
                # print(f"on current row: {find_current}")
            except:
                find_current = None
                pass
            try:
                find_above = re.findall(pattern, above)
                # print(f"on above row:{find_above}")
            except:
                find_above = None
                pass
            try:
                find_below = re.findall(pattern, below)
                #print(f"on below row: {find_below}")
            except:
                find_below = None
                pass

            if (find_current is not None and len(find_current)>0) or (find_above is not None and len(find_above)>0) or (find_below is not None and len(find_below)>0):
                #print(number.group(0))
                sum_numbers += int(number.group(0))
    return sum_numbers


test_data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

with open("input.txt", "r") as f:
    data = f.readlines()


result_test = parse_data(test_data.splitlines())
result = parse_data(data)

print(f"What is the sum of all of the part numbers in the engine schematic for test data?: {result_test}")
print(f"What is the sum of all of the part numbers in the engine schematic?: {result}")


from pprint import pprint as pp
from copy import deepcopy
import re
with open("input.txt", "r") as f:
    data = f.read()

test_data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

def seed_mapper(seedno: int, data: list) -> int:
    #print(data)
    for dst, src, length in data:
        if src <= seedno <= src+length:
            return seedno - src + dst
    return seedno


def parse_data(data:list):
    '''Parses the data.'''
    seeds = []
    maps = []
    submap = []

    for line in data.splitlines():
        if "seeds:" in line:
            seeds = [int(i) for i in line.split(':')[1].split()]
        # pass on empty line
        elif len(line) == 0:
            pass
        elif "map" in line:
            if len(submap) != 0:
                maps.append(deepcopy(submap))
                submap.clear()
        else:
            submap.append([int(i) for i in re.findall(r'\d+', line)])

    maps.append(deepcopy(submap))
    return seeds, maps

def find_lowest_location(seeds:list, maps:list)->int:
    locations = []
    for seed in seeds:
        temp = seed
        for m in maps:
            temp = seed_mapper(temp, m)
        # we only need to append the last value as that's the location
        locations.append(temp)
    return min(locations)

def reseed(seeds:list)->list:
    '''Reseeds the seeds.'''
    new_seed_list = []
    for i in range(0,len(seeds),2):
        new_seed_list += list(range(seeds[i],seeds[i]+seeds[i+1]))
    return new_seed_list

seed_data = test_data#.splitlines()

seeds, maps = parse_data(seed_data)
print(maps)
print(find_lowest_location(seeds, maps))

new_seed_list = reseed(seeds)
print(find_lowest_location(new_seed_list, maps))

seeds2, maps2 = parse_data(data)
print(find_lowest_location(seeds2, maps2))
new_seed_list = reseed(seeds2)
print(find_lowest_location(new_seed_list, maps2))



#print(seed_data)
#pp(parse_data(seed_data))


from functools import reduce


def hamming_distance(genome_1: str, genome_2: str) -> int:
    return reduce(lambda x, y: x + 1 if not len(set(y)) == 1 else x, zip(genome_1, genome_2), 0)


def neighbours_build(pattern: str, suffix: str, suffix_neighbours: set, max_distance: int) -> set:
    neighborhood = set()
    for neighbour in suffix_neighbours:
        if hamming_distance(suffix, neighbour) < max_distance:
            neighborhood.update({x + neighbour for x in {'A', 'C', 'G', 'T'}})
        else:
            neighborhood.update({pattern[0] + neighbour})
    return neighborhood


def neighbours(pattern: str, max_distance: int) -> list:
    if max_distance == 0:
        return [pattern]
    elif max_distance > 0 and len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    else:
        suffix = pattern[1:]
        suffix_neighbours = neighbours(suffix, max_distance)
    return neighbours_build(pattern, suffix, suffix_neighbours, max_distance)


if __name__ == "__main__":
    print(*sorted(neighbours(input(), int(input()))), sep='\n')
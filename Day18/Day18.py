import copy

def load(path: str):
    return list(map(eval, open(path).read().splitlines()))

def add_left(d, i, l, r):
    if isinstance(d[i], int):
        d[i] += l
        l = 0
    else:
        d[i], l, r = reduce_snail_number(d[i], 0, l, r, False)
    return d, l, r

def add_right(d, i, l, r):
    if isinstance(d[i], int):
        d[i] += r
        r = 0
    else:
        d[i], l, r = reduce_snail_number(d[i], 0, l, r, False)
    return d, l, r

def reduce_snail_number(d: list, depth: int, l: int, r: int, do_split: bool):
    # Just return if l and r are 0
    if l==0 and r==0:
        return d, l, r
    # Something happened elsewhere and a place for l is being found
    if l!=-1:
        return add_left(d, 1, l, r)
    # Something happened elsewhere and a place for r is being found
    if r!=-1:
        return add_right(d, 0, l, r)
    # Explosion time!
    if l==-1 and r==-1  and isinstance(d[0], int) and isinstance(d[1], int) and depth >= 4:
        return 0, d[0], d[1]
    # Check overflow Left
    if do_split and isinstance(d[0], int) and d[0] > 9:
        d[0] = [d[0]//2, int(d[0]/2+0.5)]
        return d, 0, 0
    # Go deeper left position
    elif not isinstance(d[0], int):
        d[0], l, r = reduce_snail_number(d[0], depth + 1, l, r, do_split)
        if r>-1:
            d, _, r = add_right(d, 1, -1, r) # Need to retain l
            return d, l, r
    # Check overflow right
    if do_split and isinstance(d[1], int) and d[1] > 9:
        d[1] = [d[1]//2, int(d[1]/2+0.5)]
        return d, 0, 0
    # Go deeper right position
    if not isinstance(d[1], int):
        d[1], l, r = reduce_snail_number(d[1], depth + 1, l, r, do_split)
        if l>-1:
            return add_left(d, 0, l, r)
    return d, l, r

def do_snail_calculus(data: list) -> list:
    d = copy.deepcopy(data)
    for i in range(len(d)):
        if i == 0:
            result = d[i]
        else:
            result = [result, d[i]]
        l, r = 0, 0
        while l>-1 and r>-1:
            result, l, r = reduce_snail_number(result, 0, -1, -1, False)
            if l==-1 and r==-1:
                result, l, r = reduce_snail_number(result, 0, -1, -1, True)
    return result

def calc_mag(d: list) -> int:
    c = 0
    if not isinstance(d[0], int):
        c += 3*calc_mag(d[0])
    else:
        c +=3*d[0]
    if not isinstance(d[1], int):
        c += 2 * calc_mag(d[1])
    else:
        c += 2 * d[1]
    return c

def largest_magnitude_pair(d: list) -> int:
    l = []
    for i in range(len(d)):
        for j in range(len(d)):
            result = do_snail_calculus([d[i], d[j]])
            l.append(calc_mag(result))
    return max(l)

def do_tests() -> None:
    # Simple addition
    assert do_snail_calculus(load('test_SAdd.txt')) == [[[[1,1],[2,2]],[3,3]],[4,4]]
    # Explosions!
    assert do_snail_calculus(load('Test_ELeft.txt')) == [[[[3,0],[5,3]],[4,4]],[5,5]] # Left explosion
    assert do_snail_calculus([[7,[6,[5,[4,[3,2]]]]]]) == [7,[6,[5,[7,0]]]] # Right explosion
    assert do_snail_calculus([[[6,[5,[4,[3,2]]]],1]]) == [[6,[5,[7,0]]],3] # Middle
    assert do_snail_calculus([[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]]) == [[3,[2,[8,0]]],[9,[5,[7,0]]]] # More complicated
    # Split (and some explosions) test
    assert do_snail_calculus(load('test_Split.txt')) == [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
    # Large Test
    assert do_snail_calculus(load('Test_Large.txt')) == [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]
    # Magnitude
    assert calc_mag([9,1]) == 29
    assert calc_mag([[9,1],[1,9]]) == 129
    assert calc_mag([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]) == 3488
    # Magnitude any pair sum
    data = load('HomeWork.txt')
    assert largest_magnitude_pair(data) == 3993

    print('Tests complete')

def main() -> None:
    do_tests()

    data = load('data.txt')
    result = do_snail_calculus(data)
    print('Part 1: ' + str(calc_mag(result)))
    print('Part 2: ' + str(largest_magnitude_pair(data)))


if __name__ == "__main__":
    main()
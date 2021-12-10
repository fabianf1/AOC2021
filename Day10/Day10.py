from statistics import median

def load_data(path: str) -> list:
    return [list(line) for line in open(path).read().strip().splitlines()]

def check_illegal(line: list, list_return: bool):
    q = []
    for c in line:
        if c in '([{<':
            q.append(c)
        else:
            cm = q.pop(-1)
            if   c == ')' and cm != '(': return 3
            elif c == ']' and cm != '[': return 57
            elif c == '}' and cm != '{': return 1197
            elif c == '>' and cm != '<': return 25137
    if list_return:
        return q
    return 0

def syntax_score(d: list) -> int:
    count = 0
    for line in d:
        count += check_illegal(line, False)
    return count

def auto_score(d: list) -> int:
    l = []
    for line in d:
        q = check_illegal(line, True)
        if isinstance(q, list):
            count = 0
            for c in q[::-1]:
                if   c == '(': count = count * 5 + 1
                elif c == '[': count = count * 5 + 2
                elif c == '{': count = count * 5 + 3
                elif c == '<': count = count * 5 + 4
            l.append(count)
    return median(l)

def main() -> None:
    # Load data
    test = load_data('test.txt')
    data = load_data('data.txt')
    # Part 1
    assert syntax_score(test) == 26397
    print('Part 1: ' + str(syntax_score(data)))
    # Part 2
    assert auto_score(test) == 288957
    print('Part 2: ' + str(auto_score(data)))

if __name__ == "__main__":
    main()
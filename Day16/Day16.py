def load_data(path: str) -> str:
    return open(path).read().strip()

def hex_to_bin(h: str) -> str:
    bin_data = bin(int(h, 16))
    bin_data = bin_data[2:]
    while len(bin_data) < len(h)*4:
        bin_data = '0' + bin_data
    return bin_data

def do_calc(p: dict) -> int:
    val = []
    i = 0
    while p.get(i):
        val.append(p[i]['val'])
        i += 1

    if p['ID'] == 0: # Sum
        return sum(val)
    elif p['ID'] == 1: # Product
        c = 1
        for v in val:
            c *= v
        return c
    elif p['ID'] == 2: # Min
        return min(val)
    elif p['ID'] == 3: # Max
        return max(val)
    elif p['ID'] == 5: # Greater than
        return int(val[0]>val[1])
    elif p['ID'] == 6: # Less than
        return int(val[0] < val[1])
    elif p['ID'] == 7: # Equal to
        return int(val[0] == val[1])

def peek(data: list, n: int) -> str:
    ret = data[0][:n]
    data[0] = data[0][n:]
    return ret

def decode_packet(d) -> dict:
    if isinstance(d, str):
        d = [hex_to_bin(d)]
    p = {'V': int(peek(d, 3), 2), 'ID': int(peek(d, 3), 2)}
    if p['ID'] == 4: # Literal value
        i = 0
        val = ''
        while True:
            i += 1
            n = peek(d, 5)
            val += n[1:]
            if n[0] == '0': break
        p['val'] = int(val, 2)
        p['len'] = 3 + 3 + i*5
    else:
        l = {'0': 15, '1': 11}
        p['I'] = peek(d, 1)
        p['L'] = int(peek(d, l[p['I']]), 2)
        num = 0
        c_len = 0
        while True:
            p[num] = decode_packet(d)
            c_len += p[num]['len']
            num+=1
            if (p['I'] == '0' and c_len == p['L']) or (p['I'] == '1' and num == p['L']): break
        p['len'] = 7 + l[p['I']] + c_len
        p['val'] = do_calc(p)
    return p

def version_sum(p: dict) -> int:
    count = p['V']
    i = 0
    while p.get(i):
        count += version_sum(p[i])
        i += 1
    return count

def do_tests() -> None:
    # Check loading
    test = load_data('test.txt')
    assert test == '38006F45291200'
    # Check conversion
    assert hex_to_bin(test) == '00111000000000000110111101000101001010010001001000000000'
    # Verify literal value; # V: 6, ID: 4; 0: 2021; len: 21
    assert decode_packet('d2fe28')['val'] == 2021 # == 110100101111111000101000
    # Verify version sum
    assert version_sum(decode_packet('8A004A801A8002F478')) == 16
    assert version_sum(decode_packet('A0016C880162017C3686B18A3D4780')) == 31
    # Verify calculations
    assert decode_packet('C200B40A82')['val'] == 3
    assert decode_packet('C200B40A82')['val'] == 3
    assert decode_packet('04005AC33890')['val'] == 54
    assert decode_packet('880086C3E88112')['val'] == 7
    assert decode_packet('CE00C43D881120')['val'] == 9
    assert decode_packet('D8005AC2A8F0')['val'] == 1
    assert decode_packet('F600BC2D8F')['val'] == 0
    assert decode_packet('9C005AC2F8F0')['val'] == 0
    assert decode_packet('9C0141080250320F1802104A08')['val'] == 1

def main() -> None:
    do_tests()

    data = load_data('data.txt')
    p = decode_packet(data)
    print('Part 1: ' + str(version_sum(p)))
    print('Part 2: ' + str(p['val']))

if __name__ == "__main__":
    main()
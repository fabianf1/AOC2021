def load(path: str):
    data = open(path).read().strip().split('\n\n')

    output = []
    for scanner in data:
        lines = scanner.splitlines()
        result = [tuple([int(x) for x in line.split(',')]) for line in lines[1:]]
        output.append(result)

    return output

def relative_distance(d: list) -> list:
    r = []
    for i in range(len(d)):
        r.append([])
        for j in range(len(d)):
            if i != j:
                x = d[j][0] - d[i][0]
                y = d[j][1] - d[i][1]
                z = d[j][2] - d[i][2]
                r[i].append((x,y,z))
    return r

def do_rot(d: list, x_m, y_m, z_m, i) -> list:
    o = []
    for k in d:
        x = x_m[i][0] * k[0] + x_m[i][1] * k[1] + x_m[i][2] * k[2]
        y = y_m[i][0] * k[0] + y_m[i][1] * k[1] + y_m[i][2] * k[2]
        z = z_m[i][0] * k[0] + z_m[i][1] * k[1] + z_m[i][2] * k[2]
        o.append((x,y,z))
    return o

def rot_x(d, i):
    x_m = [[1, 0, 0], [1, 0,  0], [1, 0, 0], [1,0,  0]]
    y_m = [[0, 1, 0], [0, 0, 1], [0, -1, 0], [0, 0, -1]]
    z_m = [[0, 0, 1], [0, -1, 0], [0, 0, -1], [0, 1, 0]]
    return do_rot(d, x_m, y_m, z_m, i)

def rot_y(d, i):
    x_m = [[1, 0, 0], [0, 0, -1], [-1, 0, 0], [0, 0, 1]]
    y_m = [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]
    z_m = [[0, 0, 1], [1, 0, 0], [0, 0, -1], [-1, 0, 0]]
    return do_rot(d, x_m, y_m, z_m, i)

def rot_z(d, i):
    x_m = [[1, 0, 0], [0, 1, 0], [-1, 0, 0], [0, -1, 0]]
    y_m = [[0,1, 0], [-1, 0, 0], [0, -1, 0], [1, 0, 0]]
    z_m = [[0, 0, 1], [0, 0, 1], [0, 0,1], [0, 0, 1]]
    return do_rot(d, x_m, y_m, z_m, i)

def rotate(d, r: int):
    # There are 24 possible rotations
    # 6 sides of a cube * 4 2D-rotations
    if r == 0:
        return d
    elif r < 4: # Keep X-face the same
        return rot_x(d, r)
    elif r < 4*4: # Rotate X around the Z-Axis; then rotate around the others
        r1 = r // 4
        r2 = r % 4
        if r1 == 1 or r1 == 3:
            return rot_y(rot_z(d, r1), r2)
        else:
            return rot_x(rot_z(d, r1), r2)
    else: #16 - 24
        r1 = r // 4
        r2 = r % 4
        if r1 == 4:
            return rot_z(rot_y(d, 1), r2)
        else:
            return rot_z(rot_y(d, 3), r2)

def find_overlap(d1, d2):
    mapping = (0,0)
    for r in range(0, 24):
        for j in range(len(d2)):
            # Rotate
            d2j_rot = set(rotate(d2[j], r))
            # Check overlap
            for i in range(len(d1)):
                overlap = set(d1[i]) & d2j_rot
                if len(overlap) > 10:
                    mapping = (i,j) # Only need 1 pair to find the relative distance
        if mapping != (0,0):
            break
    return r, mapping

def untangle_scanner_data(d: list):
    # Create initial set
    un_b = set()
    for x,y,z in d[0]:
        un_b.add((x,y,z))
    # Build relative distance list
    rel = []
    for s in d:
        rel.append(relative_distance(s))
    # Find unique beacons
    done = []
    todo = [0]
    offset = {}
    while len(todo) > 0:
        n = todo.pop(0)
        done.append(n)
        for i in range(len(d)):
            if i == n or i in done:
                continue
            r, m = find_overlap(rel[n], rel[i])
            if m != (0,0):
                todo.append(i)
                # Get relative distance and rotation
                p1 = d[n][m[0]]
                p2 = rotate([d[i][m[1]]],r)[0]
                x = p1[0] - p2[0]
                y = p1[1] - p2[1]
                z = p1[2] - p2[2]
                offset[(n,i)] = ([r], (x,y,z))
                # Get rotation list from 0 to i
                if n != 0:
                    rL = offset[(0, n)][0].copy()
                    rL.append(r)

                    # Get Offset from 0 to i
                    off = [(x, y, z)]
                    for j in range(len(rL) - 2, -1, -1):
                        off = rotate(off, rL[j])
                    x = off[0][0] + offset[(0, n)][1][0]
                    y = off[0][1] + offset[(0, n)][1][1]
                    z = off[0][2] + offset[(0, n)][1][2]
                    # Save
                    offset[(0, i)] = (rL, (x, y, z))
                else:
                    rL = [r]
                # Move scanner-i beacons to scanner-0 frame of reference
                l = d[i].copy()
                for j in range(len(rL)-1, -1, -1):
                    l = rotate(l, rL[j])

                for j in range(len(l)):
                    xN = l[j][0] + x
                    yN = l[j][1] + y
                    zN = l[j][2] + z
                    l[j] = (xN, yN, zN)
                # Save
                un_b = un_b | set(l)
    # Retrieve wanted offsets
    scan_pos = [(0,0,0)]
    for i in range(1, len(d)):
        scan_pos.append(offset[(0, i)][1])

    return scan_pos, un_b

def largest_distance(d) -> int:
    res = 0
    for i in range(len(d)):
        for j in range(i+1, len(d)):
            x = abs(d[i][0] - d[j][0])
            y = abs(d[i][1] - d[j][1])
            z = abs(d[i][2] - d[j][2])
            res = max([res, x+y+z])
    return res

def do_tests() -> None:
    data = load('Test.txt')
    scanner, beacons = untangle_scanner_data(data)
    assert len(beacons) == 79
    assert largest_distance(scanner) == 3621

    print('Tests complete')

def main() -> None:
    do_tests()

    data = load('Data.txt')
    scanner, beacons = untangle_scanner_data(data)
    print('Part 1: ' + str(len(beacons)))
    print('Part 2: ' + str(largest_distance(scanner)))

if __name__ == "__main__":
    main()
edges = [line.strip().split("-") for line in open("input.txt")]


def solution_part_01():
    conns = {}

    for x, y in edges:
        if x not in conns:
            conns[x] = set()
        if y not in conns:
            conns[y] = set()
        conns[x].add(y)
        conns[y].add(x)

    sets = set()

    for x in conns:
        for y in conns[x]:
            for z in conns[y]:
                if x != z and x in conns[z]:
                    sets.add(tuple(sorted([x, y, z])))

    print("Anwser Part One", len([s for s in sets if any(cn.startswith("t") for cn in s)]))


def solution_part_02():
    conns = {}

    for x, y in edges:
        if x not in conns:
            conns[x] = set()
        if y not in conns:
            conns[y] = set()
        conns[x].add(y)
        conns[y].add(x)

    sets = set()
    
    def search(node, req):
        key = tuple(sorted(req))
        if key in sets: return
        sets.add(key)
        for neighbor in conns[node]:
            if neighbor in req: continue
            # Same thing but using set operator instead of checking each one
            # if not all(neighbor in conns[query] for query in req): continue
            if not (req <= conns[neighbor]): continue
            search(neighbor, req | {neighbor})
    
    for x in conns:
        search(x, {x})

    print("Anwser Part Two", ",".join(sorted(max(sets, key=len))))


solution_part_01()
solution_part_02()

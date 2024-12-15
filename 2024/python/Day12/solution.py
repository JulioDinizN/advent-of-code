from collections import deque

grid = [list(line.strip()) for line in open("input.txt")]

rows = len(grid)
cols = len(grid[0])

# regions = {}
#     for r in range(len(grid)):
#         for c in range(len(grid[0])):
#             value = grid[r][c]
#             regions.setdefault(value, []).append((r, c))


def get_regions():
    regions = []
    seen = set()

    for r in range(rows):
        for c in range(cols):
            if (r, c) in seen:
                continue
            seen.add((r, c))
            region = {(r, c)}
            q = deque([(r, c)])
            crop = grid[r][c]

            while q:
                cr, cc = q.popleft()
                for dr, dc in [(cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)]:
                    if dr < 0 or dc < 0 or dr >= rows or dc >= cols:
                        continue
                    if grid[dr][dc] != crop:
                        continue
                    if (dr, dc) in region:
                        continue
                    region.add((dr, dc))
                    q.append((dr, dc))
            seen |= region
            regions.append(region)
    return regions


def solution_part_01():
    regions = get_regions()

    def perimeter(region):
        output = 0
        for r, c in region:
            output += 4
            for dr, dc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if (dr, dc) in region:
                    output -= 1
        return output

    answserSum = sum(len(region) * perimeter(region) for region in regions)

    print("Anwser Part One", answserSum)


def solution_part_02():
    regions = get_regions()

    def sides(region):
        edges = {}

        for r, c in region:
            for dr, dc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if (dr, dc) in region:
                    continue
                er = (r + dr) / 2
                ec = (c + dc) / 2
                edges[(er, ec)] = (er - r, ec - c)

        seen = set()
        side_count = 0

        for edge, direction in edges.items():
            if edge in seen:
                continue
            seen.add(edge)
            side_count += 1
            er, ec = edge
            if er % 1 == 0:
                for dr in [-1, 1]:
                    cr = er + dr
                    while edges.get((cr, ec)) == direction:
                        seen.add((cr, ec))
                        cr += dr
            else:
                for dc in [-1, 1]:
                    cc = ec + dc
                    while edges.get((er, cc)) == direction:
                        seen.add((er, cc))
                        cc += dc
        return side_count           

    answserSum = sum(len(region) * sides(region) for region in regions)

    print("Anwser Part Two", answserSum)


solution_part_01()
solution_part_02()

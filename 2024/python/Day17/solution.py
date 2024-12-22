import re

def solution_part_01():
    a, b, c, *program = map(int, re.findall(r"\d+", open("input.txt").read()))

    pointer = 0
    output = []

    def combo(operand):
        if 0 <= operand <= 3:
            return operand
        if operand == 4:
            return a
        if operand == 5:
            return b
        if operand == 6:
            return c
        else:
            raise RuntimeError("nrecognized combo operand", operand)

    while pointer < len(program):
        ins = program[pointer]
        operand = program[pointer + 1]

        if ins == 0:  # adv
            a = a >> combo(operand)
        elif ins == 1:  # bxl
            b = b ^ operand
        elif ins == 2:  # bst
            b = combo(operand) % 8
        elif ins == 3:  # jnz
            if a != 0:
                pointer = operand
                continue
        elif ins == 4:  # bxc
            b = b ^ c
        elif ins == 5:  # out
            output.append(combo(operand) % 8)
        elif ins == 6:  # bdv
            b = a >> combo(operand)
        elif ins == 7:  # cdv
            c = a >> combo(operand)
        pointer += 2

    print("Anwser Part One")
    print(*output, sep=",")


def solution_part_02():
    a, b, c, *program = list(map(int, re.findall(r"\d+", open("input.txt").read())))

    def computer(a: int, b: int = 0, c: int = 0) -> list[int]:

        def combo(val: int) -> int:
            assert val != 7, "Invalid combo value"
            if val <= 3:
                return val
            reg_map = {4: a, 5: b, 6: c}
            return reg_map[val]

        output = []
        ip = 0
        while ip < len(program):
            opcode = program[ip]
            operand = program[ip + 1]
            match opcode:
                case 0:  # adv
                    a = a >> combo(operand)
                case 1:  # bxl
                    b = b ^ operand
                case 2:  # bst
                    b = combo(operand) % 8
                case 3:  # jnz
                    if a != 0:
                        ip = operand
                        continue
                case 4:  # bxc
                    b = b ^ c
                case 5:  # out
                    output.append(combo(operand) % 8)
                case 6:  # bdv
                    b = a >> combo(operand)
                case 7:  # cdv
                    c = a >> combo(operand)
            ip += 2
        return output

    candidates = [0]
    for l in range(len(program)):
        next_candidates = []
        for val in candidates:
            for i in range(8):
                target = (val << 3) + i
                if computer(target) == program[-l - 1 :]:
                    next_candidates.append(target)
        candidates = next_candidates

    part2 = min(candidates)
    print(f"Anwser Part Two {part2}")


solution_part_01()
solution_part_02()

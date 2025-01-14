small_test_input = """\
x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02"""

test_input = """\
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""


def calc_answer(wires, gates):
    while gates:
        input1, input2, gate_type, output = gates.popleft()
        if input1 in wires and input2 in wires:
            # print(f"{input1} and {input2} values known! can calculate {output}")
            wires[output] = functions[gate_type](wires[input1], wires[input2])

        else:
            # print(f"{input1} or {input2} values not yet known, so cannot calculate {output}")
            gates.append((input1, input2, gate_type, output))
    wire_values = tuple((wire, value) for wire, value in wires.items() if wire.startswith('z'))
    wire_values = sorted(wire_values, reverse=True)
    binary_value = ''.join([str(v) for w, v in wire_values if w.startswith('z')])
    print(int(binary_value, base=2))


functions = {
    'AND': lambda x, y: x & y,
    'OR': lambda x, y: x | y,
    'XOR': lambda x, y: x ^ y,
}

if __name__ == '__main__':
    # input_str = test_input
    input_str = open('input24.txt').read()

    wires, gates = input_str.split('\n\n')
    wires = {
        name: int(value)
        for wire in wires.splitlines()
        for name, value in [wire.split(': ')]  # this is magical - list of length 1 :)
    }
    gates = {
        z: (op, x, y)
        for gate in gates.splitlines()
        for x, op, y, z in [gate.replace(' -> ', ' ').split()]
    }


    def verify_z(wire, num):
        # print(f"vz {wire} {num}")
        if wire not in gates: return False
        op, x, y = gates[wire]
        if op != 'XOR': return False
        if num == 0: return sorted([x, y]) == ['x00', 'y00']
        return verify_intermediate_xor(x, num) and verify_carry_bit(y, num) or verify_intermediate_xor(y,
                                                                                                       num) and verify_carry_bit(
            x, num)


    def verify_intermediate_xor(wire, num):
        # print(f"vx {wire} {num}")
        if wire not in gates: return False
        op, x, y = gates[wire]
        if op != 'XOR': return False
        return sorted([x, y]) == [f"x{num:0>2}", f"y{num:0>2}"]


    def verify_carry_bit(wire, num):
        # print(f"vc {wire} {num}")
        if wire not in gates: return False
        op, x, y = gates[wire]
        if num == 1:
            if op != 'AND': return False
            return sorted([x, y]) == ["x00", "y00"]
        if op != 'OR': return False
        return verify_direct_carry(x, num - 1) and verify_recarry(y, num - 1) or verify_direct_carry(y,
                                                                                                     num - 1) and verify_recarry(
            x, num - 1)


    def verify_direct_carry(wire, num):
        # print(f"vd {wire} {num}")
        if wire not in gates: return False
        op, x, y = gates[wire]
        if op != 'AND': return False
        return sorted([x, y]) == [f"x{num:0>2}", f"y{num:0>2}"]


    def verify_recarry(wire, num):
        # print(f"vr {wire} {num}")
        if wire not in gates: return False
        op, x, y = gates[wire]
        if op != 'AND': return False
        return verify_intermediate_xor(x, num) and verify_carry_bit(y, num) or verify_intermediate_xor(y,
                                                                                                       num) and verify_carry_bit(
            x, num)


    def verify(num):
        return verify_z(f"z{num:0>2}", num)

    def progress():
        i = 0
        while True:
            if not verify(i): break
            i += 1
        return i

    result = []
    for _ in range(4):
        baseline = progress()
        for x in gates:
            for y in gates:
                if x == y: continue
                gates[x], gates[y] = gates[y], gates[x]
                if progress() > baseline:
                    break
                gates[x], gates[y] = gates[y], gates[x]
            else:
                continue
            break
        result.extend([x, y])
    print(','.join(sorted(result)))
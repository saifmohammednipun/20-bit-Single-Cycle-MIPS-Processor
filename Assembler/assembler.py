def convertBinToHex(bin):
    hex_map = {
        "0000": "0", "0001": "1", "0010": "2", "0011": "3",
        "0100": "4", "0101": "5", "0110": "6", "0111": "7",
        "1000": "8", "1001": "9", "1010": "A", "1011": "B",
        "1100": "C", "1101": "D", "1110": "E", "1111": "F"
    }
    return hex_map.get(bin, "Invalid")

def checkInstruction(inst):
    instruction_map = {
        "add": "000", "sub": "000", "and": "000", "or": "000",
        "nor": "000", "sll": "000", "srl": "000",
        "lw": "110", "sw": "001", "beq": "011", "bne": "010",
        "addi": "101", "jmp": "111",
        "nop": "000"
    }
    return instruction_map.get(inst, "Invalid")

def checkRegister(reg):
    register_map = {
        "$r0": "0000", "$r1": "0001", "$r2": "0010", "$r3": "0011",
        "$r4": "0100", "$r5": "0101", "$r6": "0110", "$r7": "0111",
        "$r8": "1000", "$r9": "1001", "$r10": "1010", "$r11": "1011",
        "$r12": "1100", "$r13": "1101", "$r14": "1110", "$r15": "1111"
    }
    return register_map.get(reg, "Invalid")

def decimalToBinary(num, bits):
    if num < 0:
        num = (1 << bits) + num
    return f"{num:0{bits}b}"

readf = open("inputs", "r")
writef = open("outputs", "w")
writef.write("v2.0 raw\n")

for line in readf:
    splitted = line.split()

    # Skip empty lines or lines with insufficient tokens
    if len(splitted) == 0:
        continue

    inst = splitted[0]
    op = checkInstruction(inst)

    if inst in ["add", "sub", "and", "or", "nor", "sll", "srl"]:
        if len(splitted) < 4:
            binary = "Invalid Instruction"
        else:
            rs = checkRegister(splitted[2])
            rt = checkRegister(splitted[3])
            rd = checkRegister(splitted[1])
            shamt = decimalToBinary(int(splitted[4]), 2) if len(splitted) > 4 else "00"
            funct = {
                "add": "011", "sub": "111", "and": "110", "or": "100",
                "nor": "101", "sll": "000", "srl": "010"
            }.get(inst, "Invalid")
            binary = op + rs + rt + rd + shamt + funct

    elif inst in ["lw", "sw", "addi", "beq", "bne"]:
        if len(splitted) < 4:
            binary = "Invalid Instruction"
        else:
            rs = checkRegister(splitted[2])
            rd = checkRegister(splitted[1])
            immediate = decimalToBinary(int(splitted[3]), 9)
            binary = op + rs + rd + immediate

    elif inst == "jmp":
        if len(splitted) < 2:
            binary = "Invalid Instruction"
        else:
            target = decimalToBinary(int(splitted[1]), 17)
            binary = op + target

    elif inst == "nop":
        binary = op + "0" * 17

    else:
        binary = "Invalid Instruction"

    # Ensure binary has valid length before conversion
    if len(binary) % 4 == 0:
        hex_output = "".join(convertBinToHex(binary[i:i+4]) for i in range(0, len(binary), 4))
    else:
        hex_output = "Invalid Binary Length"

    writef.write(hex_output + "\n")
    print(hex_output)

readf.close()
writef.close()
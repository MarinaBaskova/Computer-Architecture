import sys
​
PRINT_BEEJ = 1
HALT = 2
PRINT_NUM = 3
SAVE = 4
PRINT_REGISTER = 5
ADD = 6
PUSH = 7
POP = 8
CALL = 9
RET = 10
​
'''
SAVE takes 2 arguments
saves value in [ARG1] to register [ARG2]
'''
​
​
register = [0] * 8
​
memory = [0] * 32  # 32 bytes of RAM
​
SP = 7
​
​
​


def load_memory(filename):
    try:
        address = 0


​
with open(filename) as f:
    for line in f:
        # Split before and after any comment symbols
        comment_split = line.split("#")
​
num = comment_split[0].strip()
​
# Ignore blanks
if num == "":
    continue
​
value = int(num)
​
memory[address] = value
​
address += 1
​
except FileNotFoundError:
    print(f"{sys.argv[0]}: {sys.argv[1]} not found")
    sys.exit(2)
​
​
​
​
if len(sys.argv) != 2:
    print("usage: simple.py <filename>", file=sys.stderr)
    sys.exit(1)
​
​
filepath = sys.argv[1]
load_memory(filepath)
​
​
pc = 0
running = True
​
while running:
    ir = memory[pc]
​
print(f"{ir} - {memory}")
​
if ir == PRINT_BEEJ:
    print("Beej!")
    pc += 1
​
elif ir == PRINT_NUM:
    num = memory[pc + 1]
    print(num)
    pc += 2
​
elif ir == SAVE:
    num = memory[pc + 1]
    reg = memory[pc + 2]
    register[reg] = num
    pc += 3
​
elif ir == PRINT_REGISTER:
    reg = memory[pc + 1]
    print(register[reg])
    pc += 2
​
elif ir == ADD:
    reg_a = memory[pc + 1]
    reg_b = memory[pc + 2]
    register[reg_a] += register[reg_b]
    pc += 3
​
elif ir == PUSH:
    reg = memory[pc + 1]
    val = register[reg]
    register[SP] -= 1  # Decrement SP
    memory[register[SP]] = val
    pc += 2
​
elif ir == POP:
    reg = memory[pc + 1]
    val = memory[register[SP]]
    register[reg] = val
    register[SP] += 1
    pc += 2
​
elif ir == CALL:
    register[SP] -= 1
    memory[register[SP]] = pc + 2
    reg = memory[pc + 1]
    pc = register[reg]
​
elif ir == RET:
    pc = memory[register[SP]]
    register[SP] += 1
​
elif ir == HALT:
    running = False
    pc += 1
​
else:
    print(f"Unknown instruction: {ir}")
    sys.exit(1)


#
4   # SAVE [subroutine1 address] in reg 0
6   # subroutine1 at address 6
0
9   # CALL reg 0 (subroutine1)
0
2   # HALT
# -------------------------------
# subroutine1 (address 6)
4   # SAVE [subroutine2 address] in reg 0
14  # subroutine2 at address 14
0
9   # CALL reg 0 (subroutine2)
0
1   # PRINT_BEEJ
1   # PRINT_BEEJ
10  # RET
# -------------------------------
# subroutine2 (address 14)
1   # PRINT_BEEJ
1   # PRINT_BEEJ
1   # PRINT_BEEJ
10  # RET

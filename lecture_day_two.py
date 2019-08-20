# str = "101110"
import sys
​
'''

def to_decimal(num_string, base):
    digit_list = list(num_string)
    digit_list.reverse()
    value = 0
    for i in range(len(digit_list)):
        print(f"+({int(digit_list[i])} * {base ** i})")
        value += int(digit_list[i]) * (base ** i)
    return value


​
to_decimal(str, 10)
'''

# simple.py
​
PRINT_BEEJ = 1
HALT = 2
PRINT_NUM = 3
SAVE = 4
PRINT_REGISTER = 5
ADD = 6
​
'''
SAVE takes 2 arguments
saves value in [ARG1] to register [ARG2]
'''
​
register = [0] * 8
​
memory = [0] * 128  # 128 bytes of RAM
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
    command = memory[pc]
​
if command == PRINT_BEEJ:
        print("Beej!")
        pc += 1
​
elif command == PRINT_NUM:
        num = memory[pc + 1]
        print(num)
        pc += 2
​
elif command == SAVE:
        num = memory[pc + 1]
        reg = memory[pc + 2]
        register[reg] = num
        pc += 3
​
elif command == PRINT_REGISTER:
        reg = memory[pc + 1]
        print(register[reg])
        pc += 2
​
elif command == ADD:
        reg_a = memory[pc + 1]
        reg_b = memory[pc + 2]
        register[reg_a] += register[reg_b]
        pc += 3
​
elif command == HALT:
        running = False
        pc += 1
​
else:
        print(f"Unknown instruction: {command}")
        sys.exit(1)

# beej simple

1    # PRINT_BEEJ
1    # PRINT_BEEJ
1    # PRINT_BEEJ
4    # SAVE 65 in register 2
12
2
4    # SAVE 20 in register 3
36
3
6    # ADD register 3 onto register 2
2
3
5    # PRINT_REGISTER register 2
2
1    # PRINT_BEEJ
2    # HALT

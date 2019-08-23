import sys
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
memory = [
    PRINT_BEEJ,
    SAVE,   # SAVE 65 to register 2
    65,
    2,
    SAVE,   # SAVE 20 to register 3
    20,
    3,
    ADD,    # R2 += R3
    2,
    3,
    PRINT_REGISTER,  # Print the value in register 2
    2,
    HALT
]
​
register = [0] * 8
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

'''
base 10 (decimal)

+-----1000's place
|+----100's place
||+---10's place
|||+--1's place
||||
abcd

1234

1 * 1000 + 2 * 100 + 3 * 10 + 4 * 1 == 1234

base 2 (binary)

+-----8's place (0b1000's place)
|+----4's place (0b100's place)
||+---2's place (0b10's place)
|||+--1's place (0b1's place)
||||
abcd

1110 (binary)

1 * 8 + 1 * 4 + 1 * 2 + 0 * 1 = 14

128 64 32 16 8 4 2 1

Hexadecimal is a base-16 number system. That means there are 16 possible digits used to represent numbers. 10 of the numerical values you're probably used to seeing in decimal numbers: 

0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F,

Those values still represent the same value you're used to. The remaining six digits are represented by A, B, C, D, E, and F, which map out to values of 10, 11, 12, 13, 14, and 15.
Binary to hex - > 10100011 _ > 

Split in 2 

    1010 0011
    10     3
    A3

1010 bunary - A in hex


c7 -> to binary

c    7

12  decimal    7 
1100           0111


C7 -> 11000111
'''

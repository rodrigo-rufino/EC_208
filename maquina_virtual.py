#coding: utf-8
"""
Maquina virtual
EC 208
"""
PC = 0
AC = 0
instr = 0
intr_type = 0
data_loc = [0, 0, 0]
data = [0, 0, 0]
run_bit = True
starting_adress = 0

#vetores utilizados como exemplo
program_file = open('program.txt', 'r')
memory = program_file.read().splitlines()
values = [0, 1, 2, 3, 7, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# 000 adicao, 001 multiplicacao, 010 mod, 011 pow, 100 store
#4 bits dado A, 4 bits dado B, 4 bits local onde resultado e armazenado, 2 bits instrucao

def get_instr_type(addr):
    if addr[12:] == "000":
        return "ADD"
    elif addr[12:] == "001":
        return "MUL"
    elif addr[12:] == "010":
        return "MOD"
    elif addr[12:] == "011":
        return "POW"
    elif addr[12:] == "100":
        return "STORE"
    else:
        return "Instrucao nao encontrada"

def find_data(instr, type):
    A = instr[0:4]
    B = instr[4:8]
    C = instr[8:11]
    
    return [A, B, C]

def execute(type, data):
    if type == "ADD":
        A = values[int(data[0], 2)]
        B = values[int(data[1], 2)]
        C = values[int(data[2], 2)]
        C = A + B
        values[int(data[2], 2)] = C
        print("ADD: %d = %d + % d" % (C,A,B))
    elif type == "MUL":
        A = values[int(data[0], 2)]
        B = values[int(data[1], 2)]
        C = values[int(data[2], 2)]
        C = A * B
        values[int(data[2], 2)] = C
        print("MUL: %d = %d + % d" % (C,A,B))
    elif type == "MOD":
        A = values[int(data[0], 2)]
        B = values[int(data[1], 2)]
        C = values[int(data[2], 2)]        
        C = A % B
        values[int(data[2], 2)] = C
        print("MOD: %d = %d mod %d" % (C,A,B))
    elif type == "POW":
        A = values[int(data[0], 2)]
        B = values[int(data[1], 2)]
        C = values[int(data[2], 2)]
        C = A ** B
        values[int(data[2], 2)] = C        
        print("POW: %d = %d ^ % d" % (C,A,B))
    elif type == "STORE":
        A = int(raw_input("Store data: "))
        values[int(data[0], 2)] = A
    else:
        print "Instrucao nao encontrada"
        
#Interpreter
PC = starting_adress
while run_bit:
    print values
    instr = memory[PC]
    PC = PC + 1
    instr_type = get_instr_type(instr)
    data_loc = find_data(instr, instr_type)
    execute (instr_type, data_loc)
    print values
    if PC>=len(memory):
        run_bit = False
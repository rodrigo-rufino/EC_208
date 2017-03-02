# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
PC = 0
AC = 0
instr = 0
intr_type = 0
data_loc = 0
data = 0
run_bit = True

memory = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
instruc = ["0000000000", "0000000001", "0000000010", "0000000011"]
# 00 adicao, 01 multiplicacao, 10 mod, 11 potencia

# Function definition is here
def get_instr_type(addr):
    if addr[8:9] == "00":
        return "ADD"
    elif addr[8:9] == "01":
        return "MUL"
    elif addr[8:9] == "10":
        return "MOD"
    elif addr[8:9] == "11":
        return "POT"
    else:
        return "Instrucao nao encontrada";

def find_data(instr, type):
    return;

def execute(type, data):
    return;

def interpret(memory, starting_adress):
    PC = starting_adress
    while run_bit:
        instr = memory[PC]
        PC = PC + 1
        instr_type = get_instr_type(instr)
        data_loc = find_data(instr, instr_type)
        if data_loc >= 0:
            data = memory[data_loc]
        execute (instr_type, data)
    return;


# Now you can call printinfo function


#coding: utf-8
"""
Maquina virtual
EC 208
Alunos: Rodrigo Rufino e Márcio Rotella
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
memory = ["11110100001000"]
values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
instr = ["00000000000000", "00000000000001", "00000000000010", "00000000000011"]
# 00 adicao, 01 multiplicacao, 10 store, 11 load
#4 bits dado A, 4 bits dado B, 4 bits local onde resultado e armazenado, 2 bits instrucao

def get_instr_type(addr):
    print(addr[12:] + " 24")
    if addr[12:] == "00":
        print("ADD")
        return "ADD"
    elif addr[12:] == "01":
        return "MUL"
    elif addr[12:] == "10":
        return "LOAD"
    elif addr[12:] == "11":
        return "STORE"
    else:
        return "Instrucao nao encontrada"

def find_data(instr, type):
    A = int(instr[0:4], 2)
    print(A)
    B = int(instr[4:8], 2)
    print(B)
    C = int(instr[8:11], 2)
    return [A, B, C]

def execute(type, data):
    if type == "ADD":
        print("43")
        data[2] = data[0] + data[1]
        print("ADD: %d = %d + % d" % (data[2],data[1],data[0]))
        return data
    elif type == "MUL":
        data[2] = data[0] * data[1]
        return data
    elif type == "LOAD":
        data[2] = data[0] % data[1]
        return data
    elif type == "STORE":
        data[2] = data[0] ** data[1]
        return data
    else:
        return "Instrucao nao encontrada"

#def interpret(memory, starting_adress):
PC = starting_adress
while run_bit:
    instr = memory[0]
    PC = PC + 1
    print("63")
    instr_type = get_instr_type(instr)
    data_loc = find_data(instr, instr_type)
    execute (instr_type, data_loc)
    print(values)
    if PC>=len(memory):
        run_bit = False
            
#    return

#salvar C no vetor values
#implementar outras instruções
#testar mais de uma instrução
#arquivo

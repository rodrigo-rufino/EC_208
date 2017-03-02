"""
Maquina virtual
EC 208
Alunos: Rodrigo Rufino e Márcio Rotella
"""
PC = 0
AC = 0
instr = 0
intr_type = 0
data_loc = 0
data = 0
run_bit = True

#vetores utilizados como exemplo
memory = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
instr = ["00000000000000", "00000000000001", "00000000000010", "00000000000011"]
# 00 adicao, 01 multiplicacao, 10 mod, 11 potencia
#4 bits dado A, 4 bits dado B, 4 bits local onde resultado e armazenado, 2 bits instrucao

# Function definition is here
def get_instr_type(addr):
    if addr[13:14] == "00":
        return "ADD"
    elif addr[13:14] == "01":
        return "MUL"
    elif addr[13:14] == "10":
        return "MOD"
    elif addr[13:14] == "11":
        return "POT"
    else:
        return "Instrucao nao encontrada"

def find_data(instr, type):
    A = instr[0:3]
    B = instr[5:8]
    result = instr[9:12]
    return [A, B, result]

def execute(type, data):
    if type == "ADD":
        data[2] = data[0] + data[1]
        return data
    elif type == "MUL":
        data[2] = data[0] * data[1]
        return data
    elif type == "MOD":
        data[2] = data[0] % data[1]
        return data
    elif type == "POT":
        data[2] = data[0] ** data[1]
        return data
    else:
        return "Instrucao nao encontrada"

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
    return



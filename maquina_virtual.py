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
variables = open('variables.txt', 'r+')
values = variables.read().splitlines()
variables.close()
variables = open('variables.txt', 'w+')
print values
print 'AA'
 
"""
últimos 3 bits definem o tipo da operação a ser executada
000 adicao, 001 multiplicacao, 010 mod, 011 pow, 100 store
4 bits dado A, 4 bits dado B, 4 bits local onde resultado e armazenado, 3 bits instrucao
"""

#função que decodifica os 3 últimos bits para identificar qual instrução eles correspondem
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
        return "Instrução não encontrada"
        
#função que pega o pacote de bits e tira os endereços dos dados a serem utilizados em uma operação
def find_data(instr, type):
    A = instr[0:4]
    B = instr[4:8]
    C = instr[8:11]
    return [A, B, C]

#função que, de acordo com a função selecionada, resolve uma operação diferente
def execute(type, data_loc):
    if type == "ADD":
        A = int(values[int(data_loc[0], 2)], 2)
        B = int(values[int(data_loc[1], 2)], 2)
        C = int(values[int(data_loc[2], 2)], 2)
        C = A + B
        values[int(data_loc[2], 2)] = bin(C)[2:] 
        print values[int(data_loc[2], 2)]
        print("ADD: %d = %d + % d" % (C,A,B))
    elif type == "MUL":
        A = int(values[int(data_loc[0], 2)], 2)
        B = int(values[int(data_loc[1], 2)], 2)
        C = int(values[int(data_loc[2], 2)], 2)
        C = A * B
        values[int(data_loc[2], 2)] = bin(C)[2:] 
        print("MUL: %d = %d * % d" % (C,A,B))
    elif type == "MOD":
        A = int(values[int(data_loc[0], 2)], 2)
        B = int(values[int(data_loc[1], 2)], 2)
        C = int(values[int(data_loc[2], 2)], 2)       
        C = A % B
        values[int(data_loc[2], 2)] = bin(C)[2:] 
        print("MOD: %d = %d mod %d" % (C,A,B))
    elif type == "POW":
        A = int(values[int(data_loc[0], 2)], 2)
        B = int(values[int(data_loc[1], 2)], 2)
        C = int(values[int(data_loc[2], 2)], 2)
        C = A ** B
        values[int(data_loc[2], 2)] = bin(C)[2:]      
        print("POW: %d = %d ^ % d" % (C,A,B))
    elif type == "STORE":
        A = int(raw_input("Store data: "))
        values[int(data_loc[0], 2)] = bin(A)[2:]
    else:
        print "Instrucao nao encontrada"
        
#Interpreter
PC = starting_adress
while run_bit:
    instr = memory[PC]
    PC = PC + 1
    instr_type = get_instr_type(instr)
    data_loc = find_data(instr, instr_type)
    execute (instr_type, data_loc)
    if PC>=len(memory):
        for i in values:
            i = i.zfill(32)
            print i
            variables.write(i)
            variables.write('\n')
        variables.close()
        program_file.close()
        run_bit = False        
#coding: utf-8
"""
Maquina virtual com Memória Cache
EC 208
Rodrigo Ribeiro, Márcio Rotella, Pedro Moreira, Luísa
"""
PC = 0
AC = 0
data = [0, 0, 0]
run_bit = True
starting_adress = 0

# vetores utilizados como exemplo
program_file = open('program.txt', 'r')
memory = program_file.read().splitlines()

variables = open('variables.txt', 'r+')
values = variables.read().splitlines()

variables.close()
variables = open('variables.txt', 'w+')

cache = {'tag': 0, 'cache_data': values[:8]}

cache_miss = 0
cache_hit = 0


 
"""
últimos 3 bits definem o tipo da operação a ser executada
000 adicao, 001 multiplicacao, 010 mod, 011 pow, 100 store
4 bits dado A, 4 bits dado B, 4 bits local onde resultado e armazenado, 3 bits instrucao

Dados do Sistema
    Memória Principal:
        - Tamanho da Memória Principal = 512 bits = 64 bytes
        - 16 bits para endereçamento
        - 32 bits de dados
        
    Memória Cache:
        - 1 Bloco de 4 palavras (metade da memória total)
        - TAG de 1 bit: 0 - primeiros 4 bits, 1 - últimos 4 bits
        - Dado: 16 bits
        - Tamanho da Cache = Blocos*(Dados + TAG) = 8*(32 + 1) = 264 bits
    
    Estrutura da Cache:
             ________________________________________
        000 |1 bit de TAG |    16 Bits de Dados      |
        001 .¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯.
        ... .                                        .
        110 .________________________________________.
        111 |1 bit de TAG |    16 Bits de Dados      |
             ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
"""


# função que decodifica os 3 últimos bits para identificar qual instrução eles correspondem
def get_instr_type(addr):
    if addr[12:] == "000":
        return "ADD"
    elif addr[12:] == "001":
        return "MUL"
    elif addr[12:] == "010":
        return "SUB"
    elif addr[12:] == "011":
        return "POW"
    elif addr[12:] == "100":
        return "STORE"
    else:
        return "Instrução não encontrada"


def search_cache(a):
    cont = 0
    # Ler bit mais significativo
    addr = int(a)
    msb = int(addr/1000)
    global cache
    # Comparar bit com tag atual
    while True:
        cache_data = cache['cache_data']
        # Caso o endereço esteja dentro da região que a cache possui, é um cache hit!
        if msb == cache['tag']:
            global cache_hit
            cache_hit = cache_hit + 1
            cache_address = addr - msb*1000
            # converte o valor binário para int e retorna
            value = cache_data[int(str(cache_address), 2)]
            return int(value, 2)
            break
        # Caso o endereço esteja fora da região, é um cache miss!
        else:
            global cache_miss
            cache_miss = cache_miss + 1
            # Se foi um cache miss, a cache descarta seus valores e pega outro bloco (outra metade da memória)
            if cache['tag'] == 0:
                cache = {'tag': 1, 'cache_data': values[8:]}
            else:
                cache = {'tag': 0, 'cache_data': values[:8]}


# função que pega o pacote de bits e tira os endereços dos dados a serem utilizados em uma operação
def find_data(instr):
    a = instr[0:4]
    b = instr[4:8]
    c = instr[8:12]
    return [search_cache(a), search_cache(b), c]


# função que, de acordo com a função selecionada, resolve uma operação diferente
def execute(type, data_loc):
    if type == "ADD":
        a = data_loc[0]
        b = data_loc[1]
        c = a + b
        if c >= 2**32:
            c = 2**32
        values[int(data_loc[2], 2)] = bin(c)[2:]
        print("ADD: %d = %d + %d" % (c, a, b))
    elif type == "MUL":
        a = data_loc[0]
        b = data_loc[1]
        c = a * b
        if c >= 2**32:
            c = 2**32
        values[int(data_loc[2], 2)] = bin(c)[2:]
        print("MUL: %d = %d * %d" % (c, a, b))
    elif type == "SUB":
        a = data_loc[0]
        b = data_loc[1]
        c = a - b
        if c <= 0:
            c = 0
        values[int(data_loc[2], 2)] = bin(c)[2:]
        print("SUB: %d = %d - %d" % (c, a, b))
    elif type == "POW":
        a = data_loc[0]
        b = data_loc[1]
        c = a ** b
        if c >= 2**32:
            c = 2**32
        values[int(data_loc[2], 2)] = bin(c)[2:]
        print("POW: %d = %d ^ %d" % (c, a, b))
    elif type == "STORE":
        a = int(raw_input("Store data: "))
        values[int(data_loc[2], 2)] = bin(a)[2:]
    else:
        print "Instrucao nao encontrada"


# Interpreter
if __name__ == "__main__":

    while run_bit:
        instr = memory[PC]
        PC = PC + 1
        instr_type = get_instr_type(instr)
        data_loc = find_data(instr)
        execute(instr_type, data_loc)
        if PC >= len(memory):
            for i in values:
                i = i.zfill(32)
                variables.write(i)
                variables.write('\n')
            variables.close()
            program_file.close()
            run_bit = False
    print "\nCache Info:"
    print " - Cache miss: ", cache_miss
    print " - Cache hit: ", cache_hit

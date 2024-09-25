a = 5

def muda_e_imprime():
    global a
    a = 7
    print('A dentro da função: %d' % a)

print('a antes de mudar: %d' %a)
muda_e_imprime()

print(f'a depois de mudar: {a}')

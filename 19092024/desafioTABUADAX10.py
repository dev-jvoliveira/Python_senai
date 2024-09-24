def exibir_tabuadas():
       
    for j in range(1, 6):
        for i in range(1, 11):
            print(f"{i:2} x {j:2} = {i * j:2}", end='  ')
        print()
    for j in range(6, 11):
        for i in range(1, 11):
            print(f"{i:2} x {j:2} = {i * j:2}", end='  ')
        print()

exibir_tabuadas()

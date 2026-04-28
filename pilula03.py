def atender(fila):
    if len(fila) == 0:
        print('fila vazia')
    else:
        pacientes = fila.pop(0)
        print(f'atendendo {pacientes}')
    return fila

def main():
    fila = ['ana', 'carlos', 'beatriz', 'joão']
    print(f'fila inicial {fila}')
    fila = atender(fila)
    print(f'fila alterada: {fila}')

main()
def atualizar_hist(hist,paciente):
    if paciente in hist:
        hist.remove(paciente)
    hist.append(paciente)
    return hist

def main():
    hist = ['ana', 'carlos', 'beatriz']
    novo = 'carlos'
    print(f'hist atual {hist}')
    hist = atualizar_hist(hist, novo)
    print(f'hist atualizado: {hist}')

main()
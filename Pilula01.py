def ranking(pacientes):
    ranking_pacientes = []
    for paciente in pacientes:
        ponto = 0
        if paciente ['gravidade'] >= 4:
            pontos += 3
        elif paciente ['gravidade'] >= 2:
            pontos += 2

        if paciente['idade'] >= 60:
            pontos += 2
        ranking_pacientes.append({'nome': paciente['nome'],
                                  'pontos' : pontos})
        
    for i in range(len(ranking_pacientes)):
        for j in range(i+1, len(ranking_pacientes)):
            if ranking_pacientes[i]['pontos'] < ranking_pacientes[j]['pontos']:
                ranking_pacientes[i], ranking_pacientes[j] = ranking_pacientes[j],ranking_pacientes
    
    for item in range(len(ranking_pacientes)):
        print(f'{ranking_pacientes[item]['nome']}, {ranking_pacientes[item]['pontos']}')
        


def main():
    paciente = [
        {'nome' : 'Ana', 'idade' : 70, 'gravidade':3},
        {'nome' : 'Carlos', 'idade' : 40, 'gravidade':5},
        {'nome' : 'Beatriz', 'idade' : 65, 'gravidade':2},
        {'nome' : 'João', 'idade' : 30, 'gravidade':1},
    ]
    #(print(paciente[1]['nome']),paciente[1]['idade'])

main()

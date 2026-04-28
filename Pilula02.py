from collections import Counter

def especialidadeTop(consultas):
    if not consultas:
        return None
    
    especialidades = [c['especialidade'] for c in consultas]
    return Counter(especialidades).most_common(1)[0][0]

def main():
    consultar = [
        {'paciente': 'Ana', 'especialidade': 'cardiologia'},
        {'paciente': 'Carlos', 'especialidade': 'ortopedista'},
        {'paciente': 'Beatriz', 'especialidade': 'cardiologia'},
        {'paciente': 'João', 'especialidade': 'cardiologia'},
    ]
    print(especialidadeTop(consultar))

main()
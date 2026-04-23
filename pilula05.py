def processar_consultas(registro):
    tempos = {}
    cont = {}
    status = {}
    
    for reg in registro:
        p = reg ['paciente']
        if p not in tempos:
             tempos[p] = 0
             cont[p] += reg ['tempos']
             cont[p] += 1
    
    for paciente in tempos:            
        t = tempos [paciente]
        if t < 2:
             status[paciente] = 'leve'
        elif t < 5:
            status[paciente] = 'moderado'
        else:
            statu[paciente] = 'critico'    
            
def main():
    registros = [
        {'paciente':'ana', 'tempo': 1},
        {'paciente':'ana', 'tempo': 2},
        {'paciente':'carlos', 'tempo': 4},
        
    ]
    processar_consultas(registros)
    
main()
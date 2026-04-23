def atualizar_historico(historico, paciente):
    if paciente in historico:
        historico.remove(paciente)
    historico.append(paciente)    
    return historico    

def main():
    historico = ['Ana', ' Guilherme', 'Denilson']
    novo = 'Guilherme'
    print(historico)
    historico = atualizar_historico(historico, novo)
    print(f'paciente aguardando: {novo}')
    print(f'historico atualizado: {historico}' )
    
main()
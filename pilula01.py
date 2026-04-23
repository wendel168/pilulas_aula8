def ranking_prioridade(pacientes):
    ranking = []    
    for paciente in pacientes:
        pontos = 0
        if paciente['gravidade']>= 4:
            pontos +=3
        elif paciente['gravidade']>= 2:
            pontos += 2
        if paciente['idade'] >= 60:
            pontos += 2    
        ranking.append( {'nome': paciente ['nome'],'pontos':pontos})
        
    for i in range(len(ranking)):
        for J in range(i+1,len (ranking)):
            if ranking[i]['pontos'] < ranking [J]['pontos']:
                ranking[i],ranking [J] = ranking[J], ranking[i]
    for i in range (len(ranking)):
        print (f'{i+1} - {ranking[i]['nome']}, {ranking[i]['pontos']}')            
    
                      
def main():
    pacientes = [
        {'nome':'Ana','idade':70, 'gravidade': 3},
        {'nome':'Carlos','idade':40, 'gravidade': 5},
        {'nome':'Beatriz','idade':65, 'gravidade': 2},
        {'nome':'Joao','idade':30, 'gravidade': 1},
    ]
    print(pacientes[0]['nome'])
    ranking_prioridade(pacientes)
main()    
    
    
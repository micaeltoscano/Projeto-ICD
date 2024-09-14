import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Como as colunas eram Object, não iriam aparecer quando fóssemos usar o describe(), por exemplo, então essa função "alterar_type" muda o tipo da coluna além de converter os valores para 0,1,2,3. O único parâmetro dela é o dataset.

def alterar_type(ds):

    #Criando as listas que armazenam o nome das colunas com o tipo Object
    colunas_yes_no = []
    colunas_frequencia = []
    
    for coluna in ds.columns:
        # Verificando se todos os valores da coluna são Yes ou No.
        if ds[coluna].dropna().isin(['Yes', 'No']).all():  #Obs: Usando dropna para tirar valores NaN que interferem no resultado.
            if coluna not in colunas_yes_no: #Adicionando apenas nomes únicos nas listas.
                colunas_yes_no.append(coluna)
                
        # Verificando se todos os valores da coluna são 'Never', 'Rarely', 'Sometimes', 'Very frequently'
        if ds[coluna].dropna().isin(['Never', 'Rarely', 'Sometimes', 'Very frequently']).all():
            if coluna not in colunas_frequencia:
                colunas_frequencia.append(coluna)
    
    # Criação de dicionarios para substituir categóricos por numéricos
    mapeamento_yes_no = {'Yes': 1,'No': 0}
    mapeamento_frequencia = {'Never': 0,'Rarely': 1, 'Sometimes': 2,'Very frequently': 3}
    
    # Aplicando o mapeamento para 'Yes'/'No' e convertendo para float
    for col in colunas_yes_no:
        ds[col] = ds[col].map(mapeamento_yes_no).astype(float)
    
    for col in colunas_frequencia:
        ds[col] = ds[col].map(mapeamento_frequencia).astype(float)

#Função para exibir os bloxplots. ds = dataset, coluna = nome da coluna, orientação = h para horizontal e v para vertical, titulo = nome do titulo. (Posso fazer um tratamento caso o usuário digite outra coisa, mas no momento não é necessário)
def exibir_boxplot(ds, coluna, orientacao, titulo):

    if (orientacao == "h"):
        sns.boxplot(x=ds[coluna], orient = orientacao)
        plt.xlabel('')

    elif (orientacao == "v"):
        sns.boxplot(y =ds[coluna], orient= orientacao)
        plt.ylabel('')

    plt.title(titulo)
    plt.show()


    
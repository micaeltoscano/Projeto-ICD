import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def alterar_type(dataset):
    #A funcão converte dados categóricos em numéricos e ajusta o tipo de dado das colunas para evitar o tipo object, facilitando análises estatística

    #Criando as listas que armazenam o nome das colunas com o tipo Object
    colunas_yes_no = []
    colunas_frequencia = []
    
    for coluna in dataset.columns:
        # Verificando se todos os valores da coluna são Yes ou No.
        if dataset[coluna].dropna().isin(['Yes', 'No']).all():  #Obs: Usando dropna para tirar valores NaN que interferem no resultado.
            if coluna not in colunas_yes_no: #Adicionando apenas nomes únicos nas listas.
                colunas_yes_no.append(coluna)
                
        # Verificando se todos os valores da coluna são 'Never', 'Rarely', 'Sometimes', 'Very frequently'
        if dataset[coluna].dropna().isin(['Never', 'Rarely', 'Sometimes', 'Very frequently']).all():
            if coluna not in colunas_frequencia:
                colunas_frequencia.append(coluna)
    
    # Criação de dicionarios para substituir categóricos por numéricos
    mapeamento_yes_no = {'Yes': 1,'No': 0}
    mapeamento_frequencia = {'Never': 0,'Rarely': 1, 'Sometimes': 2,'Very frequently': 3}
    
    # Aplicando o mapeamento para 'Yes'/'No' e convertendo para float
    for col in colunas_yes_no:
        dataset[col] = dataset[col].map(mapeamento_yes_no).astype(float)
    
    for col in colunas_frequencia:
        dataset[col] = dataset[col].map(mapeamento_frequencia).astype(float)

def exibir_boxplot(dataset, coluna, orientacao, titulo):

    #Função para exibir os bloxplots. ds = dataset, coluna = nome da coluna, orientação = "h" para horizontal e "v" para vertical, titulo = nome do titulo. 

    if (orientacao == "h"):
        sns.boxplot(x=dataset[coluna], orient = orientacao)
        plt.xlabel('') 

    elif (orientacao == "v"):
        sns.boxplot(y =dataset[coluna], orient= orientacao)
        plt.ylabel('')

    plt.title(titulo)
    plt.show()

def boxplot_de_varias(dataset, titulo, tamanho_x, tamanho_y, legenda, *colunas):

    #Função para exibir mais de um boxplot por vez.
    
    plt.figure(figsize=(tamanho_x, tamanho_y))
    sns.boxplot(data = dataset[list(colunas)])

    plt.xticks(rotation=45,ha='right', va='top')  
    plt.title(titulo)
    plt.figtext(0.93, 0.5, legenda, va='center', ha='left', fontsize=10)
    plt.show()
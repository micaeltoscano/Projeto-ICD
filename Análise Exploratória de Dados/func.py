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

##############################################################################################

def exibir_boxplot(dataset, coluna, orientacao='v', titulo=''):
    
    # Definindo uma cor suave e configurando o estilo do gráfico
    sns.set(style='whitegrid')  # Estilo clean com fundo claro
    plt.figure(figsize=(6, 4))  # Tamanho da figura ajustado

    # Condições para orientação do boxplot
    if orientacao == 'h':
        sns.boxplot(x=dataset[coluna], color='#3498db', linewidth=1)  # Boxplot horizontal com cor azul suave
        plt.xlabel(coluna, fontsize=14)  # Nome da coluna no eixo X
        plt.ylabel('')  # Remover rótulo do eixo Y para horizontal
    elif orientacao == 'v':
        sns.boxplot(y=dataset[coluna], color='#3498db', linewidth=1)  # Boxplot vertical com cor azul suave
        plt.ylabel(coluna, fontsize=14)  # Nome da coluna no eixo Y
        plt.xlabel('')  # Remover rótulo do eixo X para vertical

    # Adicionando o título com tamanho ajustado
    plt.title(titulo, fontsize=16)

    # Ajustando os ticks dos eixos
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    # Exibir o gráfico
    plt.show()

###############################################################################################

def boxplot_de_varias(dataset, titulo='', tamanho_x=10, tamanho_y=6, legenda='', *colunas):
    
    # Definindo o estilo clean com grades e tamanho da figura
    sns.set(style='whitegrid')
    plt.figure(figsize=(tamanho_x, tamanho_y))  # Ajusta o tamanho da figura

    # Criação dos boxplots múltiplos com cores suaves
    sns.boxplot(data=dataset[list(colunas)], palette='viridis', linewidth=1)  # Paleta 'coolwarm' para variar entre azul e vermelho

    # Melhorias nas labels e título
    plt.xticks(rotation=45, ha='right', va='top', fontsize=12)  # Rotações dos nomes das colunas para maior clareza
    plt.title(titulo, fontsize=16)  # Título com fonte maior e negrito

    # Adicionando a legenda ao lado direito
    plt.figtext(0.93, 0.5, legenda, va='center', ha='left', fontsize=10, bbox=dict(facecolor='none', edgecolor='gray'))

    # Ajustando os ticks e visibilidade
    plt.yticks(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)  # Grade suave para melhorar a leitura dos valores

    # Exibindo o gráfico
    plt.show()

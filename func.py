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

def limpeza(df):
    media_idade = df["Age"].mean()
    df["Age"] = df["Age"].fillna(media_idade)
    
    moda_streaming = df['Primary streaming service'].mode()[0]
    df['Primary streaming service'] = df['Primary streaming service'].fillna(moda_streaming)
    
    moda_ww = df['While working'].mode()[0]
    df['While working'] = df['While working'].fillna(moda_ww)
    
    moda_instru = df['Instrumentalist'].mode()[0]
    df['Instrumentalist'] = df['Instrumentalist'].fillna(moda_instru)
    
    moda_Composer = df['Composer'].mode()[0]
    df['Composer'] = df['Composer'].fillna(moda_Composer)
    
    moda_Foreign_languages = df['Foreign languages'].mode()[0]
    df['Foreign languages'] = df['Foreign languages'].fillna(moda_Foreign_languages)
    
    mediana_bpm = df['BPM'].median()
    df.loc[df["BPM"] > 300, "BPM"] = mediana_bpm
    
    media_bpm = df['BPM'].mean()
    df["BPM"] = df["BPM"].fillna(media_bpm)
    
    mode_ME = df["Music effects"].mode()[0]
    df["Music effects"] = df["Music effects"].fillna(mode_ME)

def traducao(df):
    colunas_traduzidas = [
    "data_e_hora_envio", "idade", "servico_de_streaming_principal",
    "horas_por_dia", "enquanto_trabalha",
    "instrumentalista", "compositor", "genero_fav",
    "exploratorio", "em_outros_idiomas", "bpm",
    "classica", "country",
    "edm", "folk", "gospel",
    "hip_hop", "jazz", "kpop",
    "latin", "lofi", "metal",
    "pop", "rb", "rap",
    "rock", "musica_videogame",
    "ansiedade", "depressao", "insonia", "toc",
    "efeitos_na_saude_mental", "permissoes"
]

    legenda = """
    0 - Nunca
    1 - Raramente
    2 - Algumas vezes
    3 - Bem frequentemente """

    df.columns = colunas_traduzidas
    
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

def grafico_barra(df, coluna, titulo, x_label, y_label, legenda ):
    plt.figure(figsize=(12, 6))
    df.set_index(coluna).plot(kind='bar', stacked=False, alpha=0.75)
    
    # Adicionando título e rótulos
    plt.title(titulo)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo x
    plt.legend(title= legenda)
    
    plt.show()




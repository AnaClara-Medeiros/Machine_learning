# -*- coding: utf-8 -*-
"""People_analytics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VEWTekUhklykNPwfUCqTCbJdq8v3DqYH

# **DATA SCIENCE PARA MATH DE CURRÍCULOS COM VAGAS DE EMPREGO**

---

# Leitura do Arquivo PDF
"""

!pip install pdfplumber

import pdfplumber #leitura de PDF e transformação em tabelas
import nltk #processsamneto de texto

arquivoPDF = pdfplumber.open('/content/Juliana.pdf') #abrindo o currículo PDF e salvando

primeira_pagina = arquivoPDF.pages[0] #salvar aqui a página 1 do currículo

textoCRU = primeira_pagina.extract_text() #extrair o texto desta página do currículo
textoCRU

arquivoPDF.metadata #dados de edição (onde foi feito, última edição)

arquivoPDF.hyperlinks #encontrar links no currículo

print(textoCRU) #printar mais bonitinho o texto que extraiu

"""# Pré - processamento do Texto"""

nltk.download('punkt')# baixar os pacotes nltk_data

#a função .word_tokenize quebra o texto em palavras individuais e gera uma lista com essas palavras

lista_de_palavras = nltk.tokenize.word_tokenize(textoCRU)
lista_de_palavras

#padronizando as palavras com o Lower para todas ficarem minúsculas

lista_de_palavras = [palavra.lower() for palavra in lista_de_palavras] #para cada palavra na lista, lower()

lista_de_palavras

#criar uma lista com as pontuações que queremos remover

pontuacao = ['(', ')', ":", ";", ',', '[', ']']

#criar uma lista com Stop Word, palavras que não tem sentido, só faz ligação entre palavras

nltk.download('stopwords')

stop_words = nltk.corpus.stopwords.words('portuguese') #usar o stopword em PORTUGUES
stop_words

#criação de uma lista sem STOPWORD e sem PONTUAÇÃO

keywords = [palavra for palavra in lista_de_palavras if not palavra in stop_words and not palavra in pontuacao]
#salava essa palavra se ela não estiver nem em stopword e nem em pontuação

keywords

#tamanho da lista

len(keywords)

#concatenar as palavras para ter um texto só e não lista

textocv =  " ".join(s for s in keywords)
textocv

"""# WordCloud - Nuvem de Palavras"""

#gerar uma wordcloud

from wordcloud import WordCloud


wordcloud = WordCloud(background_color = '#0f54c9', 
                      max_font_size = 150, 
                      width = 1280, 
                      height = 720, 
                      colormap= 'Blues').generate(textocv) #parâmetros de configuração

# mostrar a imagem final
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(16, 9)) #criar o gráfico
ax.imshow(wordcloud) #mostrar imagem
ax.set_axis_off() #eixos da imagem
plt.imshow(wordcloud)
#wordcloud.to_file("wordcloud.png") #gerar um arquivo com essa imagem
plt.show()

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def NuvemDePalavras(cv, salvar = True):
    '''
    cv: caminho de um arquivo PDF 
    '''
    arquivoPDF = pdfplumber.open(cv)
    primeira_pagina = arquivoPDF.pages[0]  #lê apenas a primeira página
    textoCRU = primeira_pagina.extract_text()

    lista_de_palavras = nltk.tokenize.word_tokenize(textoCRU)  # transforma o texto cru em uma lista de termos
    lista_de_palavras = [palavra.lower() for palavra in lista_de_palavras]  # deixando tudo minusculo

    keywords = [palavra for palavra in lista_de_palavras if not palavra in stop_words and not palavra in pontuacao]  # tira as pontuacoes e stopwords 
    textocv = " ".join(s for s in keywords)  # junta tudo em um texto só novamente. 


    wordcloud = WordCloud(background_color = '#0f54c9', 
                          max_font_size = 150, 
                          width = 1280, 
                          height = 720, 
                          colormap= 'Blues').generate(textocv) 
 
    # mostrar a imagem final
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.imshow(wordcloud)
    ax.set_axis_off()
    plt.imshow(wordcloud)

    if salvar:
        wordcloud.to_file("wordcloud.png")
        
    plt.show()

"""# Entrada das Vagas de Emprego

Vaga 1 - DS Senior: https://www.linkedin.com/jobs/view/2592718801/?alternateChannel=search&refId=HcViZqV2vjZAXA0OvOZrjQ%3D%3D&trackingId=6n427gmxJ%2BH5bnRHI0T5Lg%3D%3D

Vaga 2 - DS Junior: https://www.linkedin.com/jobs/view/2621616275/?alternateChannel=search&refId=I4M3V3mzbgz5oU5EfgwJxw%3D%3D&trackingId=4gDNWcSbeeVhAr15Vs2kaA%3D%3D

Vaga 3 - Engenheiro de Dados: https://www.linkedin.com/jobs/view/2596248068/?alternateChannel=search&refId=sI8VCh%2FcadPug6NsBop4sA%3D%3D&trackingId=uMjFL1VlttYcK4XiXkcToA%3D%3D

Vaga 4 - Marketing: https://www.linkedin.com/jobs/view/2601831935/?alternateChannel=search&refId=J6jCHp9UlXvGcv2qAD132w%3D%3D&trackingId=cZ4J1BVrDvBhutTRklbPPw%3D%3D
"""

import pandas as pd

vagas = pd.read_excel('vagas.xlsx', sheet_name = None)

n_vagas = len(vagas.keys())
nome_vagas = list(vagas.keys())

n_vagas

nome_vagas

# transformando a saida numa lista de dataframes (cada dataframe representa uma vaga)
vagas = [vagas[nome_vagas[i]] for i in range(n_vagas)]

vagas[0]

vaga1 = vagas[0] #salvar em uma variável 
vaga1

palavras_chaves = list(vaga1['palavras-chave']) #criar uma lista para guardar essas palavras chaves
palavras_chaves

# Clear Sale Data Science Analytics Senior
import numpy as np

limite = 5 #máximo de vezes que cada palavra pode aparecer

pesos = list(vaga1['pesos']) #pegando os pesos de cada palavra chave que tinha no excel
palavras_chaves = list(vaga1['palavras-chave']) #palavras chaves da vaga
pmax = np.sum(np.array(pesos) * limite) #número máximo de pontos que cada candidato pode fazer
print(pmax)

#quantas vezes cada palavra chave apareceu no currículo

cont = [textocv.count(pc) for pc in palavras_chaves]
cont

# limitar pelo threshold
def aux(x):
    return x if x <= limite else limite #se o n° de vezes que apareceu a palavra chave no meu currículo
                                        # for maior que o limite, então troca pelo limite, s enão deixa o n° de vezes (assim não nurla o sistema)

cont = [aux(i) for i in cont]
cont #agora mostra o número de repetições de cada termo controlado pelo meu limite

score = ((np.array(cont) * pesos).sum()/pmax).round(4)
#pega quantas vezes apareceu a palavra no CV e multiplica pelo peso dela
#soma todas esses multilicações
#divide pelo peso máximo
#deixa com quatro casas decimais

score

"""# Match de CV com vagas"""

# função entrada: CV saida, vaga - saida: score

pontuacao = ['(', ')', ';', ':', '[', ']', ',']
stop_words = nltk.corpus.stopwords.words('portuguese')

def MatchCV(cv, vaga, limite = 5):
    '''
    cv: caminho de um arquivo PDF
    vaga: dataset de palavras-chave e pesos
    '''

    arquivoPDF = pdfplumber.open(cv)
    primeira_pagina = arquivoPDF.pages[0]  #lê apenas a primeira página
    textoCRU = primeira_pagina.extract_text()

    lista_de_palavras = nltk.tokenize.word_tokenize(textoCRU)  # transforma o texto cru em uma lista de termos
    lista_de_palavras = [palavra.lower() for palavra in lista_de_palavras]  # deixando tudo minusculo

    keywords = [palavra for palavra in lista_de_palavras if not palavra in stop_words and not palavra in pontuacao]  # tira as pontuacoes e stopwords 
    textocv = " ".join(s for s in keywords)  # junta tudo em um texto só novamente. 

    pesos = list(vaga['pesos'])
    palavras_chaves = list(vaga['palavras-chave'])
    cont = [textocv.count(pc) for pc in palavras_chaves]  # conta quantas vezes cada termo da vaga aparece no texto do cv

    def aux(x, limite):
        return x if x <= limite else limite

    cont = [aux(i, limite) for i in cont]   # coloca o limite na contagem de palavras

    pmax = np.sum(np.array(pesos) * limite) 

    score = ((np.array(cont) * pesos).sum()/pmax).round(4)

    return score

MatchCV('/content/Juliana.pdf', vagas[2]) #para a vaga de engenheiro já não dá um bom Match

"""Caso queira avaliar mais de um currículo por vez!"""

lista_de_vagas = vagas

lista_de_cvs = ['/content/CV_Raquel.pdf',
                '/content/Curriculo Matheus Henrique.pdf']

lista_de_vagas[0]

# Lista de Listas, cada lista interna é score de uma pessoa nas vagas
pessoas = [[MatchCV(cv, vaga) for vaga in lista_de_vagas] for cv in lista_de_cvs]
pessoas

# filtro para pegar apenas os nomes das pessoas na lista de caminhos
nomes = [cv.split('/')[-1].split('.')[0] for cv in lista_de_cvs]
#pegar a palavra que estiver entre a barra e entre o ponto

# Conjunto de dados comos matches das pessoas com as vagas
matchs = pd.DataFrame(pessoas, columns = nome_vagas, index = nomes)
#transformar em uma tabela
#trás o match de cada um com a vaga, nas colunas o nome das vagas e os índices serão os nomes das pessoas

matchs.sort_values(by = 'eng_dados', ascending = False)

#colocar um hanking pelo maior em eng.dados

for x in nome_vagas:
    valores = nome_vagas[x]

fig = go.Figura(dados=[
    go.Bar(name='Raquel', x=valores , y=matchs),
    go.Bar(name='Matheus', x=valores, y=matchs)
  ])

fig.update_layout(barmode='group')
fig.show()

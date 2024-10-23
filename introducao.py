import pandas as pd # Importando pandas com o "apelido" pd;

sea_df = pd.read_excel("Mar.xlsx") # Importando os dados do arquivo "Mar.xlsx" (Excel);

print(sea_df) # Visualizando os dados;
print(sea_df.head(10)) # Visualizando apenas as 10 primeiras linhas;
print(sea_df.shape) # Visaulizando a quantidade de linhas e colunas da planilha;
print(sea_df.describe()) # Visualizando diferentes dados sobre as colunas numéricas da planilha;

seaLevel_s = sea_df["GMSL"] # Criando uma série para a coluna "GMSL";
seaLU_s = sea_df[["GMSL","GMSL uncertainty"]] # Criando uma série para múltiplas colunas;

print(sea_df.loc[1]) # Localizando uma linha utilizando o índice "1" como base;
print(sea_df.loc[1:5]) # Localizando as linhas 1 à 5;

print(sea_df.loc[sea_df["GMSL uncertainty"] == 24.2]) # Localizando linhas através de um critério;
# Regra da função .loc => [Linhas, Colunas]
print(sea_df.loc[sea_df["GMSL uncertainty"] == 24.2, ["Time"]]) # Exibindo apenas uma coluna dos dados que atendendem ao critério;

sea_df["% Erro"]= round((sea_df["GMSL uncertainty"]*100)/sea_df["GMSL"],2) # Criando a coluna "% erro" através do arrendondamento de um cálculo;
sea_df.loc[:, "Órgão coletor"] = "NASA" # Adicionando uma coluna e preenchendo ela da MELHOR forma;

sea_df = sea_df.dropna() # Deletando linhas com algum valor vazio;
sea_df = sea_df["Órgão coletor"].fillna("NASA") # Preenchendo valores vazios;

seadf_len = sea_df["Time"].value_counts() #Contando os valores de uma coluna;



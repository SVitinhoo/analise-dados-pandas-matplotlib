from pathlib import Path
from pandas import read_csv, concat, DataFrame
import matplotlib.pyplot as plt

from dateutil.relativedelta import relativedelta
from datetime import datetime

DIR_HOME = Path(__file__).parent
DIR_CSV = DIR_HOME / "csv"
FILE = DIR_HOME / "final.csv"

def tempo_medio(data_i, data_f):
    data_inicio = datetime.strptime(data_i.strip(), "%Y-%m-%d")
    data_fim = datetime.strptime(data_f.strip(), "%Y-%m-%d")
    tempo = relativedelta(data_fim, data_inicio)
    return tempo.years * 12 + tempo.months + tempo.days / 30

     
if not FILE.exists():
    lista = list()
    for arquivo in DIR_CSV.iterdir():
        file = read_csv(arquivo, sep=";", header=0)
        lista.append(file)
        
    df = concat(lista)
    DataFrame.to_csv(df, "final.csv", sep=";", index=False)
    

df = read_csv(FILE, sep=";", low_memory=False)

df_empresas_unicas = df.drop_duplicates(subset=["Empresa"])


# Grande Área do Conhecimento = Área do Conhecimento
qtd_area = df_empresas_unicas["Grande Área do Conhecimento"].value_counts().copy()
qtd_area.rename("Quantidade", inplace=True)
qtd_area.sort_values(ascending=False, inplace=True)
qtd_area.index.rename("Área do Conhecimento", inplace=True)
qtd_area.to_csv("resultado/area_conhecimento.csv", sep=";")


# Área do Conhecimento = Subárea do Conhecimento
qtd_subarea = df_empresas_unicas["Área do Conhecimento"].value_counts().copy()
qtd_subarea.rename("Quantidade", inplace=True)
qtd_subarea.sort_values(ascending=False, inplace=True)
qtd_subarea.index.rename("Subárea do Conhecimento", inplace=True)
qtd_subarea.to_csv("resultado/subarea_conhecimento.csv", sep=";")


# alguns dados vieram concatenados
df_cidades = df_empresas_unicas[["Cidade Instituição"]].copy()
padrao_concat = r'[a-z][A-Z]'
# pega as linhas concatenadas
linhas_concat = df_cidades['Cidade Instituição'].str.contains(padrao_concat, regex=True, na=False)
# mantendo as linhas que não estão no padrão descrito (removendo com os padrões concatenados)
df_cidades_limpo = df_cidades[~linhas_concat]
qtd_cidade = df_cidades_limpo["Cidade Instituição"].value_counts().reset_index()
qtd_cidade.rename(columns={"count": "Quantidade", "Cidade Instituição": "Cidade"}, inplace=True)
qtd_cidade.to_csv("resultado/empresas_por_cidade.csv", sep=";", index=False)



df_rp = df_empresas_unicas[df_empresas_unicas["Cidade Instituição"] == "Ribeirão Preto"].copy()
qtd_area_rp = df_rp[["Instituição", "Grande Área do Conhecimento"]].fillna("Interdisciplinar")
qtd_area_rp.rename(inplace=True, columns={"Grande Área do Conhecimento": "Área do Conhecimento", "Instituição": "Empresa"})
qtd_area_rp.to_csv("resultado/empresas_em_rp.csv", sep=";", index=False)



# Assuntos = Data de Início
# Data de Início = Data de Término
df_tempo = df_empresas_unicas[["Assuntos", "Data de Início", "Grande Área do Conhecimento"]].copy()
df_tempo.dropna(subset=["Assuntos", "Data de Início", "Grande Área do Conhecimento"], inplace=True)
df_tempo["Tempo"] = df_tempo.apply(lambda x: tempo_medio(x["Assuntos"], x["Data de Início"]), axis= 1)

df_media_por_area = df_tempo.groupby("Grande Área do Conhecimento").agg(
Média_Tempo=("Tempo", "mean"),
Qtd_Materias=("Tempo", "count")
).reset_index().sort_values(by="Qtd_Materias", ascending=False)

# O tempo médio é em meses
df_media_por_area.rename(inplace=True, columns={"Grande Área do Conhecimento": "Área do Conhecimento", "Média_Tempo": "Tempo médio em meses", "Qtd_Materias": "Quantidade"})
df_media_por_area.to_csv("resultado/tempo_medio.csv", sep=";", index=False, decimal=",")

# Criando os gráficos
# 1º 
qtd_area = qtd_area.iloc[:10]
qtd_area.plot(kind="barh", color = "salmon", figsize=(10, 6), width=0.7)
plt.title("Top 10 Áreas do Conhecimento com Mais Empresas", fontsize=14, pad=15)
plt.ylabel("Área do Conhecimento", fontsize=11)
plt.xlabel("Quantidade de Empresas", fontsize=11)
plt.yticks(fontsize=10)
plt.xticks(fontsize=10)
plt.gca().invert_yaxis()
plt.grid(True, axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("resultado/area_conhecimento.jpg", dpi = 150)
plt.close()

qtd_subarea = qtd_subarea.iloc[:10]
qtd_subarea.plot(kind="barh", color = "#057F8D", figsize=(12, 6), width=0.7)
plt.title("Top 10 Subáreas do Conhecimento com Mais Empresas", fontsize=16, pad=20)
plt.ylabel("Subárea do Conhecimento", fontsize=11)
plt.xlabel("Quantidade de Empresas", fontsize=11)
plt.yticks(fontsize=10)
plt.xticks(fontsize=10)
plt.gca().invert_yaxis()
plt.grid(True, axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("resultado/subarea_conhecimento.jpg", dpi = 150)
plt.close()

# 2º
qtd_cidade = qtd_cidade.iloc[:10]
qtd_cidade.plot(kind="bar", color = "skyblue", figsize = (10, 6) , width = 0.7, x = "Cidade", legend = False, y = "Quantidade")
plt.title("Top 10 Cidades com Mais Empresas", fontsize = 14, pad = 15)
plt.xlabel("Cidades", fontsize = 11)
plt.ylabel("Quantidade", fontsize= 11)
plt.xticks(rotation=45, ha="right", fontsize=10)
plt.yticks(fontsize = 10)
plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("resultado/empresas_por_cidade.jpg", dpi = 150)
plt.close()

# 3º -> não precisa de grafico
# 4º
df_media_por_area = df_media_por_area[:15]
df_media_por_area.plot(kind="line", x="Área do Conhecimento", y="Tempo médio em meses", color="darkorchid", marker="o", linewidth=2, figsize=(12, 6), legend=False, linestyle = "")
plt.title("Média de Tempo das 15 Áreas com Maior Volume de Amostra", fontsize = 14, pad = 15)
plt.ylabel("Tempo Médio (Meses)", fontsize = 11)
plt.xlabel("Área do Conhecimento", fontsize = 11)
plt.xticks(rotation=45, ha="right", fontsize=9, ticks=range(len(df_media_por_area)), labels=df_media_por_area["Área do Conhecimento"])
plt.yticks(fontsize=10)
plt.grid(True, axis='both', linestyle='--', alpha=0.5)

for i, linha in df_media_por_area.reset_index().iterrows():
    plt.text(
        x=i + 0.2,                                      
        y=linha["Tempo médio em meses"] -0.5,
        s=str(int(linha["Quantidade"])),
        ha='center',
        va='bottom',
        fontsize=9,
        color='darkorchid',
        weight='bold'
    )

plt.tight_layout()
plt.savefig("resultado/tempo_medio.jpg", dpi=150)
plt.close()



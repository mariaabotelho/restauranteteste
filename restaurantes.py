import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

caminho_do_arquivo = "dados_restaurantesduogourmet.xlsx"

try:
    df = pd.read_excel(caminho_do_arquivo)
except Exception as e:
    st.error(f"Erro ao carregar o arquivo de dados: {e}")
    st.stop()

categoria_selecionada = st.selectbox("Escolha uma categoria:", df['categoria'].unique())

dados_filtrados = df[df['categoria'] == categoria_selecionada]

contagem_por_bairro = dados_filtrados['bairro'].value_counts()

st.write(f"Gráfico mostrando a quantidade de restaurantes por bairro na categoria: {categoria_selecionada}")
plt.figure(figsize=(10, 5))
plt.bar(contagem_por_bairro.index, contagem_por_bairro.values, color='blue')
plt.xlabel('Bairro')
plt.ylabel('Número de Restaurantes')
plt.title('Distribuição de Restaurantes por Bairro')
plt.xticks(rotation=45)
st.pyplot(plt)

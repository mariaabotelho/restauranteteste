import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


caminho_do_arquivo = "restaurantes_duo_gourmet (1).xlsx"
df = pd.read_excel(caminho_do_arquivo)


if 'categoria' not in df.columns:
    st.error("A coluna 'categoria' não foi encontrada. Verifique se o nome está correto.")
    st.stop()  # Parar execução se a coluna não for encontrada

# pessoa vai selecionar uma categoria
categoria_selecionada = st.selectbox("Escolha uma categoria:", df['categoria'].unique())


dados_filtrados = df[df['categoria'] == categoria_selecionada]

# vai contar restaurantes por bairro na categoria que selecionar
contagem_por_bairro = dados_filtrados['bairro'].value_counts()

# Criando um gráfico de barras
st.write(f"Gráfico mostrando a quantidade de restaurantes por bairro na categoria: {categoria_selecionada}")
plt.figure(figsize=(10, 5))
plt.bar(contagem_por_bairro.index, contagem_por_bairro.values, color='blue')
plt.xlabel('Bairro')
plt.ylabel('Número de Restaurantes')
plt.title('Distribuição de Restaurantes por Bairro')
plt.xticks(rotation=45)
st.pyplot(plt)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


caminho_do_arquivo = "reviews_road_47 (6).xlsx"
df = pd.read_excel(caminho_do_arquivo)


if 'categoria' not in df.columns:
    st.error("A coluna 'Nota' não foi encontrada. Verifique se o nome está correto.")
    st.stop()  # se a coluna não for encontrada no meu df

# pessoa vai selecionar uma nota
Nota_selecionada = st.selectbox("escolhe uma nota:", df['Nota'].unique())


dados_filtrados = df[df['Nota'] == Nota_selecionada]

# vai contar restaurantes por bairro na categoria que selecionar     vai contar Comentário por user na nota que selecionar
contagem_por_user = dados_filtrados['User'].value_counts()

# vai criar um gráfico
st.write(f"gráfico mostrando a quantidade de comentários por user na nota: {Nota_selecionada}")
plt.figure(figsize=(10, 5))
plt.bar(contagem_por_User.index, contagem_por_User.values, color='blue')
plt.xlabel('User')
plt.ylabel('Número de Comentário')
plt.title('Distribuição de Comentário por User')
plt.xticks(rotation=45)
st.pyplot(plt)

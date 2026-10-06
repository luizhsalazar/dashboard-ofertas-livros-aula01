"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st
import dados


def main():
    st.set_page_config(layout="wide")
    st.title("📚 Dashboard de Livros")

    col1, col2, col3, col4 = st.columns(4)

    livros = dados.ler_livros()

    qtd_livros = len(livros)
    col1.metric("Total de Livros", qtd_livros)

    preco_medio = dados.calcular_preco_medio(livros)
    col2.metric("Preço médio", f"£{preco_medio:.2f}")

    cinco_estrelas = dados.contar_cinco_estrelas(livros)
    col3.metric("Qtd. livros 5 Estrelas", cinco_estrelas)

    mais_caro = dados.livro_mais_caro(livros)
    col4.metric("Livro mais Caro", mais_caro["preco"])
    col4.caption(mais_caro["titulo"])

    st.dataframe(livros)

if __name__ == "__main__":
    main()

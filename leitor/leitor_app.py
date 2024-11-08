from docling.document_converter import DocumentConverter
import streamlit as st
import os

def list_articles():
    """
    Lista todos os artigos na pasta assets/artigos
    Retorna uma lista com os nomes dos arquivos
    """
    articles_path = "leitor/assets/artigos"
    
    # Verifica se o diretório existe
    if not os.path.exists(articles_path):
        st.error(f"A pasta {articles_path} não existe. Por favor, crie-a e adicione seus artigos.")
        return []
    
    # Lista todos os arquivos no diretório
    articles = [f for f in os.listdir(articles_path) if os.path.isfile(os.path.join(articles_path, f))]
    
    return articles

def read_article(article_name):
    """
    Lê o conteúdo do artigo selecionado
    """
    try:
        converter = DocumentConverter()
        result = converter.convert(os.path.join("leitor/assets/artigos", article_name))
        return result.document.export_to_markdown()
    except Exception as e:
        st.error(f"Erro ao ler o artigo: {str(e)}")
        return None

def main():
    st.title("Seletor de Artigos")
    
    # Lista os artigos disponíveis
    articles = list_articles()
    
    if not articles:
        st.warning("Nenhum artigo encontrado na pasta assets/artigos")
        return
    
    # Adiciona uma opção vazia no início
    articles_with_empty = ["Selecione um artigo..."] + articles
    
    # Campo de seleção
    selected_article = st.selectbox(
        "Escolha um artigo para ler:",
        articles_with_empty
    )
    
    # Mostra o conteúdo do artigo selecionado
    if selected_article and selected_article != "Selecione um artigo...":
        st.subheader(f"Conteúdo do artigo: {selected_article}")
        
        content = read_article(selected_article)
        if content:
            st.text_area("", value=content, height=400)

if __name__ == "__main__":
    main()
from docling.document_converter import DocumentConverter
import streamlit as st
import os, base64
from dotenv import load_dotenv
from leitor.llm_prompts import gerar_sumario

def status_inicial():
    if 'texto_exportado' not in st.session_state:
        st.session_state.texto_exportado = ""
    if 'sumario_artigo' not in st.session_state:
        st.session_state.sumario_artigo = []

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
    
def load_article(article_name):
    with open(os.path.join("leitor/assets/artigos", article_name), "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')

def main():
    st.set_page_config(layout="wide", page_title="Tradutor", page_icon="🤖")
    st.title("🤖📄✨ Tradutor")
    st.info("Diagramadores: Conecte os pontos, desenhe o futuro e torne cada processo mais claro do que nunca! 🔗✨")
    
    with st.sidebar:
        # Lista os artigos disponíveis
        articles = list_articles()
        
        if not articles:
            st.warning("Nenhum artigo encontrado na pasta assets/artigos")
            return
        
        # Adiciona uma opção vazia no início
        articles_with_empty = ["Selecione um artigo..."] + articles
        
        # Campo de seleção
        selected_article = st.sidebar.selectbox(
            "Escolha um artigo para ler:",
            articles_with_empty
        )

        col_exportar, col_sumario, col_processar = st.columns(3)

        with col_exportar:
            if st.button("Exportar", use_container_width=True):
                st.session_state.texto_exportado = read_article(selected_article)

        with col_sumario:
            if st.button("Sumarizar", use_container_width=True):
                if not st.session_state.sumario_artigo:                
                    st.session_state.sumario_artigo = gerar_sumario(st.session_state.texto_exportado)            
                
                for menu in st.session_state.sumario_artigo:
                    st.write(menu.replace("##", ""))

        with col_processar:
            if st.button("Processar", use_container_width=True):
                st.write("Processado")
        
        st.button("Reiniciar", use_container_width=True)

        st.divider()

    if st.session_state.texto_exportado:

        col_pdf, col_texto = st.columns(2)

        with col_pdf:
            st.write("")
            st.write("")
            base64_pdf = load_article(selected_article)
            pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" style="overflow: auto; width: 100%; height: 600px;" type="application/pdf">'
            st.markdown(pdf_display, unsafe_allow_html=True)

        with col_texto:
            st.session_state.texto_exportado = st.text_area("", value=st.session_state.texto_exportado, height=600)
        
        

if __name__ == "__main__":
    load_dotenv()
    status_inicial()
    main()
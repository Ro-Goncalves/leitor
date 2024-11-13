from docling.document_converter import DocumentConverter
import streamlit as st
import os, base64
from ensi.llm_prompts import gerar_sumario
from ensi.utils.menu_extractor import extract_menu_content

def status_inicial():
    if 'texto_exportado' not in st.session_state:
        st.session_state.texto_exportado = ""
    if 'sumario_artigo' not in st.session_state:
        st.session_state.sumario_artigo = ()
    if 'bloquear_opcoes_exportacao' not in st.session_state:
        st.session_state.bloquear_opcoes_exportacao = False
    if 'menu_selecionado' not in st.session_state:
        st.session_state.menu_selecionado = False
    if 'texto_menu' not in st.session_state:
        st.session_state.texto_menu = ""

def list_articles():
    """
    Lista todos os artigos na pasta assets/artigos
    Retorna uma lista com os nomes dos arquivos
    """
    articles_path = "ensi/assets/artigos"
    
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
        result = converter.convert(os.path.join("ensi/assets/artigos", article_name))
        return result.document.export_to_markdown()
    except Exception as e:
        st.error(f"Erro ao ler o artigo: {str(e)}")
        return None
    
def load_article(article_name):
    with open(os.path.join("ensi/assets/artigos", article_name), "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')
                
def main():
    st.set_page_config(layout="wide", page_title="Tradutor", page_icon="🤖")
    
    st.title("🤖📄✨ Tradutor")
    st.info("Diagramadores: Conecte os pontos, desenhe o futuro e torne cada processo mais claro do que nunca! 🔗✨")
    
    
    with st.sidebar:
        
        st.subheader("PDF Para Texto")
        # Lista os artigos disponíveis
        articles = list_articles()
        
        if not articles:
            st.warning("Nenhum artigo encontrado na pasta assets/artigos")
            return
        
        # Adiciona uma opção vazia no início
        articles_with_empty = ["Selecione um artigo..."] + articles
        
        # Campo de seleção
        selected_article = st.sidebar.selectbox(
            label="Escolha um artigo para ler:",
            options=articles_with_empty,
            disabled=st.session_state.bloquear_opcoes_exportacao
        )

        col_exportar, col_sumario = st.columns(2)
        
        with col_exportar:
            if st.button(
                label="Exportar", 
                disabled=st.session_state.bloquear_opcoes_exportacao,
                use_container_width=True):
                
                st.session_state.texto_exportado = read_article(selected_article)

        with col_sumario:
            if st.button(
                label="Sumarizar",
                disabled=st.session_state.bloquear_opcoes_exportacao,
                use_container_width=True):
                
                st.session_state.sumario_artigo=gerar_sumario(st.session_state.texto_exportado)
                
                st.session_state.bloquear_opcoes_exportacao=True
                st.rerun()
               
        if st.session_state.sumario_artigo:
            
            st.markdown("---")            
            st.subheader("Opções Estudo")
            
            st.session_state.menu_selecionado = st.selectbox(
                "Escolha uma opção:",
                ["Selecione um menu..."] + st.session_state.sumario_artigo
            )
            
           
            if st.button("Traduzir", use_container_width=True):
                st.write("Processado")
                
            st.markdown("---")
        
        st.button("Reiniciar", use_container_width=True)
        
    if st.session_state.texto_exportado:
        
        st.subheader("Artigo original e texto exportado")

        col_pdf, col_texto = st.columns(2)

        with col_pdf:
            st.write("")
            st.write("")
            base64_pdf = load_article(selected_article)
            pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" style="overflow: auto; width: 100%; height: 600px;" type="application/pdf">'
            st.markdown(pdf_display, unsafe_allow_html=True)

        with col_texto:
            st.session_state.texto_exportado = st.text_area("", value=st.session_state.texto_exportado, height=600)
            
    if st.session_state.menu_selecionado and (st.session_state.menu_selecionado != "Selecione um menu..."):
        
        st.subheader(f"Aprendendo com {st.session_state.menu_selecionado}")
        
        st.session_state.texto_menu = extract_menu_content(st.session_state.texto_exportado, st.session_state.menu_selecionado)
        st.markdown(st.session_state.texto_menu)
    
        
        

if __name__ == "__main__":    
    status_inicial()
    main()
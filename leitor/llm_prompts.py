from llama_index.llms.gemini import Gemini
import ast
import streamlit as st

gemini = Gemini()

def gerar_sumario(texto_artigo):
    prompt = f"""
        <artigo>
        {texto_artigo}
        </artigo>

        Você é um especialista em identificar os menus de artigos.
        Sua tarefa é retornar todos os menus do <artigo>.
        Os retorne em um formato de lista.
        Não faça comentários, retorne somente a lista.

        exemplo de retorno: ["## Menu Um", "## Menu Dois", "## Menu Três"]
    """

    completion = gemini.complete(prompt).text
    try:
        sumario_list = ast.literal_eval(completion)
        return sumario_list
    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")

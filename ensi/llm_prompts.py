from llama_index.llms.gemini import Gemini
import ast
import streamlit as st
import os

gemini = Gemini()

def gerar_sumario(texto_artigo):
    prompt = f"""
        <artigo>
        {texto_artigo}
        </artigo>

        Atue como um especialista em análise de estrutura de artigos, com experiência 
        avançada em identificar e extrair menus ou títulos de seções para estruturar 
        conteúdos de forma organizada e lógica. Sua tarefa é localizar e retornar 
        todos os menus e subtítulos dentro do elemento <artigo>.

        1. Extraia cada menu ou subtítulo presente no conteúdo, considerando apenas 
        aqueles que aparecem como títulos de seção no formato markdown 
        (ex.: "## Título da Seção").
        2. Retorne os menus em uma lista formatada JSON, mantendo a ordem em que 
        aparecem no texto.
        3. Não adicione comentários, explicações ou texto adicional fora da lista.

        Exemplo de retorno esperado: `["## Menu Um", "## Menu Dois", "## Menu Três"]`

        Observe:
        - Se não houver menus no texto, retorne uma lista vazia `[]`.
        - Ignore textos fora do escopo dos menus, mantendo o foco na estrutura hierárquica.

        Execute essa tarefa de maneira objetiva e direta.
    """
   
    try:
        completion = gemini.complete(prompt).text
        sumario_list = ast.literal_eval(completion)
        return sumario_list
    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")

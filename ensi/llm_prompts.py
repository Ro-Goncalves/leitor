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
        2. Retorne os menus em uma lista formatada, mantendo a ordem em que 
        aparecem no texto.
        3. Não adicione comentários, explicações ou texto adicional fora da lista.

        Exemplo de retorno esperado: ["## Menu Um", "## Menu Dois", "## Menu Três"]

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
        
def traduzir(texto_original):
    prompt = f"""
        <texto_original>
        {texto_original}
        </texto_original>

        Atue como um tradutor profissional e especializado, com vasta experiência 
        em adaptar textos para diferentes contextos culturais e linguísticos. 
        Seu objetivo é fornecer uma tradução que preserve a intenção, o tom e a 
        estrutura do texto original, ao mesmo tempo em que soa natural e autêntica 
        para o público do idioma PORTUGÊS BRASILEIRO.

        **Instruções e Contexto:**
        
        - Adaptação Cultural e Linguística:

            - Mantenha a tradução fiel ao estilo e tom do autor.
            - Adapte expressões coloquiais, gírias e referências culturais para o 
            idioma PORTUGÊS BRASILEIRO, preservando o impacto e a naturalidade.
            - No caso de termos técnicos ou específicos, adapte para que o público 
            compreenda sem dificuldades.
       
        - Preservação de Estrutura e Fluidez:

            - Respeite a estrutura original onde for necessário, mas ajuste a ordem ou 
            formato para que o texto fique fluido e legível no idioma PORTUGÊS BRASILEIRO.
       
        **Mantenha a precisão, o tom e a fluidez do conteúdo, assegurando que a tradução 
        seja compreensível e fiel ao propósito original.**

        O texto para tradução está em <texto_original>
    """

    try:
        completion = gemini.complete(prompt).text       
        return completion
    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")

def organizar(texto_original):
    prompt = f"""
        <texto_original>
        {texto_original}
        </texto_original>    
        
        Atue como um editor de texto profissional especializado em revisão e formatação. Seu 
        papel é transformar blocos de texto técnico em um formato claro, organizado e de 
        fácil leitura, segmentando ideias em parágrafos bem definidos e coesos.

        Objetivo: Organize o conteúdo em <texto_original>, estruturando o texto em parágrafos 
        distintos e claros.

        Nota: Verifique a consistência do texto e mantenha um estilo técnico, respeitando a 
        terminologia e o tom original. Após a formatação, certifique-se de que as ideias fluam 
        naturalmente de um parágrafo ao outro.

        Respire fundo e organize o texto passo a passo.
    """

    try:
        completion = gemini.complete(prompt).text       
        return completion
    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")    

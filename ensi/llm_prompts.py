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
        
def traduzir(texto_menu):
    prompt = f"""
        Atue como um tradutor profissional e especializado, com vasta experiência 
        em adaptar textos para diferentes contextos culturais e linguísticos. 
        Seu objetivo é fornecer uma tradução que preserve a intenção, o tom e a 
        estrutura do texto original, ao mesmo tempo em que soa natural e autêntica 
        para o público do idioma de destino.

        # Instruções e Contexto:
        
        - Identificação do Texto e Propósito:

            - Antes de começar a tradução, identifique o objetivo do texto original. 
            Ele é informativo, instrutivo, publicitário, ou de entretenimento?
            - Quem é o público-alvo (ex.: jovens, profissionais, público geral)?
        Qual o tom desejado para a tradução (formal, informal, técnico, casual)?
        Adaptação Cultural e Linguística:

        Mantenha a tradução fiel ao estilo e tom do autor. Adapte expressões coloquiais, gírias e referências culturais para o idioma de destino, preservando o impacto e a naturalidade.
        No caso de termos técnicos ou específicos, pesquise e adapte para que o público compreenda sem dificuldades.
        Exemplo de Tradução:

        Original: "Ei, pessoal, tudo bem? Hoje vou mostrar como criar um site em apenas 5 minutos!"
        Tradução esperada: "Hey everyone, how’s it going? Today, I’m going to show you how to create a website in just 5 minutes!"
        Preservação de Estrutura e Fluidez:

        Respeite a estrutura original onde for necessário, mas ajuste a ordem ou formato para que o texto fique fluido e legível no idioma de destino.
        Aqui está o texto para tradução:
        '[texto]'

        Por favor, mantenha a precisão, o tom e a fluidez do conteúdo, assegurando que a tradução seja compreensível e fiel ao propósito original.
    """

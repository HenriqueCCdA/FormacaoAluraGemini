import os
import google.generativeai as genai
from google.api_core.exceptions import NotFound
from dotenv import load_dotenv

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=CHAVE_API_GOOGLE)
MODELO = "gemini-1.5-flashzzzz"

def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro: {e}")

def salva(nome_do_arquivo, conteudo):
    try:
        with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
    except IOError as e:
        print(f"Erro ao salvar arquivo: {e}")


def analisador_sentimentos(nome_produto):

    prompt_sistema = """
        Você é um anaalisador de sentimentos de avaliações de produtos.
        Escreva um parágrado com até 50 palavras rresumindo as avaliações e
        depois atribua qual o sentimento geral para o produto.
        Identifique tambémm 3 pontos fortes e 3 pontos frracos identificados a partir das avaliações.

        # Formato de Saída

        Nome do Produto:
        Resumo de Avaliações:
        Sentimento Geral: [utilize aqui apenas Positivo, Negativo ou Neutro]
        Ponto fortes: lista com três bullets
        Pontos fracos: lista co três bullets
    """

    prompt_usuario = carrega(f"dados/avaliacoes-{nome_produto}.txt")

    print(f"Iniciando a análise de sentimentos do produto: {nome_produto}")

    llm = genai.GenerativeModel(
        model_name=MODELO,
        system_instruction=prompt_sistema,
    )
    try:
        resposta = llm.generate_content(prompt_usuario)
    except NotFound as e:
        print(f"Erro no nome do modelo: {e}")
    else:
        texto_resposta = resposta.text
        salva(f"dados/resposta-{nome_produto}", texto_resposta)

def main():
    lista_produtos = [
        "Camisetas de algodão orgânico",
        "Jeans feitos com materiais reciclados",
        "Maquiagem mineral",
    ]

    for um_produto in lista_produtos:
        analisador_sentimentos(um_produto)

if __name__ == '__main__':
    main()

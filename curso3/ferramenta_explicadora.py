from langchain.tools import BaseTool
from langchain_google_genai import ChatGoogleGenerativeAI
from my_models import GEMINI_FLASH
from my_keys import GEMINI_API_KEY
from my_helper import encode_image
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers  import StrOutputParser, JsonOutputParser
from detalhes_imagem_modelo import DetalhesImagemModelo
import ast


class FerramentaExplicadora(BaseTool):
    name: str = "FerramentaExplicadora"
    description: str = """
    Utilize esta ferramenta sempre qque for solicado que você explique um conteúdo
    para pessoas.

    # Entrada Requeridas
    - 'tema' (str): Tema principal informado na pergutan do usuário
    """

    return_direct: bool = True

    def _run(self, acao):
        acao = ast.literal_eval(acao)
        tema_paramentro = acao.get("tema", "")

        llm = ChatGoogleGenerativeAI(
            api_key=GEMINI_API_KEY,
            model=GEMINI_FLASH,
        )

        template_resposta = PromptTemplate(
            template="""
            Assuma o papel de um professor preocupado com aspectos de didática do usuário.

            1. Elabore um explicação sobre o tema {tema} que seja compreensível por
            estudantes na fase de conclusão do ensino médio
            2. Utilize exemplos do cotidiano para tornar a explicação mais fácil
            3. Caso sugira algum recurso para apoiar a explicação, lembre-se do
            cenário e contexto brasileiro.
            4. Caso você apresente um código, seja didático e utiliza Python

            Tema pergunta: {tema}
            """,
            input_variables=["tema"],
        )

        cadeia = template_resposta | llm | StrOutputParser()
        resposta = cadeia.invoke({"tema": tema_paramentro})
        return resposta

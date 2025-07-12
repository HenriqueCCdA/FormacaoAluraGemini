import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=CHAVE_API_GOOGLE)
MODELO_ESCOLHIDO = "gemini-1.5-flash"

prompt_sistema = "Liste apenas os nommes dos produto, e ofereça ua breve descrição."

configuração_modelo = {
    "temperature": 2.0,
    "top_p": 0.9,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

llm = genai.GenerativeModel(
    model_name=MODELO_ESCOLHIDO,
    system_instruction=prompt_sistema,
    generation_config=configuração_modelo,
)

pergunta = "Liste três produtos de mmoda sustentável para ir ao shopping"

resposta = llm.generate_content(pergunta)

print(f"A Resposta gerada para pergunta é: {resposta.text}")

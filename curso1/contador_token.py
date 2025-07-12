import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=CHAVE_API_GOOGLE)
MODELO_FLASH = "gemini-1.5-flash"
MODELO_PRO = "gemini-1.5-pro"

CUSTO_ENTRADA_FLASH = 0.075
CUSTO_SAIDA_FLASH = 0.30

CUSTO_ENTRADA_PRO = 3.5
CUSTO_SAIDA_PRO = 10.5

model_flash = genai.get_model(f"models/{MODELO_FLASH}")
limites_modelo_flash = {
    "tokens_entrada": model_flash.input_token_limit,
    "tokens_saida": model_flash.output_token_limit,
}

print(f"Limites do modelo flash são: {limites_modelo_flash}")

model_pro = genai.get_model(f"models/{MODELO_PRO}")
limites_modelo_pro = {
    "tokens_entrada": model_pro.input_token_limit,
    "tokens_saida": model_pro.output_token_limit,
}

print(f"Limites do modelo pro são: {limites_modelo_pro}")

llm_flash = genai.GenerativeModel(
    f"models/{MODELO_FLASH}"
)

quantidade_tokens = llm_flash.count_tokens("O que é um calça de shopping?")
print(f"A quantidade de token é: {quantidade_tokens}")

resposta = llm_flash.generate_content("O que é uma calça de shopping?")
tokens_prompt = resposta.usage_metadata.prompt_token_count
tokens_resposta = resposta.usage_metadata.cached_content_token_count
custo_total = (tokens_prompt * CUSTO_ENTRADA_FLASH / 1_000_000 + (tokens_resposta * CUSTO_SAIDA_FLASH) / 1_000_000)
print("Custo Total U$ Flash: ", custo_total)

custo_total = (tokens_prompt * CUSTO_ENTRADA_PRO / 1_000_000 + (tokens_resposta * CUSTO_SAIDA_PRO) / 1_000_000)
print("Custo Total U$ Flash: ", custo_total)

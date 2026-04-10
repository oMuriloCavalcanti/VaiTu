import requests
import json

def interpretar_com_ia(comando: str):
    prompt = f"""
Você é um assistente que converte comandos em JSON.

Responda APENAS com JSON válido.

Comandos possíveis:
- abrir_youtube
- abrir_chrome

Formato:
{{
  "tipo": "acao",
  "acao": "nome_da_acao"
}}

OU

{{
  "tipo": "pergunta",
  "texto": "pergunta do usuário"
}}

Comando: "{comando}"
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    texto = response.json()["response"]

    try:
        return json.loads(texto)
    except:
        return {"tipo": "erro", "raw": texto}
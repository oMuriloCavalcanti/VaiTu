# core/assistant.py
from core.parser import interpretar
from core.executor import executar_acao
from services.ai_service import responder

def processar(comando: str):
    resultado = interpretar(comando)

    if resultado["tipo"] == "acao":
        executar_acao(resultado["acao"])
        return "Executando..."

    elif resultado["tipo"] == "pergunta":
        return responder(resultado["texto"])
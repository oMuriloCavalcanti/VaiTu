from services.ai_service import interpretar_com_ia
from core.executor import executar_acao

def processar(comando: str):
    resultado = interpretar_com_ia(comando)

    if resultado["tipo"] == "acao":
        executar_acao(resultado["acao"])
        return f"Executando {resultado['acao']}"

    elif resultado["tipo"] == "pergunta":
        return "Pergunta detectada (ainda não conectada à IA)"

    else:
        return "Erro ao interpretar comando"
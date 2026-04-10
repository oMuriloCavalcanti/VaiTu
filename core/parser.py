# core/parser.py
def interpretar(comando: str):
    comando = comando.lower()

    if "youtube" in comando:
        return {"tipo": "acao", "acao": "abrir_youtube"}

    if "chrome" in comando:
        return {"tipo": "acao", "acao": "abrir_chrome"}

    return {"tipo": "pergunta", "texto": comando}
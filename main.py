from core.assistant import processar

while True:
    comando = input(">> ")
    resposta = processar(comando)
    print(resposta)
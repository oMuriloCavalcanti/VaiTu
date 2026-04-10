# core/executor.py
import webbrowser
import subprocess

def abrir_youtube():
    webbrowser.open("https://youtube.com")

def abrir_chrome():
    subprocess.Popen("chrome.exe")

def executar_acao(acao):
    if acao == "abrir_youtube":
        abrir_youtube()
    elif acao == "abrir_chrome":
        abrir_chrome()
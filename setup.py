import os
import webbrowser
import threading
import time
import argparse

#Server Side Rendering (SSR) - Termo 
#registra todas as libs que estão sendo usadas no projeto
def requirements():
    requirements = "pip freeze > requirements.txt"
    os.system(requirements) #os.system serve para executar comandos do terminal

#instala todas as libs que estão sendo usadas no projeto
def install_requirements():
    requirements = "pip install -r requirements.txt"
    os.system(requirements) #os.system serve para executar comandos do terminal


#executa o servidor //////////////////////////////////////////////////////////////
def server_run():
    comando = "python manage.py runserver"
    os.system(comando) #os.system serve para executar comandos do terminal

def run():
    #executa o servidor com uma thread serada
    server_thread = threading.Thread(target=server_run)
    server_thread.start()

    #Tempo de 2 segundos
    time.sleep(2)
    #abre a página do navegador
    webbrowser.open("http://127.0.0.1:8000/")
    time.sleep(2)
    # Fecha o navegador após o servidor ser executado
    browser = webbrowser.get()
    if hasattr(browser, 'close'):
        browser.close()
    else:
        print("O navegador não suporta o método 'close'.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gerenciamento do projeto Django")
    parser.add_argument("action", choices=["requirements", "install", "run"], help="Ação a ser executada")

    args = parser.parse_args()

    if args.action == "requirements":
        requirements()
    elif args.action == "install":
        install_requirements()
    elif args.action == "run":
        run()  




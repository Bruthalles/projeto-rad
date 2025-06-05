relatorio_operacoes = []

def registrar_operacao(message):
    from datetime import datetime
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    relatorio_operacoes.append(f"[{agora}] {message}")

    log = f"[{agora}] {message}\n"

    with open('src/relatorio_operacoes.txt','a') as f:
        f.write(log)
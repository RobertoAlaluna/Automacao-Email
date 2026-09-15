import os
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv

load_dotenv()

EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
EMAIL_SENHA = os.getenv("EMAIL_SENHA")


def enviar_email(destinatario, assunto, corpo):
    mensagem = MIMEMultipart()
    mensagem["From"] = EMAIL_REMETENTE
    mensagem["To"] = destinatario
    mensagem["Subject"] = assunto

    mensagem.attach(MIMEText(corpo, "plain"))

    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(EMAIL_REMETENTE, EMAIL_SENHA)

    servidor.send_message(mensagem)
    servidor.quit()

    print(f"E-mail enviado para {destinatario}!")


def enviar_para_lista(caminho_csv, assunto, corpo):
    with open(caminho_csv, newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        contatos = list(leitor)

    print(f"Encontrei {len(contatos)} contato(s) no arquivo.")
    
    nomes = [contato["nome"] for contato in contatos]
    lista_nomes = ", ".join(nomes)
    
    confirmacao = input(f"Quer enviar o e-mail para: {lista_nomes}? (sim/nao): ")

    if confirmacao.lower() != "sim":
        print("Envio cancelado.")
        return

    for contato in contatos:
        enviar_email(contato["email"], assunto, corpo)

    print("Envio finalizado!")


if __name__ == "__main__":
    enviar_para_lista(
        caminho_csv="contatos.csv",
        assunto="Teste de envio em massa para contatos previamente cadastrados",
        corpo="Este é um teste do meu projeto de automação de envio de e-mails em massa com Python!"
    )
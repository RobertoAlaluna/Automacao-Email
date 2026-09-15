# 📧 Automação de E-mail em Massa com Python

Script em Python que automatiza o envio de e-mails para uma lista de contatos, usando o protocolo SMTP e autenticação segura via Gmail.

Projeto criado como estudo prático de automação, boas práticas de segurança (variáveis de ambiente) e manipulação de arquivos CSV.

<!-- 🎬 Adicione aqui um GIF ou print mostrando o projeto rodando -->
<!-- ![demo](caminho/para/seu-gif.gif) -->

## ✨ Funcionalidades

- Envio de e-mails individuais através de uma função reutilizável
- Leitura de uma lista de contatos a partir de um arquivo `.csv`
- Envio em massa para todos os contatos da lista
- Confirmação manual antes do disparo, evitando envios acidentais
- Credenciais protegidas com variáveis de ambiente (nunca expostas no código)

## 🛠️ Tecnologias

- [Python 3](https://www.python.org/)
- [smtplib](https://docs.python.org/3/library/smtplib.html) — biblioteca padrão para envio de e-mails via SMTP
- [python-dotenv](https://pypi.org/project/python-dotenv/) — carregamento de variáveis de ambiente
- Módulo `csv` — leitura da lista de contatos
- Módulo `email` — montagem das mensagens

## 📋 Pré-requisitos

- Python 3 instalado
- Uma conta Gmail com [Verificação em duas etapas](https://myaccount.google.com/signinoptions/two-step-verification) ativada
- Uma [Senha de app](https://myaccount.google.com/apppasswords) gerada para este projeto

## 🚀 Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/automacao-email.git
cd automacao-email
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure suas credenciais

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```
EMAIL_REMETENTE=seuemail@gmail.com
EMAIL_SENHA=suasenhadeapp
```

> ⚠️ Use uma [Senha de app](https://myaccount.google.com/apppasswords) do Google, nunca sua senha normal do Gmail.
> O arquivo `.env` nunca deve ser enviado ao GitHub (já está protegido pelo `.gitignore`).

### 4. Configure sua lista de contatos

Copie o arquivo de exemplo e renomeie:

```bash
cp contatos_exemplo.csv contatos.csv
```

Edite `contatos.csv` com os contatos reais que você deseja usar, seguindo o formato:

```
nome,email
João Silva,joao@gmail.com
Maria Souza,maria@gmail.com
```

> O arquivo `contatos.csv` também está no `.gitignore`, para proteger dados pessoais.

### 5. Execute o script

```bash
python main.py
```

O terminal vai mostrar quantos contatos foram encontrados e pedir confirmação antes de enviar:

```
Encontrei 2 contato(s) no arquivo.
Quer enviar o e-mail para: João Silva, Maria Souza? (sim/nao):
```

Digite `sim` para confirmar o envio.

## 🔒 Segurança

- Nenhuma credencial fica exposta no código — tudo é carregado a partir do `.env`
- A conexão com o servidor de e-mail usa TLS (`starttls()`)
- O envio em massa exige confirmação manual do usuário antes de disparar qualquer e-mail
- Dados pessoais (contatos reais) não são versionados no Git

## 📁 Estrutura do projeto

```
automacao-email/
├── .env                  # credenciais (não versionado)
├── .gitignore
├── contatos.csv           # lista real de contatos (não versionado)
├── contatos_exemplo.csv   # exemplo de formato, para outros testarem
├── main.py
├── README.md
└── requirements.txt
```

## 🔮 Possíveis melhorias futuras

- Interface web (Flask) para facilitar o uso por pessoas sem conhecimento técnico
- Suporte a envio de e-mails em HTML
- Suporte a anexos
- Agendamento de envios automáticos

## 📄 Licença

Este projeto é de uso livre para fins de estudo e aprendizado.
# Kuro - Discord AI Assistant 🤖

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

Kuro é um assistente inteligente para Discord que combina processamento de linguagem natural com a API do Google Gemini para proporcionar interações humanizadas e contextualizadas.

## ✨ Funcionalidades Principais

- **Conversação Natural**  
  Interaja usando o nome "Kuro" ou mencionando o bot:
"Kuro, qual a previsão do tempo?"
"@Kuro conte uma piada geek"

Copy

- **Memória Contextual**  
Mantém histórico das últimas interações por usuário

- **Aprendizado Adaptativo**  
Melhora respostas com base no feedback implícito

- **Multiplataforma**  
Funciona tanto em comandos quanto em mensagens regulares

## 🚀 Instalação

1. **Pré-requisitos**
 - Python 3.8+
 - Conta no [Google AI Studio](https://aistudio.google.com/)
 - Bot do Discord ([Guia de Criação](https://discordpy.readthedocs.io/en/stable/discord.html))

2. **Clonar Repositório**
 ```bash
 git clone https://github.com/seu-usuario/kuro-bot.git
 cd kuro-bot
Ambiente Virtual

bash
Copy
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
Instalar Dependências

bash
Copy
pip install -r requirements.txt
⚙️ Configuração
Crie um arquivo .env na raiz do projeto:

env
Copy
DISCORD_TOKEN=seu_token_aqui
GEMINI_API_KEY=sua_chave_gemini
Como obter as chaves:

DISCORD_TOKEN: Discord Developer Portal

GEMINI_API_KEY: Google AI Studio

💻 Uso
Iniciar o Bot:

bash
Copy
python bot.py
Exemplos de Interação:

Copy
Usuário: Kuro, explique quantum computing
Bot: A computação quântica usa qubits que podem existir em múltiplos estados simultaneamente...

Usuário: !reset
Bot: Histórico de conversa resetado!

Usuário: Oi @Kuro, como faço um loop em Python?
Bot: Em Python você pode usar 'for' ou 'while'. Por exemplo...
📚 Comandos
Comando	Descrição	Exemplo
!reset	Reseta o histórico da sessão	!reset

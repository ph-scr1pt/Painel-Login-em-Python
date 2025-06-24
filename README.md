# 🗝️ Painel de Login com Banco de Dados - DP Systems

Este é um projeto de um **Painel de Login** simples, desenvolvido em **Python**, utilizando **Tkinter** para a interface gráfica e **SQLite** para o armazenamento dos dados dos usuários.

O projeto foi desenvolvido como prática para aprender a trabalhar com interfaces gráficas e integração com banco de dados.

## 🚀 Funcionalidades

- 🔐 Login de usuários
- 🆕 Cadastro de novos usuários
- ✅ Validação de campos (limitação de caracteres e preenchimento obrigatório)
- 🗂️ Armazenamento dos dados no banco de dados SQLite (`UserData.db`)

## 🎨 Tecnologias Utilizadas

- 🐍 **Python**
- 🪟 **Tkinter** (Interface gráfica)
- 🗄️ **SQLite** (Banco de dados local)
- 🔗 Bibliotecas padrão (`tkinter`, `sqlite3`)

## 🗂️ Estrutura do Projeto

```
/Login-Panel
│
├── icons/                # Pasta com ícone e logo
│   ├── logo.png
│   └── icone.ico
├── __pycache__/          # Cache do Python
├── DataBaser.py          # Script de conexão e criação do banco de dados
├── Index.py              # Arquivo principal da interface e funcionalidades
├── README.md             # Documentação do projeto
└── UserData.db           # Banco de dados (gerado automaticamente)
```

## 🖥️ Como Executar

1. Clone este repositório:
```bash
git clone https://github.com/ph-scr1pt/Painel-Login-em-Python.git
```

2. Verifique se o Python está instalado. Se não estiver, baixe aqui:  
🔗 https://www.python.org/downloads/

3. Execute o arquivo principal:
```bash
python Index.py
```

O banco de dados `UserData.db` será criado automaticamente na primeira execução, se não existir.

## ⚠️ Observações Importantes

- Garanta que a pasta `icons` contenha os arquivos:
  - `logo.png`
  - `icone.ico`
- As credenciais dos usuários são armazenadas localmente no arquivo `UserData.db`.
- Este projeto é para fins educacionais e **não deve ser usado em produção sem melhorias na segurança**, como:
  - Hash de senhas
  - Proteções contra SQL Injection
  - Tratamento de erros mais robusto

## 📄 Licença

Este projeto está sob a licença MIT.

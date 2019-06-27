# VGBD

Para rodar esse projeto na sua máquina, você vai precisar do Python 3 instalado.

## Banco de dados

Popular o banco MySQL com o arquivo .sql.
Pode ser necessário configurar o usuário do banco de dados, no diretório:  `app/database/database.py`

## Bibliotecas

Para instalar as dependências necessárias, execute o comando:

```bash
pip install -r requirements.txt
```

## Server

Para iniciar o servidor `Flask` esteja na pasta raiz,
adicione as seguintes variáveis de ambiente:

```bash
export FLASK_CONFIG=development
export FLASK_APP=run.py
```

Execute

```bash
flask run
```

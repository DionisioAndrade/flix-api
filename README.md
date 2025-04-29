# API-Flix

A **API-Flix** é uma API RESTful desenvolvida para gerenciar um catálogo de filmes. Ela permite o cadastro, atualização, leitura e exclusão de filmes, gêneros, atores e outras informações associadas a filmes. A API foi projetada para ser fácil de usar e fornecer funcionalidades essenciais para manipulação e exibição de dados relacionados a filmes.

## Funcionalidades

- Cadastro de filmes
- Cadastro de gêneros de filmes
- Cadastro de atores
- Importar atores de arquivos CSV
- Manipulação de dados de filmes (criação, leitura, atualização, exclusão)
- Relacionamento entre filmes, gêneros e atores
-Avaliação de Filmes


## Tecnologias Utilizadas

- Python
- Django
- Django REST Framework
- Banco de Dados: SQLite (pode ser alterado conforme necessário)

## Como Começar

### 1. Clonando o Repositório

Clone este repositório para o seu ambiente local:

```bash
git clone https://github.com/DionisioAndrade/api-flix.git
```

### 2. Instalando dependências

```bash
pip install -r requirements.txt
```

### 3. Rodando a API
| ATENÇÃO, NUNCA UTILIZAR RUNSERVER EM PRODUÇÃO
```bash
python manage.py runserver
```

## Importe atores via CSV (opcional)
```bash
python manage.py import_actors {nome_do_arquivo.csv}
```

## Links úteis

* https://docs.djangoproject.com
* https://www.django-rest-framework.org/
* https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#




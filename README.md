# [rascunho-projeto-django4.2](/)

### Pré-requisitos

- Git
- Python v3.8.10

### Clonando o repositório

Clone o repositório e mude para diretório recém-criado.

```bash
$ git clone https://github.com/jvn20c/rascunho-projeto-django4.2.git && cd rascunho-projeto-django4.2/
```

### Criando seu ambiente virtual

Para criar o ambiente virtual:

```bash
$ python3 -m venv .venv
```

Agora vamos ativá-lo em nosso terminal:

```bash
$ source .venv/bin/activate
```

### Dependências locais

Então após baixar o repositório e estar com ambiente virtual `venv` ativo, não se esqueça de instalar as dependências e requisitos locais do projeto:

```bash
(.venv) $ pip install -r pacotes.txt
```

### Migrações

Para realizar as migrações.

```bash
$ python manage.py migrate
```

### (OPCIONAL) Criar um superusuário

Para criar um super-usuário e ter acesso à /admin/.

```bash
$ python manage.py createsuperuser
```

## Executando o projeto
Na raiz do projeto e com o ambiente virtual `venv` ativo, execute o seguinte comando:
```bash
$ python manage.py runserver
```
... e acesse o servidor de desenvolvimento em:
```bash
http://localhost:8000/
```

# fastapi-item-service
API de CRUD em python, utilizando FastAPI, Docker e JSON como banco de dados.

### Estrutura do Projeto

```sh
project/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   └── crud.py
│
├── data/
│   └── items.json
│
├── Dockerfile
└── requirements.txt
```



### Construir e Executar a Imagem Docker

```sh
docker build -t fastapi-docker-crud . 
docker run -d -p 80:80 fastapi-docker-crud
```



### Exemplos de Testes 

#### 1. Criar um novo item (POST)

```sh
curl -X POST \
  http://localhost:80/items/ \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Novo Item",
    "description": "Descrição do Novo Item",
    "price": 15.99,
    "on_offer": true
  }'
```

#### 2. Obter todos os itens (GET)

```sh
curl -X GET http://localhost:80/items/
```

#### 3. Obter um item específico por ID (GET)

```sh
curl -X GET http://localhost:80/items/1
```

#### 4. Atualizar um item existente por ID (PUT)

```sh
curl -X PUT \
  http://localhost:80/items/1 \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Item Atualizado",
    "description": "Descrição do Item Atualizado",
    "price": 19.99,
    "on_offer": false
  }'
```

#### 5. Excluir um item por ID (DELETE)

```sh
curl -X DELETE http://localhost:80/items/1
```

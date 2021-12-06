#Criar um crud para modelos de um pequeno ecommerce. Produto, Categoria, Fornecedor, Comprador.


from os import stat
from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic.main import BaseModel
from fastapi.params import Body


app = FastAPI()

# Produto

class BaseModelProduto(BaseModel):
    id: int
    nome: str
    valor: int

produtos = []

@app.post('/produtos', status_code=status.HTTP_201_CREATED)
def adicionar_produto(produto: BaseModelProduto):
    produtos.append(produto)

@app.put('/produtos/{id}', status_code=status.HTTP_202_ACCEPTED)
def alterar_produto(id: int, produto: BaseModelProduto): 
    resultado = list(filter(lambda x: x.id == id, produtos)) 
    if not resultado: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Produto com o nome: {id} não foi encontrado')

    produto_encontrado = resultado[0]
    produto_encontrado.id = produto.id
    produto_encontrado.nome = produto.nome
    produto_encontrado.valor = produto.valor
    return produto_encontrado


@app.patch('/produtos/alterar-valor/{valor}', status_code=status.HTTP_202_ACCEPTED)
def alterar_valor_produto(valor: int, valor_novo: int = Body(...)):
    resultado = list(filter(lambda x: x.valor == valor, produtos))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Produto com o valor: {valor} não foi encontrado')

    produto_encontrado = resultado[0]
    produto_encontrado.valor = valor_novo
    return produto_encontrado


@app.delete('/produtos/{id}', status_code=status.HTTP_202_ACCEPTED)
def remover_produto(id: int):
    resultado = list(filter(lambda x: x[1].id == id, enumerate(produtos)))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Produto com a descrição: {id} não foi encontrado')

    i, _ = resultado[0]
    del produtos[i]

@app.get('/produtos', status_code=status.HTTP_200_OK)
def listar_produtos():
    return produtos
#------------------------------------------------------------------------------
#Categoria

class BaseModelCategoria(BaseModel):
    id: int
    descricao: str

categorias = []

@app.post('/categorias', status_code=status.HTTP_201_CREATED)
def adicionar_categoria(categoria: BaseModelCategoria):
    categorias.append(categoria)

@app.put('/categorias/{descricao}', status_code=status.HTTP_202_ACCEPTED)
def alterar_categoria(descricao: str, categoria: BaseModelCategoria):
    resultado = list(filter(lambda a: a.descricao == descricao, categorias))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Categoria com a descrição {descricao} não encontrado')
    categoria_encontrada = resultado[0]
    categoria_encontrada.id = categoria.id
    categoria_encontrada.descricao = categoria.descricao
    return categoria_encontrada

@app.patch('/categorias/alterar-id/{id}', status_code=status.HTTP_202_ACCEPTED)
def alterar_id_categoria(id: int, id_novo: int = Body(...)):
    resultado = list(filter(lambda x: x.id == id, categorias))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Categoria com o id: {id} não foi encontrada')
    categoria_encontrada = resultado[0]
    categoria_encontrada.id = id_novo
    return categoria_encontrada

@app.delete('/categorias/{descricao}', status_code=status.HTTP_202_ACCEPTED)
def remover_categoria(descricao: str):
    resultado = list(filter(lambda x: x[1].descricao == descricao,enumerate(categorias)))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Categoria com a descricao: {descricao} não foi encontrada')    
    i, _ = resultado[0]
    del categorias[i]
	

@app.get('/categorias', status_code=status.HTTP_200_OK)
def listar_categoria():
    return categorias

#-------------------------------------------------------------------------------
# Fornecedor

class BaseModelFornecedor(BaseModel):
    id: int
    nome: str
    cnpj: int

fornecedores = []

@app.post('/fornecedores', status_code=status.HTTP_201_CREATED)
def adicionar_fornecedor(fornecedor: BaseModelFornecedor):
    fornecedores.append(fornecedor)

@app.put('/fornecedores/{id}', status_code=status.HTTP_202_ACCEPTED)
def alterar_categoria(id: int, fornecedor: BaseModelFornecedor):
    resultado = list(filter(lambda x: x.id == id, fornecedores))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Fornecedor com o id: {id} não foi encontrado')

    fornecedor_encontrado = resultado[0]
    fornecedor_encontrado.id = fornecedor.id
    fornecedor_encontrado.nome = fornecedor.nome
    fornecedor_encontrado.cnpj = fornecedor.cnpj
    return fornecedor_encontrado


@app.patch('/fornecedores/alterar-nome/{nome}', status_code=status.HTTP_202_ACCEPTED)
def alterar_nome_fornecedor(nome: str, novo_nome: str = Body(...)):
    resultado = list(filter(lambda x: x.nome == nome, fornecedores))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Fornecedor com o nome: {nome} não foi encontrado')
    fornecedor_encontrado = resultado[0]
    fornecedor_encontrado.nome = novo_nome
    return fornecedor_encontrado


@app.delete('/fornecedores/{cnpj}', status_code=status.HTTP_202_ACCEPTED)
def remover_fornecedor(cnpj: int):
    resultado = list(filter(lambda x: x[1].cnpj == cnpj, enumerate(fornecedores)))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Fornecedor com o cnpj: {cnpj} não foi encontrado')    
    i, _ = resultado[0]
    del fornecedores[i]
	
@app.get('/fornecedores', status_code=status.HTTP_200_OK)
def listar_fornecedor():
    return fornecedores

#-------------------------------------------------------------------------------
#Comprador 

class BaseModelComprador(BaseModel):
    nome: str
    cpf: int

compradores = []

@app.post('/compradores', status_code=status.HTTP_201_CREATED)
def adicionar_comprador(comprador: BaseModelComprador):
    compradores.append(comprador)

@app.put('/compradores/{nome}', status_code=status.HTTP_202_ACCEPTED)
def alterar_comprador(nome: str, comprador: BaseModelComprador): 
    resultado = list(filter(lambda x: x.nome == nome, compradores))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Comprador com o nome: {nome} não foi encontrado')

    comprador_encontrado = resultado[0]
    comprador_encontrado.nome = comprador.nome
    comprador_encontrado.cpf = comprador.cpf
    return comprador_encontrado

@app.patch('/compradores/alterar-nome/{nome}', status_code=status.HTTP_202_ACCEPTED)
def alterar_valor_produto(nome: str, novo_nome: str = Body(...)):
    resultado = list(filter(lambda x: x.nome == nome, compradores))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Comprador com o nome: {nome} não foi encontrado')
    comprador_encontrado = resultado[0]
    comprador_encontrado.nome = novo_nome
    return comprador_encontrado


@app.delete('/compradores/{cpf}', status_code=status.HTTP_202_ACCEPTED)
def remover_produto(cpf: int):
    resultado = list(filter(lambda x: x[1].cpf == cpf, enumerate(compradores)))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Comprador com o nome: {cpf} não foi encontrado')
    i, _ = resultado[0]
    del compradores[i]

@app.get('/compradores', status_code=status.HTTP_200_OK)
def listar_comprador():
    return compradores
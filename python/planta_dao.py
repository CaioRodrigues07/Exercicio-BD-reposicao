# planta_dao.py
# EXERCÍCIO: complete cada função no espaço indicado (onde está o TODO).
# Use sempre parâmetros (%s) e feche a conexão no finally.

from mysql.connector import Error

from connection_dao import close_connection, get_connection


# Questão 1: inserir uma planta.
# Deve inserir na tabela planta e devolver o id gerado (cursor.lastrowid).
# Lembre-se do commit!
def inserir_planta(nome, especie, preco, estoque):
    connection = get_connection()
    if connection is None:
        return None
    cursor = None
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO planta (nome, especie, preco, estoque) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nome, especie, preco, estoque))
        connection.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Erro ao inserir planta: {e}")
        return None
    finally:
        close_connection(connection, cursor)


# Questão 2: listar todas as plantas, ordenadas pelo id.
# Deve devolver a lista de tuplas (cursor.fetchall()).
def listar_plantas():
    connection = get_connection()
    if connection is None:
        return []
    cursor = None
    try:
        cursor = connection.cursor()
        sql = "SELECT id, nome, especie, preco, estoque FROM planta ORDER BY id"
        cursor.execute(sql)
        return cursor.fetchall()
    except Error as e:
        print(f"Erro ao listar plantas: {e}")
        return []
    finally:
        close_connection(connection, cursor)


# Questão 3: buscar as plantas de uma espécie.
# Deve devolver a lista de tuplas das plantas cuja espécie seja igual ao parâmetro.
def buscar_por_especie(especie):
    connection = get_connection()
    if connection is None:
        return []
    cursor = None
    try:
        cursor = connection.cursor()
        sql = "SELECT id, nome, especie, preco, estoque FROM planta WHERE especie = %s ORDER BY id"
        cursor.execute(sql, (especie,))
        return cursor.fetchall()
    except Error as e:
        print(f"Erro ao buscar plantas por espécie: {e}")
        return []
    finally:
        close_connection(connection, cursor)


# Questão 4: atualizar o preço de uma planta pelo id.
# Deve devolver True se alguma linha foi alterada (cursor.rowcount > 0), senão False.
def atualizar_preco(id_planta, novo_preco):
    connection = get_connection()
    if connection is None:
        return False
    cursor = None
    try:
        cursor = connection.cursor()
        sql = "UPDATE planta SET preco = %s WHERE id = %s"
        cursor.execute(sql, (novo_preco, id_planta))
        connection.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"Erro ao atualizar preço: {e}")
        return False
    finally:
        close_connection(connection, cursor)


# Questão 5: remover uma planta pelo id.
# Deve devolver True se alguma linha foi removida, senão False.
def remover_planta(id_planta):
    connection = get_connection()
    if connection is None:
        return False
    cursor = None
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM planta WHERE id = %s"
        cursor.execute(sql, (id_planta,))
        connection.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"Erro ao remover planta: {e}")
        return False
    finally:
        close_connection(connection, cursor)


# Questão 6 (Desafio): valor total do estoque.
# Deve devolver a soma de preco * estoque de todas as plantas, como float.
# Dica: SELECT COALESCE(SUM(preco * estoque), 0) FROM planta
def valor_total_estoque():
    connection = get_connection()
    if connection is None:
        return 0.0
    cursor = None
    try:
        cursor = connection.cursor()
        sql = "SELECT COALESCE(SUM(preco * estoque), 0) FROM planta"
        cursor.execute(sql)
        resultado = cursor.fetchone()
        return float(resultado[0])
    except Error as e:
        print(f"Erro ao calcular valor do estoque: {e}")
        return 0.0
    finally:
        close_connection(connection, cursor)

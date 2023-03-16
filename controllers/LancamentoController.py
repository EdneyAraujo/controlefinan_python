from typing import List
import services.database as db;
import models.Lancamentos as lancamento;



def Incluir(Lancamentos):
    count = db.cursor.execute("""
    INSERT INTO lancamentos (lanDescricao, lanValor, lanTipo, lanCategoria) 
    VALUES (?,?,?,?)""",
    Lancamentos.descricao, Lancamentos.valor, Lancamentos.tipo, Lancamentos.categoria).rowcount
    db.cnxn.commit()

def Excluir(id):
    count = db.cursor.execute("""
    DELETE FROM lancamentos WHERE id = ?""",
    id).rowcount
    db.cnxn.commit()

def SelecionarTodos():
    db.cursor.execute("SELECT * FROM lancamentos")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(lancamento.Lancamentos(row[0], row[1], row[2], row[3], row[4]))
    return costumerList


from modelos import TipoModel
from Managers.conexion import getCursor
from fastapi import APIRouter, Depends
import psycopg
from Managers.Managertipos import tipos

ClaseTipo=tipos()

router = APIRouter(prefix="/tipo", tags=["tipo routes"])

@router.post("/crear_tipo")
def post_tipo(tipo: TipoModel, cursor:psycopg.Cursor=Depends(getCursor) ):
    res= ClaseTipo.agregar_tipo ( tipo, cursor)
    return {res}

@router.get("/ver_tipos")
def get_tipo ( cursor:psycopg.Cursor=Depends(getCursor)):
    res= ClaseTipo.ver_tipo (cursor)
    return res

@router.delete("/borrar_tipo/{id}")
def delete_tipo (id: int, cursor:psycopg.Cursor=Depends(getCursor)):
    res= ClaseTipo.eliminar_tipo (id,cursor)
    return {res}

@router.put("/actualizar_tipo/{id}")
def update_tipo (id:int, Tipo:TipoModel, cursor:psycopg.Cursor=Depends(getCursor)):
    res= ClaseTipo.actualizar_tipo (id, Tipo, cursor)
    return {res}
    
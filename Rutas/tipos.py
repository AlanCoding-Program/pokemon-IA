from modelos import TipoModel
from Managers.conexion import getCursor
from fastapi import APIRouter, Depends
import psycopg
from Managers.Managertipos import tipos

ClaseTipo=tipos()

router = APIRouter(prefix="/Tipos", tags=["Tipos routes"])

@router.post("/crear_tipo")
def crear (tipo: TipoModel, cursor:psycopg.Cursor=Depends(getCursor) ):
    res= ClaseTipo.agregar_tipo( tipo, cursor)
    return {res}

@router.get("/ver_tipos")
def ver ( cursor:psycopg.Cursor=Depends(getCursor)):
    pass

@router.delete("/borrar_tipo/{id}")
def borrar (id: int, cursor:psycopg.Cursor=Depends(getCursor)):
    pass

@router.put("/actualizar_tipo/{id}")
def actualizar (id:int, Tipo:TipoModel, cursor:psycopg.Cursor=Depends(getCursor)):
    pass
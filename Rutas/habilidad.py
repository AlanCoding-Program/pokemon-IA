from modelos import HabilidadModel
from Managers.conexion import getCursor
from fastapi import APIRouter, Depends
import psycopg
from Managers.Managerhabilidad import habilidades

ClaseHabilidad= habilidades()

router = APIRouter(prefix="/habilidad", tags=["habilidad routes"])


@router.post("/crear_habilidad")
def habilidad_post (Habilidad: HabilidadModel, cursor:psycopg.Cursor=Depends(getCursor) ):
    res= ClaseHabilidad.agregar_habilidad (Habilidad, cursor)
    return {res}


@router.get("/ver_Habilidades")
def habilidad_get ( cursor:psycopg.Cursor=Depends(getCursor)):
    res= ClaseHabilidad.ver_habilidad (cursor)
    return res

@router.delete("/borrar_Habilidad/{id}")
def habilidad_delete (id: int, cursor:psycopg.Cursor=Depends(getCursor)):
    res= ClaseHabilidad.eliminar_habilidad (id,cursor)
    return {res}

@router.put("/actualizar_Habilidad/{id}")
def habilidad_put (id:int, Habilidad:HabilidadModel, cursor:psycopg.Cursor=Depends(getCursor)):
    res= ClaseHabilidad.actualizar_habilidad (id, Habilidad, cursor)
    return {res}



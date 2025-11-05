from modelos import HabilidadModel
from Managers.conexion import getCursor
from fastapi import APIRouter, Depends
import psycopg

router = APIRouter(prefix="/Habilidades", tags=["Habilidad routes"])

@router.post("/crear_habilidad")
def crear (Habilidad: HabilidadModel, cursor:psycopg.Cursor=Depends(getCursor) ):
    pass

@router.get("/ver_Habilidades")
def ver ( cursor:psycopg.Cursor=Depends(getCursor)):
    pass

@router.delete("/borrar_Habilidad/{id}")
def borrar (id: int, cursor:psycopg.Cursor=Depends(getCursor)):
    pass

@router.put("/actualizar_Habilidad/{id}")
def actualizar (id:int, Habilidad:HabilidadModel, cursor:psycopg.Cursor=Depends(getCursor)):
    pass


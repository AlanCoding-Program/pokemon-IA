from modelos import PokemonModel
from Managers.conexion import getCursor
from fastapi import APIRouter, Depends
import psycopg

router = APIRouter(prefix="/Pokemons", tags=["Pokemon routes"])

@router.post("/crear_pokemon")
def crear (Pokemon: PokemonModel, cursor:psycopg.Cursor=Depends(getCursor) ):
    pass

@router.get("/ver_pokemons")
def ver ( cursor:psycopg.Cursor=Depends(getCursor)):
    pass

@router.delete("/borrar_pokemon/{id}")
def borrar (id: int, cursor:psycopg.Cursor=Depends(getCursor)):
    pass

@router.put("/actualizar_pokemon/{id}")
def actualizar (id:int, pokemon:PokemonModel, cursor:psycopg.Cursor=Depends(getCursor)):
    pass
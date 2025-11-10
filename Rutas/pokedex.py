import psycopg
from modelos import PokedexModel
from fastapi import APIRouter, Depends
from Managers.conexion import getCursor
from Managers.Managerpokedex import pokedex

Clasepokedex= pokedex()

router = APIRouter(prefix="/pokedex" , tags=["pokedex routes"])

@router.post ("/agregar_pokedex")
def pokedex_post(pokedex:PokedexModel, cursor:psycopg.Cursor = Depends (getCursor)):
    res= Clasepokedex.agregar_pokedex (pokedex, cursor)
    return {res}


@router.get ("/ver_pokedex")
def pokedex_get (cursor:psycopg.Cursor = Depends (getCursor)):
    res= Clasepokedex.ver_pokedex(cursor)
    return res
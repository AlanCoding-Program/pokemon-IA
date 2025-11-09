from modelos import PokemonModel
from Managers.conexion import getCursor
from fastapi import APIRouter, Depends
import psycopg
from Managers.Managerpokemon import pokemons

ClasePokemon= pokemons()

router = APIRouter(prefix="/pokemon", tags=["pokemon routes"])

@router.post("/crear_pokemon")
def pokemon_post(Poke: PokemonModel, cursor:psycopg.Cursor=Depends(getCursor) ):
    res= ClasePokemon.agregar_pokemon (Poke,cursor)
    return {res}


@router.get("/ver_pokemons")
def pokemon_get ( cursor:psycopg.Cursor=Depends(getCursor)):
    res= ClasePokemon.ver_pokemon (cursor)
    return res


@router.delete("/borrar_pokemon/{id}")
def pokemon_delete (id: int, cursor:psycopg.Cursor=Depends(getCursor)):
    res= ClasePokemon.eliminar_pokemon (id,cursor)
    return {res}


@router.put("/actualizar_pokemon/{id}")
def pokemon_put (id:int, poke:PokemonModel, cursor:psycopg.Cursor=Depends(getCursor)):
    res = ClasePokemon.actualizar_pokemon (id,poke, cursor)
    return {res}
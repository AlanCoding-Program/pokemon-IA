from modelos import PokemonModel
from Managers.conexion import getCursor
from fastapi import APIRouter, Depends
import psycopg
from Managers.Managerpokemon import pokemons

router = APIRouter(prefix="/pokemon", tags=["pokemon routes"])

@router.post("/crear_pokemon")
def pokemon_post (Pokemon: PokemonModel, cursor:psycopg.Cursor=Depends(getCursor) ):
    return pokemons.agregar_pokemon (Pokemon,cursor)


@router.get("/ver_pokemons")
def pokemon_get ( cursor:psycopg.Cursor=Depends(getCursor)):
    return pokemons.ver_pokemon (cursor)


@router.delete("/borrar_pokemon/{id}")
def pokemon_delete (id: int, cursor:psycopg.Cursor=Depends(getCursor)):
    return pokemons.eliminar_pokemon (id,cursor)


@router.put("/actualizar_pokemon/{id}")
def pokemon_put (id:int, pokemon:PokemonModel, cursor:psycopg.Cursor=Depends(getCursor)):
    return pokemons.actualizar_pokemon (id,pokemon, cursor)
from pydantic import BaseModel

class PokemonModel(BaseModel):
    nombre:str

class HabilidadModel (BaseModel):
    habilidad:str

class TipoModel (BaseModel):
    tipo:str

class PokedexModel (BaseModel):
    pokemon_id: int
    tipo_id: int
    habilidad_id: int

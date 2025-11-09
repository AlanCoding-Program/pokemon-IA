from pydantic import BaseModel

class PokemonModel(BaseModel):
    nombre:str

class HabilidadModel (BaseModel):
    habilidad:str

class TipoModel (BaseModel):
    tipo:str
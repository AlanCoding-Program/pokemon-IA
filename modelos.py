from pydantic import BaseModel

class PokemonModel(BaseModel):
    Nombre:str

class HabilidadModel (BaseModel):
    Habilidad:str

class TipoModel (BaseModel):
    tipo:str
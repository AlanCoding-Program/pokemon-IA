from fastapi import FastAPI, Depends
from Rutas.habilidad import router as habilidadRouter
from Rutas.pokemon import router as pokemonRouter
from Rutas.tipos import router as tiposRouter

app = FastAPI()
app.include_router(habilidadRouter)
app.include_router(pokemonRouter)
app.include_router(tiposRouter)

@app.get ("/")
def fast():
    return("funka fastapi")




   



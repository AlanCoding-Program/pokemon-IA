from fastapi import FastAPI, Depends
from Rutas.habilidad import router as habilidadRouter
from Rutas.pokemon import router as pokemonRouter
from Rutas.tipos import router as tiposRouter
from Rutas.pokedex import router as pokedexRouter

app = FastAPI()
app.include_router(habilidadRouter)
app.include_router(pokemonRouter)
app.include_router(tiposRouter)
app.include_router(pokedexRouter)

@app.get ("/")
def fast():
    return("FastAPI funcionando en Vercel 🚀")




   



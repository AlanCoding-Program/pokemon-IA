from modelos import  PokedexModel
import psycopg

class pokedex:
    
    def agregar_pokedex (self, Pokedex: PokedexModel, cursor  ):
        cursor.execute("INSERT INTO pokedex (pokemon_id,tipo_id,habilidad_id) VALUES (%s,%s,%s)",(Pokedex.pokemon_id, Pokedex.tipo_id, Pokedex.habilidad_id))
        return "añadido a la pokedex!!!!"
    
    
    def ver_pokedex (self, cursor):
        res = cursor.execute( "SELECT pokemon.nombre, tipo.tipo, habilidad.habilidad FROM pokedex INNER JOIN pokemon ON pokedex.pokemon_id = pokemon.id_pokemon INNER JOIN tipo ON pokedex.tipo_id = tipo.id_tipo INNER JOIN habilidad ON pokedex.habilidad_id = habilidad.id_habilidad").fetchall()
        return [{"nombre": row[0], "tipo": row[1], "habilidad": row[2]} for row in res]
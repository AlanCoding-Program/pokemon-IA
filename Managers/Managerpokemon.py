from modelos import  PokemonModel
import psycopg

class pokemons:
    def agregar_pokemon (self, Pokemon:PokemonModel, cursor:psycopg.Cursor):

        cursor.execute ("INSERT INTO pokemon (nombre) VALUES (%s)", (Pokemon.nombre,))
        return "!!!pokemon agregado !!!"
    

    def ver_pokemon (self, cursor: psycopg.Cursor):

        res= cursor.execute ("SELECT nombre,id_pokemon FROM pokemon").fetchall()
        return [{"id": row [1] , "nombre": row [0]} for row in res]
    

    def eliminar_pokemon (self,id:int, cursor: psycopg.Cursor):
        cursor.execute ( "DELETE FROM pokemon WHERE id_pokemon=%s", (id,))
        return "pokemon eliminado"
    

    def actualizar_pokemon (self, id: int, Pokemon: PokemonModel, cursor:psycopg.Cursor):
        cursor.execute ("UPDATE  pokemon SET nombre= %s WHERE id_pokemon=%s", (Pokemon.nombre,id,))
        return "pokemon actualizado"
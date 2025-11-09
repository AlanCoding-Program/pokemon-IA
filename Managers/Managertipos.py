from modelos import TipoModel
import psycopg



class tipos:
  

    def agregar_tipo (self, Tipo:TipoModel, cursor: psycopg.Cursor ):
        cursor.execute ( "INSERT INTO tipo (tipo) VALUES (%s)", (Tipo.tipo,),)
        return "tipo agregado"
        
    
    def ver_tipo (self, cursor:psycopg.Cursor ):

       res=  cursor.execute ( "SELECT id_tipo, tipo FROM tipo").fetchall()
       return [{"id": row [0], "tipo": row[1]} for row in res]
    

    def actualizar_tipo (self, id:int, tipo:TipoModel, cursor:psycopg.Cursor):

        cursor.execute ("UPDATE Tipo SET Tipo=%s WHERE id_tipo=%s", (tipo.tipo,id,))
        return "tipo actualizado"

        
    def eliminar_tipo ( self,id:int, cursor:psycopg.Cursor):

        cursor.execute ( "DELETE FROM tipo WHERE id_tipo=(%s)", (id,))
        return "tipo eliminado"




        
    






        
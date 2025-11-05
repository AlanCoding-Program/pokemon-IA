from modelos import TipoModel
import psycopg



class tipos:
  

    def agregar_tipo (self, tipo:TipoModel, cursor: psycopg.Cursor ):
        cursor.execute ( "INSERT INTO Tipo (tipo) VALUES (%s)", (tipo.tipo,)),
        return "tipo agregado"
        
    
    def ver_tipos (self, cursor:psycopg.Cursor ):

       res=  cursor.execute ( "SELECT id_tipo Tipo FROM Tipo").fetchall()
       return [{"id_tipo": row [0], "Tipo": row[1]} for row in res]
    

    def actualizar_tipo (self, id:int, tipo:TipoModel, cursor:psycopg.Cursor):

        cursor.execute ("UPDATE Tipo SET Tipo=%s WHERE id_tipo=%s", tipo.Tipo,id)

        
    def eliminar_tipo ( self,id:int, cursor:psycopg.Cursor):

        cursor.execute ( "DELETE FROM Tipo WHERE id_tipo=(%s)", (id,))




        
    






        
from database.DB_connect import DBConnect

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    @staticmethod
    def get_all_rifugi():
        conn=DBConnect.get_connection()
        result=[]
        cursor=conn.cursor(dictionary=True)
        query="SELECT * FROM rifugio"
        cursor.execute(query)
        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_connessioni(anno):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)


        query = ("SELECT * FROM connessione "
                 "WHERE anno <= %s")

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result
import sqlite3

def obtenerUsuarios(self):  #metodos
        conn = sqlite3.connect(personas.db)
        cursor = conn.cursor()
        cursor.execute('select * from persons')
        self.gente = cursor.fetchall()
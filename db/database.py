from peewee import * 

db = SqliteDatabase('database.db')

class noticias(Model):
    conteudo = TextField()
    data = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])

    class Meta:
        database = db

db.connect()
db.create_tables([noticias])
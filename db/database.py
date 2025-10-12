from peewee import * 

db = SqliteDatabase('database.db')

def create(db, noticias):
    db.connect()
    db.create_tables([noticias], safe=True)
    db.close()

class noticias(Model):
    conteudo = TextField()
    data = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])

    class Meta:
        database = db

create(db, noticias)
from peewee import *
import peewee
# Criamos o banco de dados
sqlite_db = SqliteDatabase('db/database.db', pragmas={
    'journal_mode': 'wal',
    'cache_size': -1024 * 64})


class BaseModel(peewee.Model):

    class Meta:
        database = sqlite_db

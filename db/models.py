import peewee
from db.config_db import BaseModel
from peewee import *
from helpers.generator_index import generator_index
# models.py

class Link(BaseModel):

    index = CharField(unique=True)
    url = TextField()


def register_link(link) -> bool:
	indexs_database = [index.get("index") for index in list(Link.select(Link.index).dicts())]
	print(indexs_database)
	index = ""
	while index in indexs_database:
		index = generator_index()

	Link.insert(index=index, url=link).execute()
	return index


def get_link(index):
	link = list(Link.select(Link.url).where(Link.index == index).dicts())
	return link


if __name__ == '__main__':
	try:
		Link.create_table()
		print("Tabela 'Link' criada com sucesso!")

	except peewee.OperationalError:
		print("Tabela 'Link' ja existe!")
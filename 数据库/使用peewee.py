from peewee import *

db = SqliteDatabase('people.db')


class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db  # This model uses the "people.db" database.


class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db  # this model uses the "people.db" data


db.connect()
db.drop_tables([Person, Pet])
db.create_tables([Person, Pet], True)
from datetime import date

uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), is_relative=True)
print(uncle_bob.save())
bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
bob_kitty.name='Hello Kitty'
bob_kitty.save()
bob_kitty.delete()
db.close()

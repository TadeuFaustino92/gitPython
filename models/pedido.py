import uuid
from database import Database
import datetime

__author__ = 'Tadeu Faustino'

class Pedido(object):
    def __init__(self, nome, email, telefone, pedido, date=datetime.datetime.utcnow(), id=None):   # valores default só no final
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.pedido = pedido
        self.created_dade = date
        self.id = uuid.uuid4().hex if id is None else id # unique id: 4 = random

    def save_to_mongo(self):
        Database.insert(collection='pedidos',
                        data=self.json())

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone,
            'pedido': self.pedido,
            'created_date': self.created_dade
        }

    @staticmethod
    def from_mongo(id):
        data = Database.find_one(collection='pedidos', query={'id': id})



from models.pedido import Pedido
from database import Database

__author__ = 'Tadeu Faustino'

Database.initialize()

pedido = Pedido(nome="Tadeu",
                email="tadeu@gmil.com",
                telefone="23466954",
                pedido="Lagosta",
                date="12/12/12",
                id="001")

pedido.save_to_mongo()

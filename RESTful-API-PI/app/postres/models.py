#from operator import length_hint
#from sqlalchemy.orm import backref

from app.db import db, BaseModelMixin
import datetime


class Usuario(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String)
    password = db.Column(db.String)
    token = db.Column(db.String)

    def __init__(self, usuario, password):
        self.usuario = usuario
        self.password = password
        self.token = ""

    def __repr__(self):
        return f'Usuario({self.usuario})'
    def __str__(self):
        return f'{self.usuario}'



class PostreDisponible(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    precio = db.Column(db.Numeric)
    
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __repr__(self):
        return f'PostreDisponible({self.nombre}, {self.precio})'
    
    def __str__(self):
        return f'{self.nombre} - {self.precio}'


class PedidoDePostre(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    id_postre = db.Column(db.Integer, db.ForeignKey('postre_disponible.id'), nullable=False)
    cantidad = db.Column(db.Integer)
    estado = db.Column(db.String)
    
    def __init__(self, id_usuario, id_postre, cantidad, estado):
        self.id_usuario = id_usuario
        self.id_postre = id_postre
        self.cantidad = cantidad
        self.estado = estado
    
    def __repr__(self):
        return f'PedidoDePostre({self.id_usuario}, {self.id_postre})'
    
    def __str__(self):
        return f'Pedido {self.id} - Usuario: {self.id_usuario}, Postre: {self.id_postre}, Cantidad: {self.cantidad}, Estado: {self.estado}'



# class Luminosidad(db.Model, BaseModelMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     valor = db.Column(db.Float)
#     timestamp = db.Column(db.DateTime)
#     status = db.Column(db.String)
#     usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

#     def __init__(self, valor, timestamp, status, usuario_id):
#         self.valor = valor
#         self.timestamp = timestamp
#         self.status = status
#         self.usuario_id = usuario_id
    
#     def __repr__(self):
#         return f'Luminosidad({self.valor})'
#     def __str__(self):
#         return f'{self.valor}'

# class Movimiento(db.Model, BaseModelMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     valor = db.Column(db.Float)
#     timestamp = db.Column(db.DateTime)
#     status = db.Column(db.String)
#     usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

#     def __init__(self, valor, timestamp, status, usuario_id):
#         self.valor = valor
#         self.timestamp = timestamp
#         self.status = status
#         self.usuario_id = usuario_id
    
#     def __repr__(self):
#         return f'Movimiento({self.valor})'
#     def __str__(self):
#         return f'{self.valor}'

# class Distancia(db.Model, BaseModelMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     valor = db.Column(db.Float)
#     timestamp = db.Column(db.DateTime)
#     status = db.Column(db.String)
#     usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

#     def __init__(self, valor, timestamp, status, usuario_id):
#         self.valor = valor
#         self.timestamp = timestamp
#         self.status = status
#         self.usuario_id = usuario_id
    
#     def __repr__(self):
#         return f'Distancia({self.valor})'
#     def __str__(self):
#         return f'{self.valor}'


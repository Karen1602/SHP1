from marshmallow import fields

from app.ext import ma
from app.db import db, BaseModelMixin
import datetime

class UsuarioSchema(ma.Schema):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String)
    password = db.Column(db.String)
    token = db.Column(db.String)

class PostreDisponibleSchema(ma.Schema):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    precio = db.Column(db.Numeric)

class PedidoDePostreSchema(ma.Schema):
    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    id_postre = db.Column(db.Integer, db.ForeignKey('postre_disponible.id'), nullable=False)
    cantidad = db.Column(db.Integer)
    estado = db.Column(db.String)




# class MovimientoSchema(ma.Schema):
#     id = fields.Integer(dump_only=True)
#     timestamp = fields.DateTime()
#     status = fields.String()
#     usuario_id = fields.Integer()

# class DistanciaSchema(ma.Schema):
#     id = fields.Integer(dump_only=True)
#     valor = fields.Number()
#     timestamp = fields.DateTime()
#     status = fields.String()
#     usuario_id = fields.Integer()

# class UsuarioSchema(ma.Schema):
#     id = fields.Integer(dump_only=True)
#     usuario = fields.String()
#     password = fields.String()
#     token = fields.String()

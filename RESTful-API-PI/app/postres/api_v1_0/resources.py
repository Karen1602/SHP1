from flask import request, Blueprint
from flask_restful import Api, Resource

from .schemas import PostreDisponibleSchema
from ..models import PostreDisponible

postres_v1_0_bp = Blueprint('postres_v1_0_bp', __name__)

api = Api(postres_v1_0_bp)

postre_schema = PostreDisponibleSchema()

class PostreDisponibleListResource(Resource):
    def get(self):
        postres = PostreDisponible.query.all()
        result = postre_schema.dump(postres, many=True)
        return result

    def post(self):
        data = request.get_json()
        postre_dict = postre_schema.load(data)
        postre = PostreDisponible(nombre=postre_dict['nombre'], precio=postre_dict['precio'])
        postre.save()
        resp = postre_schema.dump(postre)
        return resp, 201

class PostreDisponibleResource(Resource):
    def get(self, postre_id):
        postre = PostreDisponible.query.get(postre_id)
        if postre is None:
            raise ObjectNotFound('El postre no existe')
        resp = postre_schema.dump(postre)
        return resp

    def put(self, postre_id):
        postre = PostreDisponible.query.get(postre_id)
        if postre is None:
            raise ObjectNotFound('El postre no existe')
        data = request.get_json()
        postre_dict = postre_schema.load(data)
        postre.nombre = postre_dict["nombre"]
        postre.precio = postre_dict["precio"]
        postre.save()
        resp = postre_schema.dump(postre)
        return resp, 200

    def delete(self, postre_id):
        postre = PostreDisponible.query.get(postre_id)
        if postre is None:
            raise ObjectNotFound('El postre no existe')
        postre.delete()
        return "", 204
    
api.add_resource(PostreDisponibleListResource, '/api/v1.0/postre/', endpoint='postre_list_resource')
api.add_resource(PostreDisponibleResource, '/api/v1.0/postre/<int:postre_id>', endpoint='postre_resource')

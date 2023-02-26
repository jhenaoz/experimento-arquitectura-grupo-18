from flask_restful import Resource
from app.modelos import DetalleEntrega, DetalleEntregaSchema

detalle_entrega = DetalleEntregaSchema()

class VistaDetallesEntregas(Resource):
    def get(self):
        return [detalle_entrega.dump(r) for r in DetalleEntrega.query.all()]


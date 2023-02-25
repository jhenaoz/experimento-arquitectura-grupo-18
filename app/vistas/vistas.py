from flask_restful import Resource
from app.modelos import DetalleEntrega, DetalleEntregaSchema

detalle_entrega = DetalleEntregaSchema()

class VistaDetallesEntregas(Resource):
    def get(self):
        detalles_entregas = []
        detalles_entregas_respuesta = DetalleEntrega.query.all()
        if not detalles_entregas_respuesta:
            return detalles_entregas
        else:
            for detalle_entrega in detalles_entregas_respuesta:
                detalle = {
                    "id": detalle_entrega.id,
                    "Fecha Salida": detalle_entrega.fecha_salida,
                    "Fecha llegada": detalle_entrega.fecha_llegada,
                    "Notas": detalle_entrega.notas,
                    "Volumen": detalle_entrega.volumen,
                    "Status": detalle_entrega.status
                }
                detalles_entregas.append(detalle)
            return detalle


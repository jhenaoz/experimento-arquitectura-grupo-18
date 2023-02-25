import enum
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
db = SQLAlchemy()

class EnumEstado(enum.Enum):
    PROGRAMADO: str = 'PROGRAMADO'
    EN_CURSO: str = 'EN CURSO'
    ENTREGADO: str = 'ENTREGADO'

class DetalleEntrega(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_salida = db.Column(db.Date)
    fecha_llegada = db.Column(db.Date)
    fotos = db.Column(db.String(512))
    notas = db.Column(db.String(512))
    status = db.Column(db.Enum(EnumEstado))
    volumen = db.Column(db.Numeric)

class DetalleEntregaSchema(Schema):
    class Meta:
        model = DetalleEntrega
        include_relationships = True
        load_instance = True

    id = fields.String()
    status = EnumEstado
    volumen = fields.String()

from flask_cors import CORS
from .modelos import db
from flask_restful import Api
from app.vistas import VistaDetallesEntregas
import os
from app import create_app

app = create_app('default')
app_context= app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
cors = CORS(app)
api = Api(app)

api.add_resource(VistaDetallesEntregas, '/distribuciones')

print('Starting server')
@app.route('/ping')
def ping():
    return "ok"

@app.route('/kill-program')
def fail():
    os._exit(12)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

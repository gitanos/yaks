import os

from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app, prefix='/yak-shop')

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'randomkey')
app.config['PROPOGATE_EXCEPTIONS'] = True


@app.before_request
def before_request():
    # Debug request incoming
    if True:
        from flask import request
        print("HEADERS", request.headers)
        print("REQ_path", request.path)
        print("ARGS",request.args)
        print("DATA",request.data)
        print("FORM",request.form)

@app.after_request
def add_cors(response):
    """Set CORS headers for each request. All domains are allowed in debug mode."""
    CORS_DOMAIN = "*"
    response.headers.add('Access-Control-Allow-Origin', CORS_DOMAIN)
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    response.headers.add('Access-Control-Max-Age', 86400)
    return response

# avoid circularity
import endpoints

api.add_resource(endpoints.Load, '/load')
api.add_resource(endpoints.StockT, '/stock/<int:T>')
api.add_resource(endpoints.HerdT, '/herd/<int:T>')

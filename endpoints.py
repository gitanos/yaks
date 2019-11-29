import json
import xml.etree.ElementTree as ET

from flask import request, Response
from flask_restful import Resource, abort, reqparse

from main import get_stock_info, get_herd_info

parser = reqparse.RequestParser()

class Load(Resource):
    def post(self):

        if request.content_type not in ['application/xml', 'text/xml']:
            return Response('Unsupported Media Type', 415)

        try:
            tree = ET.XML(str(request.data, 'utf-8'))
        except Exception as e:
            print(str(e))
            abort(400)

        with open("load.xml", "wb") as f:
            f.write(ET.tostring(tree))

        # print('\n Data Json ', json.dumps(xmltodict.parse(request.data, attr_prefix='@', cdata_key='#text', dict_constructor=dict)))
        # print('\n Back to XML: ', xmltodict.unparse(xmltodict.parse(request.data), pretty=True))

        return Response("Response: status=205", status=205)


class StockT(Resource):
    def get(self, T):

        try:
            # get stock info
            info_stock = get_stock_info(days=T)
        except Exception as e:
            print(str(e))
            abort(400)

        output = json.dumps(info_stock, sort_keys=True, indent=4)

        return Response(output, 200)


class HerdT(Resource):
    def get(self, T):

        try:
            # get herd info
            info_herd = get_herd_info(days=T)
        except Exception as e:
            print(str(e))
            abort(400)

        output = json.dumps(info_herd, indent=4)

        return Response(output, 200)


class Order(Resource):
    def post(self, T):

        parser.add_argument('order', type=dict)
        data = parser.parse_args()

        milk_ord = float(data['order']['milk'])
        wool_ord = float(data['order']['skins'])
        #print('JSON', request.get_json(force=True))

        try:
            # get stock info
            instock = get_stock_info(days=T)
        except Exception as e:
            print(str(e))
            abort(400)

        mis = instock['milk']
        wis = instock['skins']
        if mis >= milk_ord and wis >= wool_ord:
            return Response(json.dumps(data['order']), 201)
        elif mis < milk_ord and wis >= wool_ord:
            return Response(json.dumps({'skins': wool_ord}), 206)
        elif mis >= milk_ord and wis < wool_ord:
            return Response(json.dumps({'milk': milk_ord}), 206)
        else:
            return Response('Not in stock', 404)


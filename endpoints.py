import json
import xml.etree.ElementTree as ET

from flask import request, Response, jsonify
from flask_restful import Resource, abort

from main import get_stock_info, get_herd_info


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

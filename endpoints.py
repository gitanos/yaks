from flask import request, Response
from flask_restful import Resource, abort

import xml.etree.ElementTree as ET


class Load(Resource):
    def post(self):

        if request.content_type not in ['application/xml', 'text/xml']:
            return Response('Unsupported Media Type', 415)

        try:
            tree = ET.XML(str(request.data, 'utf-8'))
        except Exception as e:
            abort(400, str(e))

        with open("load.xml", "wb") as f:
            f.write(ET.tostring(tree))

        # print('\n Data Json ', json.dumps(xmltodict.parse(request.data, attr_prefix='@', cdata_key='#text', dict_constructor=dict)))
        # print('\n Back to XML: ', xmltodict.unparse(xmltodict.parse(request.data), pretty=True))

        return Response("Response: status=205", status=205)

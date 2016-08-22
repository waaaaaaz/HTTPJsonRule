#coding: utf-8

from flask import Blueprint, request
from flask_restful import Resource, Api

from HTTPJsonRule.response import SaveResponse


API_VERSION_V1 = 1
API_VERSION = API_VERSION_V1

api_v1_bp = Blueprint('api_v1', __name__)
api_v1 = Api(api_v1_bp)

class HTTPSave(Resource):
	def post(self):
		if request.get_json:
			return SaveResponse(request.get_json())

api_v1.add_resource(HTTPSave, '/save')
#coding: utf-8

from flask import Blueprint, request
from flask_restful import Resource, Api
from HTTPJsonRule.response import ReqResponse


API_VERSION_V2 = 2
API_VERSION = API_VERSION_V2

api_v2_bp = Blueprint('api_v2', __name__)
api_v2 = Api(api_v2_bp)

class HTTPRequest(Resource):
	def post(self):
		if request.get_json:
			return ReqResponse(request.get_json())

api_v2.add_resource(HTTPRequest, '/request')
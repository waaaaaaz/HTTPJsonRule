#coding: utf-8

import json
import ast

import requests

from builder import Save
from exceptions import ValidationError


def ReqResponse(json_dict):

	try:
		Validate_To_Request(json_dict)
	except ValidationError, problem:
		return problem.message
	return _request(json_dict)

def _request(json_dict):
	response_dict = {}
	r_url = json_dict['url']
	r_method = json_dict['method'].lower()
	if r_method == 'get':
		r = requests.get(r_url)
	elif r_method == 'post':
		r_json = ast.literal_eval(json_dict['json'])
		r = requests.post(r_url, json=r_json)
	response_dict['response_header'] = dict(r.headers)
	response_dict['response_status'] = r.status_code
	response_dict['response_encoding'] = r.encoding
	try:
		response_dict['response_content'] = json.loads(r.content)
	except Exception:
		return "response mediatype is not JSON"
	return response_dict

def SaveResponse(json_dict):

	try:
		Validate_To_Save(json_dict)
	except ValidationError, problem:
		return problem.message
	else:
		return Save(json_dict)

def Validate_To_Request(json_dict):

	if not json_dict['url']:
		raise ValidationError("No url value for http request")
	if not json_dict['method']:
		raise ValidationError("No method value for http request")
	if json_dict['method'] == 'POST' and not json_dict['json']:
		raise ValidationError("No json value for http request")


def Validate_To_Save(json_dict):

	if not json_dict['url']:
		raise ValidationError("No request url value for test case")
	if not json_dict['method']:
		raise ValidationError("No reuqest method value for test case")
	if not json_dict['resp_status']:
		raise ValidationError("No response status value for test case")
	if not json_dict['resp_header']:
		raise ValidationError("No response head value for test case")
	if not json_dict['resp_content']:
		raise ValidationError("No response json value for test case")
	if json_dict['method'] == 'POST' and not json_dict['json']:
		raise ValidationError("No reuqest json value for test case")

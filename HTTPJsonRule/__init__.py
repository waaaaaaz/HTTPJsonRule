#coding: utf-8
import os

from flask import Flask
from flask.ext.cors import CORS

from HTTPJsonRule.api.httpsave import api_v1, api_v1_bp, API_VERSION_V1
from HTTPJsonRule.api.httprequest import api_v2, api_v2_bp, API_VERSION_V2
from HTTPJsonRule.posts.views import posts


def create_app(environment=None):
	HTTPJsonRule = Flask(__name__)

	if not environment:
		environment = os.environ.get('FLASK_CONFIG', 'development')
	HTTPJsonRule.config.from_object('HTTPJsonRule.config.{}'.format(environment.capitalize()))
	HTTPJsonRule.config.from_pyfile(
		'config_{}.py'.format(environment.lower()),
		silent=True
		)

	HTTPJsonRule.register_blueprint(
		api_v1_bp,
		url_prefix='{prefix}/v{version}'.format(prefix=HTTPJsonRule.config['URL_PREFIX'], version=API_VERSION_V1)
		)

	HTTPJsonRule.register_blueprint(
		api_v2_bp,
		url_prefix='{prefix}/v{version}'.format(prefix=HTTPJsonRule.config['URL_PREFIX'], version=API_VERSION_V2)
		)

	HTTPJsonRule.register_blueprint(posts)

	CORS(HTTPJsonRule)

	return HTTPJsonRule

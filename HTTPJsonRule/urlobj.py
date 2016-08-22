# coding: utf-8

from urlparse import urlparse

class Urlobj(object):

	def __init__(self, url_str):

		self.url = url_str
		self.scheme = urlparse(url_str).scheme
		self.port = str(urlparse(url_str).port)
		self.netloc = urlparse(url_str).netloc
		self.path = urlparse(url_str).path
		self.query = urlparse(url_str).query

	def __repr__(self):
		return repr(self.__dict__)


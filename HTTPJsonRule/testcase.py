# coding: utf-8

import re
import os
import json

from model import Model
from urlobj import Urlobj


class TestCase(Model):

	def __init__(self, param_dict):
		super(self.__class__, self).__init__(param_dict)
		self._obj_for_testcase()


	def _obj_for_testcase(self):

		setattr(self, 'resquest_url', self.url)
		setattr(self, 'request_method', self.method)
		setattr(self, 'request_json', self.json)
		setattr(self, 'response_status', self.resp_status.split(':')[1].strip())
		setattr(self, 'response_head', json.loads(self.resp_header))
		setattr(self, 'response_json', self.resp_content)
		setattr(self, 'response_encoding', self.response_head['Content-Type'].split(';')[1].split('=')[1])
		setattr(self, 'response_content_type', self.response_head['Content-Type'].split(';')[0])
		setattr(self, 'testcase_description', None)
		setattr(self, 'testcase_path', self._testcase_path())
		setattr(self, 'testcase_name', self._testcase_name())

	def _testcase_path(self):

		url_path = Urlobj(self.url).path
		url_path_item = re.split('[^A-Za-z0-9]', url_path)
		new_separator = os.path.sep
		new_path = Urlobj(self.url).netloc + new_separator.join(url_path_item)
		testcase_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'testcase_output', new_path))
		return testcase_path

	def _testcase_name(self):

		tcpath = self._testcase_path()
		patten = re.compile('^(?:testcase)(\d+)(\.)')
		num_flag = 0
		full_name = "testcase001.py"
		if not os.path.exists(tcpath):
			print "xxxxxxxxxxxx"
			os.makedirs(tcpath)
			return full_name
		elif not os.listdir(tcpath):
			return full_name
		elif full_name not in os.listdir(tcpath):
			return full_name
		elif full_name in os.listdir(tcpath):
			while (full_name in os.listdir(tcpath)):
				full_name = _increment(full_name)
			return full_name

def _increment(full_name):
	
	patten = re.compile('^(?:testcase)(\d+)(\.)')
	history_name = patten.search(full_name)
	if history_name:
		num_name = str(int(history_name.group(1))+1)
		start, end = history_name.span(1)
		full_name = full_name[:max(end-len(num_name), start)] + num_name + full_name[end:]
	return full_name
	



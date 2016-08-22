# coding: utf-8

import requests
import unittest
import json
from jsonschema import validate


url = "http://www.omdbapi.com/?y=&plot=short&r=json&s=silicon"
req_json = None

class HTTPTest(unittest.TestCase):

	'''
	description for test case
	'''

	@classmethod
	def setUpClass(cls):
		r = requests.get(url)	    
		cls.status = r.status_code
		cls.header = r.headers
		cls.json = r.json()
		super(HTTPTest, cls).setUpClass()

	@classmethod
	def tearDownClass(self):
		pass

	def testStatus(self):
		status = self.status
		expected_status = 200
		self.assertEqual(status, expected_status)

	def testEncoding(self):
		encoding = self.header['Content-Type'].split(';')[1]
		expected_encoding = "utf-8"
		self.assertIsNotNone(encoding)
		self.assertIn(expected_encoding.lower(), encoding.lower())

	def testContentType(self):
		content_type = self.header['Content-Type'].split(';')[0]
		expected_contenttype = "application/json"
		self.assertIsNotNone(content_type)
		self.assertIn(expected_contenttype, content_type.lower())

	def testResponseJson(self):
		response_json = self.json
		expected_jsonschema = json.load(open(__file__[:-2:] + "schema.json"))
		valid = False
		try:
			validate(response_json, expected_jsonschema)
			valid = True
		except Exception as e:
			print "invalid :\n\t{0}".format(str(e))
		self.assertTrue(valid)




if __name__ == '__main__':
	unittest.main()

#coding: utf-8


import os
import json

from jinja2 import Environment, FileSystemLoader

from testcase import TestCase
from generator import SchemaGenerator


def Save(json_dict):
	local_json = TestCase(json_dict)
	template_dir = os.path.join(os.path.dirname(__file__), 'testcase_templates')
	env = Environment(loader=FileSystemLoader(template_dir))
	output = env.get_template('testcase.py.tmpl').render(local_json.__dict__)
	tc_file = local_json.testcase_path + os.path.sep + local_json.testcase_name
	json_file = tc_file[:-2:] + "schema.json"
	with open(tc_file, 'w') as f:
		f.write(output)
	resp_dict = json.loads(local_json.response_json)
	json_output = SchemaGenerator(resp_dict).to_dict()
	with open(json_file, 'w') as f:
		f.write(json.dumps(json_output))

	return "a testcase \" {0} \" created".format(tc_file)






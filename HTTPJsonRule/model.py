# coding: utf-8

class Model(object):

	def __init__(self, param_dict):
		self._obj_from_json(param_dict)

	def __repr__(self):
		return repr(self.__dict__)
		#return repr("<{0} : ======> \n  {1}>".format(self.__class__.__name__, self.__dict__))

	def items(self):
		return self.__dict__.items()

	def __getitem__(self, key):
		return self.__dict__[key]

	def __setitem__(self, key, item):
		self.__dict__[key] = item

	def _obj_from_json(self, param_dict):
		for a, b in param_dict.items():
			if isinstance(b, (list, tuple)):
				setattr(self, a, [Model(x) if isinstance(x, dict) else x for x in b])
			else:
				setattr(self, a, Model(b) if isinstance(b, dict) else b)

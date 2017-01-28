

#calss header
class _PREFERRED():
	def __init__(self,): 
		self.name = "PREFERRED"
		self.definitions = [u'liked or wanted more than anything else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

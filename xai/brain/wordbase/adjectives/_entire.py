

#calss header
class _ENTIRE():
	def __init__(self,): 
		self.name = "ENTIRE"
		self.definitions = [u'whole or complete, with nothing missing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

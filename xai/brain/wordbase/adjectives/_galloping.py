

#calss header
class _GALLOPING():
	def __init__(self,): 
		self.name = "GALLOPING"
		self.definitions = [u'increasing or developing at a very fast rate that cannot be controlled: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

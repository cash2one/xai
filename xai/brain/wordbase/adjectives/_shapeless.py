

#calss header
class _SHAPELESS():
	def __init__(self,): 
		self.name = "SHAPELESS"
		self.definitions = [u'without a clear form or structure: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _PROPITIATORY():
	def __init__(self,): 
		self.name = "PROPITIATORY"
		self.definitions = [u'intended to please someone and make them feel calm: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

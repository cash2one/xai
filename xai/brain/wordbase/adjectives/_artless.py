

#calss header
class _ARTLESS():
	def __init__(self,): 
		self.name = "ARTLESS"
		self.definitions = [u'simple and not wanting to deceive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

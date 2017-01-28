

#calss header
class _VANILLA():
	def __init__(self,): 
		self.name = "VANILLA"
		self.definitions = [u'used to describe a product or service that is basic and has no special features: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

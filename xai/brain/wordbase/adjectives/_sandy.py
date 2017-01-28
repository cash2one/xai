

#calss header
class _SANDY():
	def __init__(self,): 
		self.name = "SANDY"
		self.definitions = [u'covered with sand or containing sand: ', u'Sandy hair is a pale brownish-orange colour.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

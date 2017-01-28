

#calss header
class _GODLESS():
	def __init__(self,): 
		self.name = "GODLESS"
		self.definitions = [u'not having or believing in God or gods: ', u'bad or evil']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

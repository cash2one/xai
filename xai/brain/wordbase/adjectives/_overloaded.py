

#calss header
class _OVERLOADED():
	def __init__(self,): 
		self.name = "OVERLOADED"
		self.definitions = [u'having or supplied with too much of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

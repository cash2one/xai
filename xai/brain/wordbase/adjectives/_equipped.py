

#calss header
class _EQUIPPED():
	def __init__(self,): 
		self.name = "EQUIPPED"
		self.definitions = [u'having the necessary tools, clothes, equipment, etc.: ', u'having the skills needed to do something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

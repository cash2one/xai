

#calss header
class _LEXICAL():
	def __init__(self,): 
		self.name = "LEXICAL"
		self.definitions = [u'relating to words']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

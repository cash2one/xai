

#calss header
class _GRAMMATICAL():
	def __init__(self,): 
		self.name = "GRAMMATICAL"
		self.definitions = [u'relating to grammar or obeying the rules of grammar: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

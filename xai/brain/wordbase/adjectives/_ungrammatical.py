

#calss header
class _UNGRAMMATICAL():
	def __init__(self,): 
		self.name = "UNGRAMMATICAL"
		self.definitions = [u'not grammatical']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

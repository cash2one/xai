

#calss header
class _NEUTER():
	def __init__(self,): 
		self.name = "NEUTER"
		self.definitions = [u'relating to a particular gender (= class of nouns) in some languages: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

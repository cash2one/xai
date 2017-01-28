

#calss header
class _PARADIGMATIC():
	def __init__(self,): 
		self.name = "PARADIGMATIC"
		self.definitions = [u'relating to the way different words or language items can be chosen to play a particular part in a language structure: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

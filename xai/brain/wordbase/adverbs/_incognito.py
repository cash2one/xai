

#calss header
class _INCOGNITO():
	def __init__(self,): 
		self.name = "INCOGNITO"
		self.definitions = [u'avoiding being recognized, by changing your name or appearance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _IRRELEVANT():
	def __init__(self,): 
		self.name = "IRRELEVANT"
		self.definitions = [u'not related to what is being discussed or considered and therefore not important: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _CONTRADICTORY():
	def __init__(self,): 
		self.name = "CONTRADICTORY"
		self.definitions = [u'If two or more facts, pieces of advice, etc. are contradictory, they are very different from each other: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

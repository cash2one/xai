

#calss header
class _DOWNWARD():
	def __init__(self,): 
		self.name = "DOWNWARD"
		self.definitions = [u'\u2192\xa0 downwards ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
